ARG PLATFORM=linux/amd64
FROM --platform=${PLATFORM} python:3.14-slim

# =================================================
# Install System Dependencies & Cleanup
# =================================================
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget gnupg curl unzip ca-certificates \
    libnss3 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libgbm1 \
    libasound2 \
    && update-ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# =================================================
# Python Dependencies (Fixed Paths)
# =================================================
COPY requirements-base.txt .
COPY api_tests/requirements.txt ./api_tests/requirements.txt
COPY gui_tests/requirements.txt ./gui_tests/requirements.txt
COPY unit_tests/requirements.txt ./unit_tests/requirements.txt

RUN pip install --no-cache-dir \
    -r requirements-base.txt \
    -r api_tests/requirements.txt \
    -r gui_tests/requirements.txt \
    -r unit_tests/requirements.txt

# Final Copy
COPY . .

CMD ["pytest"]