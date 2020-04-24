from TechTeam.adapter.admin_support import AdminSupportAdapter
from TechTeam.adapter.department import DepartmentAdapter
from TechTeam.adapter.department_country_support import DepartmentCountrySupportAdapter
from TechTeam.adapter.department_involved import DepartmentInvolvedAdapter
from TechTeam.adapter.employee_in_charge import EmployeeInChargeAdapter
from TechTeam.adapter.support_department import SupportDepartmentAdapter
from TechTeam.adapter.problem_type import ProblemTypeAdapter
from TechTeam.adapter.request import RequestAdapter
from TechTeam.adapter.request_update import RequestUpdateAdapter
from TechTeam.adapter.user import UserAdapter

department = {
    "department": "prueba5"
}

user = {
    "first_name": "xxx",
    "last_name": "xxx",
    "phone": "123",
    "email": "xxx@gmail.com",
    "employee_serial": "1234"
}

admin_support = {
    "first_name": "aa",
    "last_name": "aa",
    "phone": "45",
    "email": "ty@gmail.com",
    "employee_serial": "22",
    "id_support_department": "90"
}

department_involved = {
    "id_department_support": "1",
    "id_request": "10"
}

department_country_support = {
    "id_department": "7",
    "country": "USA"
}

employee_in_charge = {
    "id_department": "2",
    "first_name": "Javier",
    "last_name": "Sotooo",
    "phone": "3453",
    "email": "caoto@gmail.com",
    "employee_serial": "45",
}

problem_type = {
    "name": "aa",
    "description": "aaaa"
}

request = {
    "id_problem_type": "1",
    "description": "blablabla",
    "user_id_creation": "1",
    "priority": "High",
    "country": "mexico",
}

request_update = {
    "id_department_support": "1",
    "description": "blablabla",
    "status": "In process"
}

support_department = {
    "id_department": "8",
    "name": "Prueba",
    "email": "bad",
}

functions = ProblemTypeAdapter()
print(functions.update('4',problem_type))
