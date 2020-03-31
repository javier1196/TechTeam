from TechTeam.msql.MsqlConnection import MsqlConnection

"""
Esta clase no jala por las llaves foraneas
"""


class EmployeeInChargeAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM employee_in_charge"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_employee_in_charge = {
                "id_department": record[0],
                "first_name": record[1],
                "last_name": record[2],
                "phone": record[3],
                "email": record[4],
                "employee_serial": record[5],
            }
            records_to_return.append(each_employee_in_charge)
        return records_to_return

    def new(self, employee_in_charge_dict):
        connection = MsqlConnection()
        sentence = "INSERT employee_in_charge(id_department, first_name, last_name_ phone_ email_ employee_serial) " \
                   "VALUES('" + employee_in_charge_dict["id_department"] + "','" + employee_in_charge_dict[
                       "first_name"] + "','" + employee_in_charge_dict["last_name"] + "','" + employee_in_charge_dict[
                       "phone"] + \
                   "','" + employee_in_charge_dict["email"] + "','" + employee_in_charge_dict["employee_serial"] + "') "
        connection.execute(sentence)
        connection.commit()
        connection.close_connection()
        return "employee_in_charge was created correctly"""

    def delete(self, id):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM employee_in_charge WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "DELETE FROM employee_in_charge WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "employee_in_charge was deleted"
        return "This employee_in_charge does not exist"

    def update(self, id, employee_in_charge_dict):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM employee_in_charge WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "UPDATE employee_in_charge set id_department = '" + employee_in_charge_dict[
                "id_department"] + "',  first_name = '" + employee_in_charge_dict["last_name"] + "',  phone = '" + \
                       employee_in_charge_dict["phone"] + "',  email = '" + employee_in_charge_dict[
                           "email"] + "',  employee_serial = '" + employee_in_charge_dict[
                           "employee_serial"] + "' WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()

            connection.close_connection()
            return "employee_in_charge was updated"
        return "This employee_in_charge does not exist"
