from TechTeam.msql.MsqlConnection import MsqlConnection

"""
Esta clase no jala por las llaves foraneas
"""


class SupportDepartmentAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM support_department"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_support_department = {
                "id_department": record[0],
                "name": record[1],
                "email": record[2],
            }
            records_to_return.append(each_support_department)
        return records_to_return

    def new(self, support_department_dict):
        connection = MsqlConnection()
        sentence = "INSERT support_department(id_department, name, " \
                   "email) VALUES('" + support_department_dict["id_department"] + "','" + \
                   support_department_dict["name"] + "','" + support_department_dict["email"] + "') "
        connection.execute(sentence)
        connection.commit()
        connection.close_connection()
        return "support_department was created correctly"""

    def delete(self, id):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM support_department WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "DELETE FROM support_department WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "support_department was deleted"
        return "This support_department does not exist"

    def update(self, id, support_department_dict):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM support_department WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "UPDATE support_department set id_problem_type = '" + support_department_dict[
                "id_department"] + "',  name = '" + support_department_dict["name"] + "',  email = '" + \
                       support_department_dict["email"] + "' WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()

            connection.close_connection()
            return "support_department was updated"
        return "This support_department does not exist"
