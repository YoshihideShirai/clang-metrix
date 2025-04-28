FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        clang-19 clang-format-19 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "cli.py"]