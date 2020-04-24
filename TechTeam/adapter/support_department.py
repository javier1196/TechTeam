from TechTeam.msql.MsqlConnection import MsqlConnection


class SupportDepartmentAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM support_department"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_support_department = {
                "id": record[0],
                "id_department": record[1],
                "name": record[2],
                "email": record[3]
            }
            records_to_return.append(each_support_department)
        return records_to_return

    def new(self, support_department_dict):
        connection = MsqlConnection()
        sentence_search = "SELECT * FROM department WHERE id='" \
                          + support_department_dict["id_department"] + "'"
        row = connection.get_all(sentence_search)
        if row:
            sentence = "INSERT support_department(id_department, name, " \
                       "email) VALUES('" + support_department_dict["id_department"] + "','" + \
                       support_department_dict["name"] + "','" + support_department_dict["email"] + "') "
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "This support department was created succesfully"
        else:
            connection.close_connection()
            return "This support department does not exist"

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
        sentence_search = "SELECT * FROM support_department WHERE id='" + str(id) + "'"
        row = connection.get_all(sentence_search)
        if row:
            sentence_search_department = "SELECT * FROM department WHERE id='" \
                                         + support_department_dict["id_department"] + "'"
            row_search = connection.get_all(sentence_search_department)
            if row_search:
                sentence = "UPDATE support_department set id_department = '" + support_department_dict[
                    "id_department"] + "',  name = '" + support_department_dict["name"] + "',  email = '"\
                           + support_department_dict["email"] + "' WHERE ID = '" + str(id) + "'"
                connection.execute(sentence)
                connection.commit()
                connection.close_connection()
                return "departments_involved was updated"
            else:
                connection.close_connection()
                return "This id department does not exist"
        else:
            connection.close_connection()
            return "This request does not exist"
