from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from uvicorn import run
import os


from Natural_Language_Understanding import NLU

app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)

@app.get('/')
def index():
    return ('Welcome to A Smart Assistant')

@app.post('/predict')
def predict(message):

    res = NLU(message)

    return res
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    run(app, host="0.0.0.0", port=port)