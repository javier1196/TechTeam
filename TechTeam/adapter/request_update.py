from TechTeam.msql.MsqlConnection import MsqlConnection

"""
Esta clase no jala por las llaves foraneas
"""


class RequestUpdateAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM request_update"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_request = {
                "id_problem_type": record[0],
                "description": record[1],
                "status": record[2],
                "date": record[3],
            }
            records_to_return.append(each_request)
        return records_to_return

    def new(self, request_update_dict):
        connection = MsqlConnection()
        sentence = "INSERT request_update(id_problem_type, description, " \
                   "status, date) VALUES('" + request_update_dict["id_problem_type"] + "','" + \
                   request_update_dict["description"] + "','" + request_update_dict["status"] + "','" + request_update_dict[
                       "status"] + "','" + request_update_dict["date"] + "') "
        connection.execute(sentence)
        connection.commit()
        connection.close_connection()
        return "request_update was created correctly"""

    def delete(self, id):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM request_update WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "DELETE FROM request_update WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "request_update was deleted"
        return "This request_update does not exist"

    def update(self, id, request_update_dict):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM request_update WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "UPDATE request set id_problem_type = '" + request_update_dict[
                "id_problem_type"] + "',  status = '" + request_update_dict["status"] + "',  date = '" + \
                       request_update_dict["date"] + "' WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()

            connection.close_connection()
            return "request_update was updated"
        return "This request_update does not exist"
