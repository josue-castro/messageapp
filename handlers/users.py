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
        return result

    def build_user_contact_dict(self, row):
        result = {}
        result['firstname'] = row[0]
        result['lastname'] = row[1]
        result['username'] = row[2]
        result['phone'] = row[3]
        result['email'] = row[4]
        return result

    def build_username_dict(self, row):
        result = {'username': row[0]}
        return result

    def build_user_groups_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gname'] = row[1]
        result['pid'] = row[2]

    def build_user_attributes(self, pid, firstName, lastName, username, phone, email):
        result = {}
        result['pid'] = pid
        result['firstName'] = firstName
        result['lastName'] = lastName
        result['username'] = username
        result['phone'] = phone
        result['email'] = email
        return result

    def getAllUsers(self):
        dao = UserDAO()
        user_list = dao.getAllUsers()
        result_list = []
        for row in user_list:
            result_list.append(self.build_username_dict(row))
        return jsonify(Users=result_list)

    def getUserById(self, pid):
        dao = UserDAO()
        row = dao.getUserById(pid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def getUserByPhone(self, phone):
        dao = UserDAO()
        row = dao.getUserByPhone(phone)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def getUserByEmail(self, email):
        dao = UserDAO()
        row = dao.getUserByPhone(email)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def getUserByUsername(self, username):
        dao = UserDAO()
        row =dao.getUserByUsername(username)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def getUserGroups(self, pid):
        dao = UserDAO()
        group_list = dao.getUserGroups(pid)
        result_list = []
        for row in group_list:
            result_list.append(self.build_user_groups_dict(row))
        return jsonify(My_Groups=result_list)

    def getUserContacts(self, pid):
        dao = UserDAO()
        contact_list = dao.getUserContacts(pid)
        result_list = []
        for row in contact_list:
            result_list.append(self.build_user_contact_dict(row))
        return jsonify(My_contacts=result_list)


    def insertUser(self, form):
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            firstName = form['firstName']
            lastName = form['lastName']
            username = form['username']
            phone = form['phone']
            email = form['email']
            if firstName and lastName and username and phone and email:
                dao = UserDAO()
                pid = dao.insert(firstName, lastName, username, phone, email)
                result = self.build_user_attributes(pid, firstName, lastName, username, phone, email)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deletePart(self, pid):
        dao = UserDAO()
        if not dao.getUserById(pid):
            return jsonify(Error="Part not found."), 404
        else:
            dao.delete(pid)
            return jsonify(DeleteStatus="OK"), 200