from TechTeam.msql.MsqlConnection import MsqlConnection


class AdminSupportAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM admin_support"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_admin_support = {
                "id": record[0],
                "first_name": record[1],
                "last_name": record[2],
                "phone": record[3],
                "email": record[4],
                "employee_serial": record[5],
                "id_support_department": record[6],
            }
            records_to_return.append(each_admin_support)
        return records_to_return

    def new(self, admin_dict):
        connection = MsqlConnection()
        sentence_search = "SELECT * FROM support_department WHERE id='" + admin_dict["id_support_department"] + "'"
        row = connection.get_all(sentence_search)
        if row:
            sentence = "INSERT admin_support(first_name, last_name, phone, email, employee_serial, id_support_department) " \
                       "VALUES('" + admin_dict["first_name"] + "','" + admin_dict["last_name"] + "','" + admin_dict[
                           "phone"] + "','" + admin_dict["email"] + "','" + admin_dict["employee_serial"] + "','" + \
                       admin_dict["id_support_department"] + "') "
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "admin_support was created correctly"
        else:
            connection.close_connection()
            return "This support department does not exist"

    def delete(self, id):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM admin_support WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "DELETE FROM admin_support WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "Admin_support was deleted"
        return "This admin_support does not exist"

    def update(self, id, admin_dict):
        connection = MsqlConnection()
        sentence_search = "SELECT * FROM support_department WHERE id='" + admin_dict["id_support_department"] + "'"
        row = connection.get_all(sentence_search)
        if row:
            sentence = "UPDATE admin_support set first_name = '" + admin_dict["first_name"] + "',  last_name = '" + \
                       admin_dict["last_name"] + "', phone = '" + admin_dict["phone"] + "', email = '" + admin_dict[
                           "email"] + "', employee_serial = '" + admin_dict["employee_serial"] + "', employee_serial = '" + \
                       admin_dict["id_support_department"] + "' WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "admin_support was updated correctly"
        else:
            connection.close_connection()
            return "This support department does not exist"

