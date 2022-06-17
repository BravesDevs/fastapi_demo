from typing import Optional
from datetime import date as date_type
from fastapi import FastAPI, File, UploadFile, Datetime
from utils.utils import convertBytesToString, parsed_csv


app = FastAPI()


@app.get('/')
def getName():
    return {'ok': True, 'content': "Hello World"}


@app.post('/csv/')
async def parse_csv(file: UploadFile = File(...)):
    contents = await file.read()
    json_string = convertBytesToString(contents)
    return {
        'ok': True,
        'content': json_string
    }


# @app.post('/calculate_age/')
# def calculateAge(date:date_type):
