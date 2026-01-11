ARG PLATFORM=linux/amd64
FROM --platform=${PLATFORM} python:3.14-slim

# =================================================
# Install System Dependencies, Chrome, Firefox & Cleanup
# =================================================
RUN apt-get update && apt-get install -y --no-install-recommends \
        wget gnupg curl unzip ca-certificates \
    && update-ca-certificates \
    \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    \
    && apt-get update && apt-get install -y --no-install-recommends \
        google-chrome-stable \
        firefox-esr \
    \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

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