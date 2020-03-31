from TechTeam.msql.MsqlConnection import MsqlConnection

"""
Esta clase no jala por las llaves foraneas
"""

class DepartmentInvolvedAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM departments_involved"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_department_involved = {
                "id_department_support": record[0],
                "id_request": record[1],
            }
            records_to_return.append(each_department_involved)
        return records_to_return

    def new(self, department_involved_dict):
        connection = MsqlConnection()
        sentence = "INSERT departments_involved(id_department_support, id_request) VALUES('" + department_involved_dict["id_department_support"] + "','" + department_involved_dict["id_request"] + "') "
        connection.execute(sentence)
        connection.commit()
        connection.close_connection()
        return "departments_involved was created correctly"""

    def delete(self, id):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM departments_involved WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "DELETE FROM departments_involved WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "departments_involved was deleted"
        return "This departments_involved does not exist"

    def update(self, id, department_involved_dict):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM departments_involved WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "UPDATE departments_involved set id_department_support = '" + department_involved_dict["id_department_support"] + "',  id_request = '" + department_involved_dict["id_request"] + "' WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()

            connection.close_connection()
            return "departments_involved was updated"
        return "This departments_involved does not exist"
