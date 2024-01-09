import os
import json
import uvicorn
from fastapi import Request, FastAPI, Response
from google.cloud import storage

app = FastAPI(title = "S2DR3")

AIP_HEALTH_ROUTE = os.environ.get("AIP_HEALTH_ROUTE", "/health")
AIP_PREDICT_ROUTE = os.environ.get("AIP_PREDICT_ROUTE", "/predict")

def upload_to_bucket(blob_name, path_to_file, bucket_name):
    storage_client = storage.Client.from_service_account_json(
        'credentials.json'
    )
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)

    return blob.public_url

def write_content_to_file(file_name, str_content):
    with open(file_name, "w") as file:
        file.write(str_content)

@app.get(AIP_HEALTH_ROUTE, status_code = 200)
async def health():
    return {
        "response" : "ok"
    }

@app.post(AIP_PREDICT_ROUTE)
async def predict(request: Request):
    body = await request.json()
    write_content_to_file("data.txt", json.dumps(body))
    uploaded_url = upload_to_bucket("output/data.txt", "data.txt", "s2dr3-202312")
    return uploaded_url
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port = 8080)