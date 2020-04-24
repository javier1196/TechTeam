from TechTeam.msql.MsqlConnection import MsqlConnection


class DepartmentInvolvedAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM departments_involved"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_department_involved = {
                "id": record[0],
                "id_department_support": record[1],
                "id_request": record[2],
            }
            records_to_return.append(each_department_involved)
        return records_to_return

    def new(self, department_involved_dict):
        connection = MsqlConnection()
        sentence_search_department_support = "SELECT * FROM support_department WHERE id ='" \
                                             + department_involved_dict["id_department_support"] + "'"
        row = connection.get_all(sentence_search_department_support)
        if row:
            sentence_search_request = "SELECT * FROM request WHERE id='" \
                                      + department_involved_dict["id_request"] + "'"
            row_request = connection.get_all(sentence_search_request)
            if row_request:
                sentence = "INSERT departments_involved(id_department_support, id_request) VALUES('" + \
                           department_involved_dict[
                               "id_department_support"] + "','" + department_involved_dict["id_request"] + "') "
                connection.execute(sentence)
                connection.commit()
                connection.close_connection()
                return "This department involved was created correctly"
            else:
                connection.close_connection()
                return "This request does not exist"
        else:
            connection.close_connection()
            return "This department support does not exist"

    def delete(self, id):
        connection = MsqlConnection()
        sentence_search = "SELECT * FROM departments_involved WHERE ID = " + str(id)
        row = connection.get_one(sentence_search)
        if row:
            sentence = "DELETE FROM departments_involved WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "departments_involved was deleted"
        return "This departments_involved does not exist"

    def update(self, id, department_involved_dict):
        connection = MsqlConnection()
        sentence_search_department_support = "SELECT * FROM support_department WHERE id ='" \
                                             + department_involved_dict["id_department_support"] + "'"
        row = connection.get_all(sentence_search_department_support)
        if row:
            sentence_search_request = "SELECT * FROM request WHERE id='" \
                                      + department_involved_dict["id_request"] + "'"
            row_request = connection.get_all(sentence_search_request)
            if row_request:
                sentence = "UPDATE departments_involved set id_department_support = '" + department_involved_dict[
                    "id_department_support"] + "',  id_request = '" + department_involved_dict[
                               "id_request"] + "' WHERE ID = '" + str(id) + "'"
                connection.execute(sentence)
                connection.commit()
                connection.close_connection()
                return "departments_involved was updated"
            else:
                connection.close_connection()
                return "This request does not exist"
        else:
            connection.close_connection()
            return "This department support does not exist"
