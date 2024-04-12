# Chatbot with LLM

## Test Model

```bash
brew install llm
llm install llm-gpt4all
llm -m llama-2-7b-chat "What is Large Language Model?"
```

## Vector Dabatabse

```bash
docker pull epsilla/vectordb
docker run -d -p 8888:8888 epsilla/vectordb

docker pull chromadb/chroma
docker run --pull=always -d -p 8000:8000 chromadb/chroma
```

## SQL Dabatabse

```bash
docker run --name some-postgres -e POSTGRES_DB=pruebas -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -p 5432:5432 -d postgres
```

## Run

```python
python learn.py

python documents.py

streamlit run database.py
```  

## Examples DB

Cuantas tareas hay?
Cuantas tareas estan completas?
Me puedes listar todas las tareas?
Me puedes listar todas las tareas completas?

Cuantas tareas han sido completadas?
Quienes han completado mas tareas y cuantas fueron?
Cuantas tareas hay pendientes por completar?
Que area ha completado mas tareas?
Que area ha completado menos tareas?

## Example Documents  

