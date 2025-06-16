
FROM ubuntu:24.04

ARG SYFT_VERSION=0.108.0
ARG ORT_VERSION=10.0.0
ARG SCANCODE_VERSION=33.0.3
ARG SCANOSS_CLI_VERSION=4.0.0
ARG MSBOM_VERSION=1.0.8

# Install basics
RUN apt-get update && apt-get install -y curl python3 python3-pip openjdk-17-jdk git docker.io && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt /opt/scanforge/
RUN pip3 install --no-cache-dir -r /opt/scanforge/requirements.txt

# Install Syft
RUN curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin v${SYFT_VERSION}

# Install ScanOSS CLI
RUN pip3 install scanoss-cli==${SCANOSS_CLI_VERSION}

# Download ORT CLI
RUN curl -L https://github.com/oss-review-toolkit/ort/releases/download/v${ORT_VERSION}/ort-${ORT_VERSION}.jar -o /usr/local/bin/ort.jar

# Download Microsoft SBOM tool
RUN curl -L https://github.com/microsoft/sbom-tool/releases/download/v${MSBOM_VERSION}/sbom-tool-linux-x64 -o /usr/local/bin/sbom-tool && chmod +x /usr/local/bin/sbom-tool

# Copy app
COPY . /opt/scanforge
WORKDIR /opt/scanforge

ENTRYPOINT ["python3", "main.py"]
