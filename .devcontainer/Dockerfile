FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        clang-19 clang-format-19 \
    && rm -rf /var/lib/apt/lists/*
