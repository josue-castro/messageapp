from flask import jsonify
from dao.user import UserDAO

class UserHandler:
    def build_user_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['firstName'] = row[1]
        result['lastName'] = row[2]
        result['username'] = row[3]
        result['phone'] = row[4]
        result['email'] = row[5]

    def getAllUsers(self):
        dao = UserDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result_list.append(self.build_user_dict(row))
        return jsonify(Users=result_list)