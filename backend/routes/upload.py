from fastapi import APIRouter, UploadFile, File
import uuid
import os

router = APIRouter()

UPLOAD_DIR = "data/audio"

@router.post("/upload-meeting")
async def upload_meeting(file: UploadFile = File(...)):
    
    meeting_id = str(uuid.uuid4())
    
    file_path = f"{UPLOAD_DIR}/{meeting_id}.m4a"
    
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    return {
        "meeting_id": meeting_id,
        "filename": file.filename,
        "status": "uploaded"
    }