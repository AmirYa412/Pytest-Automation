FROM --platform=linux/amd64 python:3.14-slim

# =================================================
# Install System Dependencies & Chrome in ONE layer
# =================================================
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget gnupg curl unzip ca-certificates firefox-esr \
    libnss3 libgbm1 libasound2 \
    && update-ca-certificates \
    # Install Google Chrome
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    # Cleanup to drop image size
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# =================================================
# Drivers (Matched to Chrome)
# =================================================
RUN CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d '.' -f 1) \
    && CHROMEDRIVER_VERSION=$(curl -s "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_${CHROME_VERSION}") \
    && wget -q "https://storage.googleapis.com/chrome-for-testing-public/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip" \
    && unzip chromedriver-linux64.zip && mv chromedriver-linux64/chromedriver /usr/local/bin/ && chmod +x /usr/local/bin/chromedriver \
    && rm -rf chromedriver-linux64.zip

# =================================================
# GeckoDriver (Firefox)
# =================================================
RUN GECK_VER=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep 'tag_name' | cut -d '"' -f 4) \
    && wget -q "https://github.com/mozilla/geckodriver/releases/download/${GECK_VER}/geckodriver-${GECK_VER}-linux64.tar.gz" \
    && tar -xzf "geckodriver-${GECK_VER}-linux64.tar.gz" -C /usr/local/bin \
    && rm "geckodriver-${GECK_VER}-linux64.tar.gz"

WORKDIR /app

# =================================================
# Python Dependencies (Fixed Paths)
# =================================================
# Copy requirements into their respective subdirectories to avoid overwriting
COPY requirements-base.txt .
COPY api_tests/requirements.txt ./api_tests/requirements.txt
COPY gui_tests/requirements.txt ./gui_tests/requirements.txt
COPY unit_tests/requirements.txt ./unit_tests/requirements.txt

# Install all of them. Using --no-cache-dir saves hundreds of MBs.
RUN pip install --no-cache-dir \
    -r requirements-base.txt \
    -r api_tests/requirements.txt \
    -r gui_tests/requirements.txt \
    -r unit_tests/requirements.txt

# Final Copy
COPY . .

CMD ["pytest"]