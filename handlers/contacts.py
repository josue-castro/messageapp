from flask import jsonify
from dao.contact import ContactDAO
class ContactHandler:
    def mapToDic(self, row):
        result = {}
        result['main user'] = row[0]
        result['contact name'] = row[1]
        result['phone'] = row[2]
        result['email'] = row[3]
        result['cid'] = row[4]
        return result

    def getMyContacts(self, pid):
        dao = ContactDAO()
        result = dao.getMyContacts(pid)
        mapped_results = []
        for c in result:
            mapped_results.append(self.mapToDic(c))
        return jsonify(My_contacts=mapped_results)

    def getContactByName(self,pid,name):
        dao = ContactDAO()
        result = dao.getContactByName(pid, name)
        mapped_results = []
        for c in result:
            mapped_results.append(self.mapToDic(c))
        return jsonify(Contact=mapped_results)
