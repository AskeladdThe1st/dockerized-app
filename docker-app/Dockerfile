# 1) Builder stage
FROM python:3.12-slim AS builder

# Make pip behave nicely in CI/builds
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install deps into a "wheelhouse" (prebuilt wheels)
COPY requirements.txt .
RUN pip wheel --wheel-dir /wheels -r requirements.txt


# 2) Runtime stage (small + clean)
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-root user
# (Debian slim has adduser/addgroup)
RUN addgroup --system app && adduser --system --ingroup app app

# Install dependencies from wheels built in the builder stage
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels

# Copy your application code
COPY app ./app

# Make sure the non-root user can read the app
RUN chown -R app:app /app

USER app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
