from flask import jsonify
from dao.user import UserDAO


class UserHandler:
    def build_user_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
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

    def build_user_groups_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gname'] = row[1]
        result['pid'] = row[2]
        return result

    def build_user_attributes(self, pid, firstName, lastName, username, phone, email):
        result = {}
        result['pid'] = pid
        result['firstname'] = firstName
        result['lastname'] = lastName
        result['username'] = username
        result['phone'] = phone
        result['email'] = email
        return result

    def UserLogin(self, json):
        if len(json) != 2:
            return jsonify(Error="Malformed query string"), 402
        else:
            username = json["username"]
            password = json["password"]
            if username and password:
                dao = UserDAO()
                row = dao.UserLogin(username, password)
                if not row:
                    return jsonify(Error="Username or password are incorrect"), 404
                else:
                    user = self.build_user_dict(row)
                    return jsonify(User=user)
            else:
                return jsonify(Error="Missing username or password"), 400

    def getAllUsers(self):
        dao = UserDAO()
        user_list = dao.getAllUsers()
        result_list = []
        for row in user_list:
            result_list.append(self.build_user_dict(row))
        return jsonify(Users=result_list)

    def getUserById(self, pid):
        dao = UserDAO()
        row = dao.getUserById(pid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def searchUser(self, args):
        username = args.get("username")
        firstname = args.get("firstname")
        lastname = args.get("lastname")
        phone = args.get("phone")
        email = args.get("email")
        dao = UserDAO()

        if (len(args) == 1) and (username or email or phone):
            if username:
                row = dao.getUserByUsername(username)
            elif phone:
                row = dao.getUserByPhone(phone)
            else:
                row = dao.getUserByEmail(email)

            if not row:
                return jsonify(Error="User Not Found"), 404
            else:
                user = self.build_user_dict(row)
                return jsonify(User=user)
        elif (len(args) == 2) and firstname and lastname:
            user_list = dao.getUserSearchByName(firstname, lastname)
            result_list = []
            for row in user_list:
                result_list.append(self.build_user_dict(row))
            return jsonify(Users=result_list)
        else:
            return jsonify(Error="Malformed query string"), 400

    # def getUserByPhone(self, phone):
    #     dao = UserDAO()
    #     row = dao.getUserByPhone(phone)
    #     if not row:
    #         return jsonify(Error="User Not Found"), 404
    #     else:
    #         user = self.build_user_dict(row)
    #         return jsonify(User=user)

    # def getUserByEmail(self, email):
    #     dao = UserDAO()
    #     row = dao.getUserByPhone(email)
    #     if not row:
    #         return jsonify(Error="User Not Found"), 404
    #     else:
    #         user = self.build_user_dict(row)
    #         return jsonify(User=user)

    # def getUserByUsername(self, username):
    #     dao = UserDAO()
    #     row = dao.getUserByUsername(username)
    #     if not row:
    #         return jsonify(Error="User Not Found"), 404
    #     else:
    #         user = self.build_user_dict(row)
    #         return jsonify(User=user)

    # def getUserSearchByName(self, firstName, lastName):
    #     dao = UserDAO()
    #     user_list = dao.getUserSearchByName(firstName, lastName)
    #     result_list = []
    #     for row in user_list:
    #         result_list.append(self.build_user_dict(row))
    #     return jsonify(Contacts=result_list)

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

    def searchContacts(self, pid, args):
        firstname = args.get("firstname")
        lastname = args.get("lastname")
        dao = UserDAO()

        if (len(args) == 2) and firstname and lastname:
            contact_list = dao.getUserContactsByName(pid, firstname, lastname)
            result_list = []
            for row in contact_list:
                result_list.append(self.build_user_dict(row))

            return jsonify(Users=result_list)
        else:
            return jsonify(Error="Malformed query string"), 400

    # def getUserContactsByName(self, pid, firstName, lastName):
    #     dao = UserDAO()
    #     contact_list = dao.getUserContactsByName(pid, firstName, lastName)
    #     result_list = []
    #     for row in contact_list:
    #         result_list.append(self.build_user_dict(row))
    #     return jsonify(Contacts=result_list)

    def insertUser(self, json):
        if len(json) != 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            firstname = json['firstname']
            lastname = json['lastname']
            username = json['username']
            phone = json['phone']
            email = json['email']
            password = json['password']
            if firstname and lastname and username and (phone or email):
                dao = UserDAO()
                pid = dao.insert(firstname, lastname, username, phone, email, password)
                result = self.build_user_attributes(pid, firstname, lastname, username, phone, email)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteUser(self, pid):
        dao = UserDAO()
        if not dao.getUserById(pid):
            return jsonify(Error="User not found."), 404
        else:
            dao.delete(pid)
            return jsonify(DeleteStatus="OK"), 200
