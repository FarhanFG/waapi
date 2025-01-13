from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/fetch-total-count")
def fetch_total_count():
    try:
        # Perform the GET request to the target URL
        url = "http://13.126.242.31:8000/total-count"
        headers = {"accept": "application/json"}
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        return {"status": "success", "data": response.json()}
    except requests.RequestException as e:
        return {"status": "error", "message": str(e)}
