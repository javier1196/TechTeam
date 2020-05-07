from TechTeam.msql.MsqlConnection import MsqlConnection


class DepartmentCountrySupportAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM department_country_support"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_department_involved = {
                "id": record[0],
                "id_department": record[1],
                "country": record[2],
            }
            records_to_return.append(each_department_involved)
        return records_to_return

    def new(self, department_country_support_dict):
        connection = MsqlConnection()
        sentence_search = "SELECT * FROM department WHERE id ='" + department_country_support_dict["id_department"] + "'"
        row = connection.get_all(sentence_search)
        if row:
            sentence = "INSERT department_country_support(id_department, country) VALUES('" + department_country_support_dict["id_department"] + "','" + department_country_support_dict["country"] + "') "
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "departments_involved was created correctly"
        else:
            connection.close_connection()
            return "This department was incorrectly"

    def delete(self, id):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM department_country_support WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "DELETE FROM department_country_support WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "department_country_support was deleted"
        return "This department_country_support does not exist"

    def update(self, id, department_country_support_dict):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM department_country_support WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence_valid_department = "SELECT * FROM department WHERE id ='" + department_country_support_dict["id_department"] + "'"
            row_valid = connection.get_all(sentence_valid_department)
            if row_valid:
                sentence = "UPDATE department_country_support set id_department = '" + department_country_support_dict["id_department"] + "',  country = '" + department_country_support_dict["country"] + "' WHERE ID = '" + str(id) + "'"
                connection.execute(sentence)
                connection.commit()

                connection.close_connection()
                return "department_country_support was updated"
            else:
                return "This department id does not exist"
        else:
            return "This department_country_support does not exist"
