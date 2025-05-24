from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks.json once when the app starts
with open(os.path.join(os.path.dirname(__file__), "..", "marks.json"), "r") as f:
    marks_data = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = []):
    result = [marks_data.get(n, None) for n in name]
    return JSONResponse(content={"marks": result})
