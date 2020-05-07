from TechTeam.msql.MsqlConnection import MsqlConnection
import datetime

class RequestUpdateAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM request_update"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_request = {
                "id": record[0],
                "id_department_support": record[1],
                "description": record[2],
                "status": record[3],
                "date": record[4],
                "id_request": record[5]
            }
            records_to_return.append(each_request)
        return records_to_return

    def new(self, request_update_dict):
        connection = MsqlConnection()
        sentence_search = "SELECT * FROM support_department WHERE id='" + request_update_dict["id_department_support"] +"'"
        row = connection.get_all(sentence_search)
        if row:
            sentence_search2 = "SELECT * FROM request WHERE id='" + request_update_dict[
                "id_request"] + "'"
            row2 = connection.get_all((sentence_search2))
            if row2:
                x = datetime.datetime.now()
                current_date = str(x.year) + "-" + str(x.month) + "-" + str(x.day)
                sentence = "INSERT request_update(id_department_support, description, " \
                           "status, date, id_request) VALUES('" + request_update_dict["id_department_support"] + "','" + \
                           request_update_dict["description"] + "','" + request_update_dict["status"] + "','" \
                           + str(current_date) + "','" + request_update_dict["id_request"] + "')"
                connection.execute(sentence)
                connection.commit()
                connection.close_connection()
                return "request_update was created correctly"
            else:
                connection.close_connection()
                return "This id request does not exist"
        else:
            connection.close_connection()
            return "This id support department does not exist"

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
        sentence_searh = "SELECT * FROM request_update WHERE ID = " + str(id)
        row = connection.get_one(sentence_searh)
        if row:
            sentence_search2 = "SELECT * FROM support_department WHERE id='" + request_update_dict[
                "id_department_support"] + "'"
            row2 = connection.get_all(sentence_search2)
            if row2:
                sentence_search3 = "SELECT * FROM request WHERE id='" + request_update_dict[
                    "id_request"] + "'"
                row3 = connection.get_all(sentence_search3)
                if row3:
                    x = datetime.datetime.now()
                    current_date = str(x.year) + "-" + str(x.month) + "-" + str(x.day)
                    sentence = "UPDATE request_update set id_department_support = '" + request_update_dict["id_department_support"] + "',  description = '" + request_update_dict["description"] + "',  status = '" + request_update_dict["status"] + "',  date = '" + str(current_date) + "',  id_request = '" + request_update_dict["id_request"] + "' WHERE ID = '" + str(id) + "'"
                    connection.execute(sentence)
                    connection.commit()

                    connection.close_connection()
                    return "request_update was updated"
                else:
                    return "id request does not exist"
            else:
                return "id support deparment does not exist"
        return "This request_update does not exist"
