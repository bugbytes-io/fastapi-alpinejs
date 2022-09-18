from typing import List 
import uvicorn
from fastapi import FastAPI

from models import Employee, Department

app = FastAPI()


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)