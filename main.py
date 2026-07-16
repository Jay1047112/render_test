from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI(title="FastAPI")


@app.get("/", summary="Read Root")
def read_root() -> RedirectResponse:
    return RedirectResponse(url="/docs", status_code=307)


@app.get("/hello", summary="Read Hello")
def read_hello() -> dict[str, str]:
    return {"message": "Hello"}


@app.get("/api", summary="Read Api")
def read_api() -> dict[str, str]:
    return {
        "name": "fastapi-render-hello",
        "docs": "/docs",
        "openapi": "/openapi.json",
    }
