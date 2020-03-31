from TechTeam.msql.MsqlConnection import MsqlConnection

"""
las llaves foraneas no jalan
"""

class ProblemTypeAdapter(object):
    def list(self):
        connection = MsqlConnection()
        sentence = "SELECT * FROM problem_types"
        records = connection.get_all(sentence)
        connection.close_connection()
        records_to_return = []
        for record in records:
            each_problem_type = {
                "name": record[0],
                "description": record[1],
            }
            records_to_return.append(each_problem_type)
        return records_to_return

    def new(self, problem_type_dict):
        connection = MsqlConnection()
        sentence = "INSERT problem_types(name, description) " \
                   "VALUES('" + problem_type_dict["name"] + "','" + problem_type_dict[
                       "description"] + "') "
        connection.execute(sentence)
        connection.commit()
        connection.close_connection()
        return "problem_types was created correctly"""

    def delete(self, id):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM problem_types WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "DELETE FROM problem_types WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()
            connection.close_connection()
            return "problem_types was deleted"
        return "This problem_types does not exist"

    def update(self, id, problem_types_dict):
        connection = MsqlConnection()
        sentenceSearh = "SELECT * FROM problem_types WHERE ID = " + str(id)
        row = connection.get_one(sentenceSearh)
        if row:
            sentence = "UPDATE problem_types set name = '" + problem_types_dict[
                "name"] + "',  description = '" + "' WHERE ID = '" + str(id) + "'"
            connection.execute(sentence)
            connection.commit()

            connection.close_connection()
            return "problem_types was updated"
        return "This problem_types does not exist"
