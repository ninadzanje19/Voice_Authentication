from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from feature_extraction import *
from fastapi.responses import HTMLResponse

app = FastAPI()

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
async def metadata(params: metadata):
    audio_data = extract_mfcc(params.audio)
    return audio, audio_data
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