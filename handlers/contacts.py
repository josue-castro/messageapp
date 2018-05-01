from flask import jsonify
from dao.contact import ContactDAO


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


    def insertContact(self, form):
        if len(form) !=3:
            return jsonify(Error="Malformed post request"), 400
        else:
            pid = form['pid']
            contact_id = form['contact_id']

            if pid and contact_id:
                dao = ContactDAO()
                pid = dao.addContact(pid, contact_id)
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