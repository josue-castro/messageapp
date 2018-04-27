from flask import jsonify
from dao.member import MembersDAO


class MemberHandler:
    def mapToDic(self, row):
        result = {'username': row}
        return result

    def getMembers(self, gid):
        dao = MembersDAO()
        result = dao.getMembersINFO(gid)
        mapped_results = []
        for c in result:
            mapped_results.append(self.mapToDic(c))
        return jsonify(Members=mapped_results)

