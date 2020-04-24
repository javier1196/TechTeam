from TechTeam.msql.MsqlConnection import MsqlConnection


class DepartmentAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM department"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_department = {
                "id": record[0],
                "department": record[1]
            }
            records_to_return.append(each_department)
        return records_to_return

    def new(self, department_dict):
        connection = MsqlConnection()
        sentence = "INSERT department(department) VALUES('" + department_dict["department"] + "')"
        connection.execute(sentence)
        connection.commit()
        connection.close_connection()
        return "Department was created correctly"""

    def delete(self, id):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM department WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "DELETE FROM department WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "Department was deleted"
        return "This department does not exist"

    def update(self, id, department_dict):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM department WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "UPDATE department set department = '" + department_dict["department"] + "' WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()

            connection.close_connection()
            return "Department was updated"
        return "This department does not exist"
