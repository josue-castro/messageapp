from flask import jsonify
from dao.contact import ContactDAO


class ContactHandler:
    def mapToDic(self, row):
        result = {}
        result['pid'] = row[0]
        result['contact_id'] = row[1]
        return result

    def map_to_contact_info(self, row):
        result = {}
        result['firstname'] = row[0]
        result['lastname'] = row[1]
        result['username'] = row[2]
        result['phone'] = row[3]
        result['email'] = row[4]
        return result

    def getMyContacts(self, pid):
        dao = ContactDAO()
        result = dao.getMyContactsINFO(pid)
        mapped_results = []
        for c in result:
            mapped_results.append(self.map_to_contact_info(c))
        return jsonify(My_contacts=mapped_results)

    def getContactByName(self, pid, name):
        dao = ContactDAO()
        result = dao.getContactByName(pid, name)
        mapped_results = []
        for c in result:
            mapped_results.append(self.mapToDic(c))
        return jsonify(Contact=mapped_results)
