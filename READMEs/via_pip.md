# TLDR 

Notes related to integrating AgentOps with the official OpenAI Python SDK

## Reference links

- https://pypi.org/project/openai/
- https://pypi.org/project/python-dotenv/
- https://pypi.org/project/agentops/
- https://docs.agentops.ai/v1/integrations/openai
- https://app.agentops.ai/settings/projects

## Steps

- python3 --version
```sh
python3 -m venv venv
source venv/bin/activate
python --version
touch requirements.txt
echo "openai>=1.57.0,<2.0.0" > requirements.txt
echo "\npython-dotenv>=1.0.1,<2.0.0" >> requirements.txt
echo "\nagentops>=0.3.21,<0.4.0" >> requirements.txt
pip install -r requirements.txt
```

##

```sh
deactivate
```