from TechTeam.adapter.admin_support import AdminSupportAdapter
from TechTeam.adapter.department_country_support import DepartmentCountrySupportAdapter

department = {
    "department": "prueba5"
}

user = {
    "first_name": "Caro",
    "last_name": "Soto",
    "phone": "1234567890",
    "email": "carosoto@gmail.com",
    "employee_serial": "69"
}

admin_support = {
    "first_name": "xxxx",
    "last_name": "xxxx",
    "phone": "344",
    "email": "xxxxx@gmail.com",
    "employee_serial": "33",
    "id_support_department": "3"
}

department_involved = {
    # "id_department_support": "1",
    # "id_request": "3"
}

department_country_support = {
    "id_department": "7",
    "country": "USA"
}

employee_in_charge = {
    # "id_department": "1",
    "first_name": "Javier",
    "last_name": "Sotooo",
    "phone": "3453",
    "email": "caoto@gmail.com",
    "employee_serial": "45",
}

problem_type = {
    "name": "Config",
    "Description": "balbalblablalbla"
}

request = {
    # "id_problem_type": "1",
    "description": "blablabla",
    "creation_date": "",
    "update_date": "",
    "date_closed_ticket": "",
    "status": "good",
    "solution": "blablabla",
    "priority": "urge",
    "country": "mexico",
}

request_update = {
    # "id_problem_type": "1",
    "description": "blablabla",
    "status": "good",
    "date": "",
}

support_department = {
    # "id_department": "1",
    "name": "blablabla",
    "email": "good",
}

functions = DepartmentCountrySupportAdapter()
print(functions.update(4, department_country_support))
