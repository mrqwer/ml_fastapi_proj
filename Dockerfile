# Build multi_stage
FROM python:3.10 AS builder

WORKDIR /src

COPY ./requirements.txt .

# Install build dependencies and cleanup
RUN set -ex && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --prefix=/install -r ./requirements.txt

# Production stage
FROM python:3.10-slim

WORKDIR /src
# Install libmagic package and other required system packages
RUN echo "deb http://deb.debian.org/debian bookworm main" > /etc/apt/sources.list && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends libmagic1 && \
    apt-get install libmagic-dev && \
    apt-get clean && \
    rm -rf /var/cache/apt/*


# Copy only the necessary files from the builder stage, including updated requirements
COPY --from=builder /install /usr/local
COPY ./src .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
