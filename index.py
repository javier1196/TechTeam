from adapter.department import DepartmentAdapter
from adapter.user import UserAdapter
from adapter.admin_support import AdminSupportAdapter
from adapter.department_involved import DepartmentInvolvedAdapter
from adapter.department_country_support import DepartmentCountrySupportAdapter
from adapter.employee_in_charge import EmployeeInChargeAdapter
from adapter.problem_type import ProblemTypeAdapter
from adapter.request import RequestAdapter
from adapter.request_update import RequestUpdateAdapter
from adapter.support_department import SupportDepartmentAdapter

department = {
    "department": "prueba4"
}

user = {
    "first_name": "Caro",
    "last_name": "Soto",
    "phone": "1234567890",
    "email": "carosoto@gmail.com",
    "employee_serial": "69"
}

admin_support = {
    "first_name": "Javier",
    "last_name": "Sotooo",
    "phone": "3453",
    "email": "caoto@gmail.com",
    "employee_serial": "45",
    "id_support_department": "3"
}

department_involved = {
    # "id_department_support": "1",
    # "id_request": "3"
}

department_country_support = {
    # "id_department": "1",
    "country": "mexico"
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

functions = DepartmentAdapter()
functions2 = UserAdapter()
functions3 = AdminSupportAdapter()
functions4 = DepartmentInvolvedAdapter()
functions5 = DepartmentCountrySupportAdapter()
functions6 = EmployeeInChargeAdapter()
functions7 = ProblemTypeAdapter()
functions8 = RequestAdapter()
functions9 = RequestUpdateAdapter
functions10 = SupportDepartmentAdapter

# print(functions.new(department))
# print(functions2.update(1, user))
# print(functions3.update(1, admin_support))
# print(functions4.new(department_involved))
# print(functions5.new(department_country_support))