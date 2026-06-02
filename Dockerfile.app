# Base image
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim


RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

COPY src/ src/
COPY tests/ tests/
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
COPY README.md README.md

WORKDIR /

RUN uv sync --locked --no-cache --no-install-project

RUN uv run pytest tests/


ENTRYPOINT ["uv", "run", "streamlit", "run", "src/ikano_case/app.py", "--server.address=0.0.0.0", "--server.port=8501"]
