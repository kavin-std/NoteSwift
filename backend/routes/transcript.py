from fastapi import APIRouter
import os
from services.whisper_service import transcribe_audio

router = APIRouter()

AUDIO_DIR = "data/audio"
TRANSCRIPT_DIR = "data/transcripts"


@router.post("/transcribe/{meeting_id}")
def transcribe(meeting_id: str):

    audio_path = f"{AUDIO_DIR}/{meeting_id}.m4a"

    transcript = transcribe_audio(audio_path)

    transcript_path = f"{TRANSCRIPT_DIR}/{meeting_id}.txt"

    with open(transcript_path, "w") as f:
        f.write(transcript)

    return {
        "meeting_id": meeting_id,
        "transcript": transcript
    }