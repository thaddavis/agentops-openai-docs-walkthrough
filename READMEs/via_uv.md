# TLDR

Notes related to integrating AgentOps with the official OpenAI Python SDK

## Reference links

https://docs.astral.sh/uv/getting-started/installation/#pypi

## Steps

```sh
python3 -m venv .venv
source .venv/bin/activate
python --version
pip install uv
```

```sh
uv init
uv add openai python-dotenv agentops packaging
uv sync
uv run examples/1.sync_completion.py
```
