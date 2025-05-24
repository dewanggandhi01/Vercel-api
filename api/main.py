from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["GET"],  # Only allow GET requests
    allow_headers=["*"],
)

current_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(current_dir, 'q-vercel-python.json')) as f:
    students_data = json.load(f)

@app.get("/api")
async def get_marks(name: List[str] = Query(None)):
    if not name:
        return {"error": "Please provide at least one name"}
    
    marks = []
    for student_name in name:
        mark = next((student["marks"] for student in students_data 
                     if student["name"].lower() == student_name.lower()), None)
        marks.append(mark)
    
    return {"marks": marks}

@app.get("/")
async def root():
    return {"message": "Student Marks API. Use /api?name=X&name=Y to get marks."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("index:app", host="0.0.0.0", port=8000, reload=True)
