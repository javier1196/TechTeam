from TechTeam.msql.MsqlConnection import MsqlConnection

"""
Esta clase no jala por las llaves foraneas
"""

class RequestAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM request"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_request = {
                "id_problem_type": record[0],
                "description": record[1],
                "creation_date": record[0],
                "update_date": record[1],
                "date_closed_ticket": record[0],
                "status": record[1],
                "solution": record[1],
                "priority": record[0],
                "country": record[1],
            }
            records_to_return.append(each_request)
        return records_to_return

    def new(self, request_dict):
        connection = MsqlConnection()
        sentence = "INSERT request(id_problem_type, description, creation_date, update_date, date_closed_ticket, " \
                   "status, solution, priority, country) VALUES('" + request_dict["id_problem_type"] + "','" + request_dict["description"] + "','" + request_dict["creation_date"] + "','" + request_dict["update_date"] + "','" + request_dict["status"] + "','" + request_dict["solution"] + "','" + request_dict["priority"] + "','" + request_dict["country"] + "') "
        connection.execute(sentence)
        connection.commit()
        connection.close_connection()
        return "request was created correctly"""

    def delete(self, id):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM request WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "DELETE FROM request WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "request was deleted"
        return "This request does not exist"

    def update(self, id, request_dict):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM request WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "UPDATE request set id_problem_type = '" + request_dict[
                "id_problem_type"] + "',  description = '" + request_dict["description"] + "',  creation_date = '" + \
                       request_dict["creation_date"] + "',  update_date = '" + request_dict[
                           "update_date"] + "',  date_closed_ticket = '" + request_dict[
                           "date_closed_ticket"] + "',  status = '" + request_dict[
                           "status"] + "',  solution = '" + request_dict[
                           "solution"] + "',  priority = '" + request_dict[
                           "priority"] + "',  country = '" + request_dict[
                           "country"] + "' WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()

            connection.close_connection()
            return "request was updated"
        return "This request does not exist"
