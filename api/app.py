from fastapi import FastAPI

app=FastAPI(title="inc add")

app.include_router()