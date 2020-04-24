from TechTeam.msql.MsqlConnection import MsqlConnection
import datetime


class RequestAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM request"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_request = {
                "id": record[0],
                "id_problem_type": record[1],
                "description": record[2],
                "creation_date": record[3],
                "update_date": record[4],
                "date_closed_ticket": record[5],
                "user_id_creation": record[6],
                "status": record[7],
                "solution": record[8],
                "priority": record[9],
                "country": record[10],
            }
            records_to_return.append(each_request)
        return records_to_return

    def new(self, request_dict):
        connection = MsqlConnection()
        sentence_search = "SELECT * FROM problem_types WHERE id='" + request_dict["id_problem_type"] + "'"
        row = connection.get_all(sentence_search)
        if row:
            sentence_search2 = "SELECT * FROM users WHERE id='" + request_dict["user_id_creation"] + "'"
            row2 = connection.get_all(sentence_search2)
            if row2:
                x = datetime.datetime.now()
                current_date = str(x.year) + "-" + str(x.month) + "-" + str(x.day)
                sentence = "INSERT request(id_problemType, description, creation_date, user_id_creation, status, priority, country) VALUES('" + request_dict["id_problem_type"] + "','" \
                           + request_dict["description"] + "','" + str(current_date) + "','" \
                           + request_dict["user_id_creation"] + "','IN PROCESS','" + request_dict["priority"] \
                           + "','" + request_dict["country"] +"')"
                connection.execute(sentence)
                connection.commit()
                connection.close_connection()
                return "This request was created succesfully"
            else:
                connection.close_connection()
                return "This user does not exist"
        else:
            connection.close_connection()
            return "This problem type does not exist"


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
            sentence_search = "SELECT * FROM problem_types WHERE id='" + request_dict["id_problem_type"] + "'"
            row_2 = connection.get_all(sentence_search)
            if row_2:
                x = datetime.datetime.now()
                current_date = str(x.year) + "-" + str(x.month) + "-" + str(x.day)
                sentence = "UPDATE request set id_problemType = '" + request_dict[
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
            else:
                connection.close_connection()
                return "This problem type does not exist"
        else:
            connection.close_connection()
            return "This request does not exist"
