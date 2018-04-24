from flask import jsonify
from dao.contact import ContactDao


class ContactHandler:
    def mapToDic(self, row):
        result = {}
        result['pid'] = row[0]
        result['contact_id'] = row[1]
        return result

    def map_to_contact_info(self, row):
        result = {}
        result['pid'] = row[0]
        result['contact_id'] = row[1]
        result['firstname'] = row[2]
        result['lastname'] = row[3]
        result['username'] = row[4]
        result['phone'] = row[5]
        result['email'] = row[6]
        return result

    def getMyContacts(self, pid):
        result = dao.getMyContactsINFO(pid)
        dao = ContactDAO()
        result = dao.getMyContacts(pid)
        mapped_results = []
        for c in result:
            mapped_results.append(self.map_to_contact_info(c))
        return jsonify(My_contacts=mapped_results)

    def getContactByName(self,pid,name):
        dao = ContactDAO()
        result = dao.getContactByName(pid, name)
        mapped_results = []
        for c in result:
            mapped_results.append(self.mapToDic(c))
        return jsonify(Contact=mapped_results)
