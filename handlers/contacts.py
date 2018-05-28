from flask import jsonify
from dao.contact import ContactDAO
from dao.user import UserDAO


class ContactHandler:
    @staticmethod
    def mapToDic(row):
        result = {}
        result['pid'] = row[0]
        result['contact_id'] = row[1]
        return result

    @staticmethod
    def map_to_contact_info(row):
        result = {}
        result['firstname'] = row[0]
        result['lastname'] = row[1]
        result['username'] = row[2]
        result['phone'] = row[3]
        result['email'] = row[4]
        return result

    @staticmethod
    def map_contact_attributes(pid, contact_id):
        result = {}
        result['pid'] = pid
        result['contact_id'] = contact_id
        return result

    def getMyContacts(self, pid):
        dao = ContactDAO()
        result = dao.getMyContactsINFO(pid)
        mapped_results = []
        for c in result:
            mapped_results.append(self.map_to_contact_info(c))
        return jsonify(My_contacts=mapped_results)

    def getContactById(self, pid, contact_id):
        dao = ContactDAO()
        row = dao.getContactByid(pid, contact_id)
        if not row:
            return jsonify(Error="Contact Not Found"), 404
        else:
            user = self.map_to_contact_info(row)
            return jsonify(Contact=user)


    def insertContact(self, pid, json):
        if len(json) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            info = json['info']
            if info:
                user_dao = UserDAO()
                if user_dao.getUserByPhone(info):
                    contact_id = user_dao.getUserByPhone(info)[0]
                elif user_dao.getUserByEmail(info):
                    contact_id = user_dao.getUserByEmail(info)[0]
                else:
                    return jsonify(Error="User was not found"), 400
                contact_dao = ContactDAO()
                pid = contact_dao.addContact(pid, contact_id)
                result = self.map_contact_attributes(pid, contact_id)
                return jsonify(new_Contact=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def delete(self, pid, contact_id):
        dao = ContactDAO()
        if not dao.getMyContactByid(pid, contact_id):
            return jsonify(Error="User not found."), 404
        else:
            dao.delete(pid, contact_id)
            return jsonify(DeleteStatus="OK"), 200