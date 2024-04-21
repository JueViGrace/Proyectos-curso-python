'''Main application'''

from fastapi import FastAPI
from src.app.routes import app_router

app = FastAPI()

app.include_router(app_router, prefix='/api', tags=['api'])

@app.get('/health', tags=['health'])
def health():
    '''Health endpoint'''
    return {
        'message': 'Health is ok!'
    }
