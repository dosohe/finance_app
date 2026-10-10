from fastapi import FastAPI

app = FastAPI(title="Finance App")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
