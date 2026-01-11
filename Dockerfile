FROM --platform=linux/amd64 python:3.14-slim

# =================================================
# Install System Dependencies (minimal)
# =================================================
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    unzip \
    ca-certificates \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# =================================================
# Google Chrome (latest stable)
# =================================================
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Verify Chrome
RUN google-chrome --version

# =================================================
# ChromeDriver (auto-matched to Chrome version)
# =================================================
RUN CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d '.' -f 1) \
    && CHROMEDRIVER_VERSION=$(curl -s "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_${CHROME_VERSION}") \
    && wget -q "https://storage.googleapis.com/chrome-for-testing-public/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip" \
    && unzip chromedriver-linux64.zip \
    && mv chromedriver-linux64/chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver \
    && rm -rf chromedriver-linux64.zip chromedriver-linux64

RUN chromedriver --version

# =================================================
# Firefox ESR (latest stable)
# =================================================
RUN apt-get update \
    && apt-get install -y firefox-esr \
    && rm -rf /var/lib/apt/lists/*

RUN firefox-esr --version

# =================================================
# GeckoDriver (latest stable)
# =================================================
RUN GECKODRIVER_VERSION=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep 'tag_name' | cut -d '"' -f 4) \
    && wget -q "https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VERSION}/geckodriver-${GECKODRIVER_VERSION}-linux64.tar.gz" \
    && tar -xzf "geckodriver-${GECKODRIVER_VERSION}-linux64.tar.gz" \
    && mv geckodriver /usr/local/bin/geckodriver \
    && chmod +x /usr/local/bin/geckodriver \
    && rm "geckodriver-${GECKODRIVER_VERSION}-linux64.tar.gz"

RUN geckodriver --version

# =================================================
# Python Dependencies
# =================================================
WORKDIR /app

COPY requirements-base.txt .
COPY api_tests/requirements.txt ./api_tests/
COPY gui_tests/requirements.txt ./gui_tests/
COPY unit_tests/requirements.txt ./unit_tests/

RUN pip install --no-cache-dir \
    -r requirements-base.txt \
    -r api_tests/requirements.txt \
    -r gui_tests/requirements.txt \
    -r unit_tests/requirements.txt

# =================================================
# Copy Application Code
# =================================================
COPY . .

# =================================================
# Default Command
# =================================================
CMD ["pytest", "-v"]