import os
import uvicorn
from fastapi import Request, FastAPI, Response

app = FastAPI(title = "S2DR3")

AIP_HEALTH_ROUTE = os.environ.get("AIP_HEALTH_ROUTE", "/health")
AIP_PREDICT_ROUTE = os.environ.get("AIP_PREDICT_ROUTE", "/predict")

@app.get(AIP_HEALTH_ROUTE, status_code = 200)
async def health():
    return {"health": "ok"}

@app.post(AIP_PREDICT_ROUTE)
async def predict(request: Request):
    body = await request.json()
    print(body)

    instances = body["instances"]
    print(instances)

    return instances

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port = 8080)