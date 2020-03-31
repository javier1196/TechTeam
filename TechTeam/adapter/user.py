from TechTeam.msql.MsqlConnection import MsqlConnection


class UserAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM users"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_user = {
                "id": record[0],
                "first_name": record[1],
                "last_name": record[2],
                "phone": record[3],
                "email": record[4],
                "employee_serial": record[5]
            }
            records_to_return.append(each_user)
        return records_to_return

    def new(self, user_dict):
        connection = MsqlConnection()
        sentence = "INSERT users(first_name, last_name, phone, email, employee_serial) VALUES('" + user_dict["first_name"] + "','" + user_dict["last_name"] + "','" + user_dict["phone"] + "','" + user_dict["email"] + "','" + user_dict["employee_serial"] + "') "
        connection.execute(sentence)
        connection.commit()
        connection.close_connection()
        return "User was created correctly"""

    def delete(self, id):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM users WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "DELETE FROM users WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "User was deleted"
        return "This User does not exist"

    def update(self, id, user_dict):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM users WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "UPDATE users set first_name = '" + user_dict["first_name"] + "',  last_name = '" + user_dict["last_name"] + "', phone = '" + user_dict["phone"] + "', email = '" + user_dict["email"] + "', employee_serial = '" + user_dict["employee_serial"] + "' WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()

            connection.close_connection()
            return "User was updated"
        return "This user does not exist"
