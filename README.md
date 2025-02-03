```bash
conda create -n name
conda activate name
conda install -c conda-forge poetry
conda env export --from-history > environment.yml
```

## Create environment from file

```bash
conda env create -f environment.ym
```

## After of this, don´t forget choose your execution environment

```bash
poetry init
poetry add langgraph
poetry add python-dotenv
```

# Debug de sistema de agentes

```bash
poetry add "langgraph-cli[inmem]"
```

# Now run the command to open in dashboard and install fast api to expose the service in a endpoint

```bash
langgraph dev
poetry add "fastapi[standard]"
fastapi dev app/api.py
```

# Join langgraph as a orchestrator system and langchain as al comunication with LLMs

```bash
poetry add langchain-openai
```
