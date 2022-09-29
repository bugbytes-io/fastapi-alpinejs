import json
from typing import List 
import uvicorn
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import select, Session

from database import get_session, engine
from models import Employee, Department

app = FastAPI()

templates = Jinja2Templates(directory="templates")

from fastapi.encoders import jsonable_encoder
import json

@app.get("/home/", response_class=HTMLResponse)
async def home(request: Request, session: Session = Depends(get_session)):
    stmt = select(Employee, Department).where(Employee.department_id == Department.id)
    results = session.exec(stmt).all()
    employee_data = jsonable_encoder(results)
    print(employee_data)
    departments = set([e['Department']['name'] for e in employee_data])
    context = {
        'request': request,
        'results': json.dumps(employee_data),
        'departments': departments
    }
    return templates.TemplateResponse("employees.html", context)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)