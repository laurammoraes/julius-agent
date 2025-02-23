

from fastapi import FastAPI

from agent import makeAction

app = FastAPI()

@app.post("/agent/action")
async def read_item(action: str ):
    response = await makeAction(action)
    return {"response": response}