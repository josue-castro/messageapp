from flask import jsonify
from dao.member import MembersDAO


class MemberHandler:
    def build_member_dict(self,row):
        result = {}
        result['username'] = row[0]
        result['firstName'] = row[1]
        result['lastName'] = row[2]

    def getMembers(self, gid):
        dao = MembersDAO()
        member_list = dao.getMembersINFO(gid)
        result_list = []
        for m in member_list:
            result_list.append(self.build_member_dict(m))
        return jsonify(Members=result_list)

