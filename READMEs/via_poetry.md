# TLDR 

Notes related to integrating AgentOps with the official OpenAI Python SDK

## Reference links

- https://python-poetry.org/docs/#installing-manually
- https://python-poetry.org/docs/basic-usage/

## Steps

```sh
python3 -m venv venv
source venv/bin/activate
python --version
pip install -U pip setuptools
pip install poetry
```

```sh
poetry add openai
poetry run python examples/poetry/1.py
poetry run python examples/poetry/2.py
poetry run python examples/poetry/3.py
```