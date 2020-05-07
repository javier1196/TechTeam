from TechTeam.msql.MsqlConnection import MsqlConnection


class SupportDepartmentProblemType(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM support_department_problem_type"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_department_involved = {
                "id": record[0],
                "id_problem_type": record[1],
                "id_support_department": record[2],
            }
            records_to_return.append(each_department_involved)
        return records_to_return

    def new(self, department_involved_dict):
        connection = MsqlConnection()
        sentence_search_department_support = "SELECT * FROM support_department WHERE id ='" \
                                             + str(department_involved_dict["id_department_support"]) + "'"
        row = connection.get_all(sentence_search_department_support)
        if row:
            sentence_search_request = "SELECT * FROM problem_types WHERE id='" \
                                      + str(department_involved_dict["id_problem_type"]) + "'"
            row_request = connection.get_all(sentence_search_request)
            if row_request:
                sentence = "INSERT support_department_problem_type(id_problem_type, id_support_department) VALUES('" + \
                           str(department_involved_dict[
                               "id_problem_type"]) + "','" + str(department_involved_dict["id_department_support"]) + "') "
                connection.execute(sentence)
                connection.commit()
                connection.close_connection()
                return "This request was created correctly"
            else:
                connection.close_connection()
                return "This problem type does not exist"
        else:
            connection.close_connection()
            return "This department support does not exist"""

    def delete(self, id):
        connection = MsqlConnection()
        sentence_search = "SELECT * FROM support_department_problem_type WHERE ID = " + str(id)
        row = connection.get_one(sentence_search)
        if row:
            sentence = "DELETE FROM support_department_problem_type WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "support_department_problem_type was deleted"
        return "This departments_involved does not exist"

    def update(self, id, department_involved_dict):
        connection = MsqlConnection()
        sentence_search_department_support = "SELECT * FROM support_department WHERE id ='" \
                                             + department_involved_dict["id_department_support"] + "'"
        row = connection.get_all(sentence_search_department_support)
        if row:
            sentence_search_request = "SELECT * FROM problem_types WHERE id='" \
                                      + department_involved_dict["id_problem_type"] + "'"
            row_request = connection.get_all(sentence_search_request)
            if row_request:
                sentence = "UPDATE support_department_problem_type set id_problem_type = '" + department_involved_dict[
                    "id_problem_type"] + "',  id_support_department = '" + department_involved_dict[
                               "id_department_support"] + "' WHERE ID = '" + str(id) + "'"
                connection.execute(sentence)
                connection.commit()
                connection.close_connection()
                return "support_department_problem_type was updated"
            else:
                connection.close_connection()
                return "This problem_type does not exist"
        else:
            connection.close_connection()
            return "This department support does not exist"
