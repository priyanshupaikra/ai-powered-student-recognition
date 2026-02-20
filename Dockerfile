# syntax=docker/dockerfile:1

FROM python:3.13-slim AS base
WORKDIR /app

# Builder stage: install dependencies in a venv
FROM base AS builder

# Bind requirements.txt for pip install, use cache for pip
COPY --link requirements.txt ./
RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    --mount=type=cache,target=/root/.cache/pip \
    python -m venv .venv && \
    .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install -r requirements.txt

# Final stage: copy app code and venv, set up non-root user
FROM base AS final

# Create non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Copy installed venv from builder
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy application code (excluding .env, .git, etc. via .dockerignore)
COPY --link . .

# Set permissions for non-root user
RUN chown -R appuser:appgroup /app
USER appuser

# Expose port (commonly 8000 for Django, can be adjusted)
EXPOSE 8000

# Default command: run Django app via manage.py
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
