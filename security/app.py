from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

# Add middleware for session handling
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

@app.post("/store/{value}")
async def store_value(request: Request, value: str):
    # Store the value in the session
    session = request.session
    session["value"] = value
    return {"detail": "Value stored in session"}

@app.get("/read")
async def read_value(request: Request):
    # Read the value from the session
    session = request.session
    value = session.get("value", "No value stored")
    return {"stored_value": value}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)