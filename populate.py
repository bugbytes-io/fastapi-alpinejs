from database import engine
from models import Department, Employee
from sqlmodel import Session, select

def populate():
    with Session(engine) as session:
        departments = [
            {'id': 1, 'name': 'Accounts'},
            {'id': 2, 'name': 'Sales'},
            {'id': 3, 'name': 'Management'}
        ]
        
        for department in departments:
            session.add(Department(**department))
        
        session.commit()
        
        sales = session.exec(
            select(Department).where(Department.name == 'Sales')
        ).first()

        accounts = session.exec(
            select(Department).where(Department.name == 'Accounts')
        ).first()

        management = session.exec(
            select(Department).where(Department.name == 'Management')
        ).first()

        # add employees
        employees = [
            {
                'id': 1, 
                'first_name': 'Jim', 
                'surname': 'Halpert', 
                'job_title': 'Sales Executive', 
                'department_id': sales.id
            },
            {
                'id': 2, 
                'first_name': 'Todd', 
                'surname': 'Packer', 
                'job_title': 'Sales Executive', 
                'department_id': sales.id    
            },
            {
                'id': 3, 
                'first_name': 'Phyllis', 
                'surname': 'Vance', 
                'job_title': 'Regional Director of Sales', 
                'department_id': sales.id
            },
            {
                'id': 4, 
                'first_name': 'Angela', 
                'surname': 'Martin', 
                'job_title': 'Head of Accounting', 
                'department_id': accounts.id
            },
            {
                'id': 5, 
                'first_name': 'Oscar', 
                'surname': 'Martinez', 
                'job_title': 'Accountant', 
                'department_id': accounts.id
            },
            {
                'id': 6, 
                'first_name': 'Dwight', 
                'surname': 'Schrute', 
                'job_title': 'Assistant to the Regional Manager', 
                'department_id': management.id
            },
            {
                'id': 7, 
                'first_name': 'Michael', 
                'surname': 'Scott', 
                'job_title': 'Regional Manager', 
                'department_id': management.id
            },
            {
                'id': 8, 
                'first_name': 'Kevin', 
                'surname': 'Malone', 
                'job_title': 'Accountant', 
                'department_id': accounts.id
            },
        ]

        for employee in employees:
            session.add(Employee(**employee))
            session.commit()

if __name__ == '__main__':
    # creates the table if this file is run independently, as a script
    populate()