# Builder stage
FROM python:3.12-slim as builder
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y gcc libssl-dev

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.12-slim
WORKDIR /app

# Copy virtual environment
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application
COPY . .

# Set entrypoint
ENTRYPOINT ["python", "-m", "src.cli"]
