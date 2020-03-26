from msql.MsqlConnection import MsqlConnection

"""
las llaves foraneas no jalan
"""

class DepartmentCountrySupportAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM department_country_support"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_department_involved = {
                "id_department": record[0],
                "country": record[1],
            }
            records_to_return.append(each_department_involved)
        return records_to_return

    def new(self, department_country_support_dict):
        connection = MsqlConnection()
        # sentence = "INSERT department_country_support(id_department, country) VALUES('" + department_country_support_dict["id_department"] + "','" + department_country_support_dict["country"] + "') "
        sentence = "INSERT department_country_support(id_department) VALUES('" + department_country_support_dict["id_department"] + "') "
        connection.execute(sentence)
        connection.commit()
        connection.close_connection()
        return "departments_involved was created correctly"""

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
            # sentence = "UPDATE department_country_support set id_department = '" + department_country_support_dict["id_department"] + "',  country = '" + department_country_support_dict["country"] + "' WHERE ID = '" + str(id) + "'"
            sentence = "UPDATE department_country_support set id_department = '" + department_country_support_dict["id_department"] + "' WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()

            connection.close_connection()
            return "department_country_support was updated"
        return "This department_country_support does not exist"
