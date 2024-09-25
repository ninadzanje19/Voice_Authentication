from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse
import os
from fastapi.middleware.cors import CORSMiddleware
from audio_preprocessing import preprocess_audio
from feature_extraction import *
from fastapi.responses import HTMLResponse

UPLOAD_DIRECTORY = r"G:\Projects\Voice_Authentication\Voice_Authentication\data\audio_data"
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class audios(BaseModel):
    audio1: str
    audio2: str

class metadata(BaseModel):
    metadata: str
    audio: str
@app.get("/")
async def home():
    voice1 = r"G:\Projects\Voice_Authentication\Voice_Authentication\data\data\process\audio1.wav"
    voice2 = r"G:\Projects\Voice_Authentication\Voice_Authentication\data\data\process\audio2.wav"
    result = similarity_percentage(voice1, voice2)
    return result

@app.post("/metadata")
async def metadata(
    name: str = Form(...),
    audio: UploadFile = File(...)
):
    # Save the uploaded file
    file_location = f"{UPLOAD_DIRECTORY}/{audio.filename}"
    with open(file_location, "wb") as file_object:
        file_object.write(await audio.read())

    processed_audio = preprocess_audio(file_location, process_audio_dir)
    audio_mfcc = extract_mfcc(processed_audio)
    audio_mfcc = list(audio_mfcc)
    return {
        "metadata": name,
        "mfcc_data": audio_mfcc,
        "location": processed_audio
    }
@app.post("/")
async def home2(params: audios):
    voice1 = fr"G:\Projects\Voice_Authentication\Voice_Authentication\data\process_audio\{params.audio1}.wav"
    voice2 = fr"G:\Projects\Voice_Authentication\Voice_Authentication\data\process_audio\{params.audio2}.wav"
    result = similarity_percentage(voice1, voice2)
    return result

@app.get("/form")
async def html():
    with open("index.html", "r") as f:
        content = f.read()
        return HTMLResponse(content = content)