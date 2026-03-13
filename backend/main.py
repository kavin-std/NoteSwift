from fastapi import FastAPI
from routes import upload, transcript

app = FastAPI(title="NoteSwift Backend")

app.include_router(upload.router)
app.include_router(transcript.router)

@app.get("/")
def home():
    return {"message": "NoteSwift backend running"}