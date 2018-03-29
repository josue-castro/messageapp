from flask import jsonify
from dao.members import MembersDAO
class MemberHandler:
    def mapToDic(self, row):
        result = {}
        result['gid'] = row[0]
        result['pid'] = row[1]
        return result

    def getMembers(self, gid):
        dao = MembersDAO()
        result = dao.getMembers(gid)
        mapped_results = []
        for c in result:
            mapped_results.append(self.mapToDic(c))
        return jsonify(Members=mapped_results)

