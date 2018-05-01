from flask import jsonify
from dao.member import MembersDAO


class MemberHandler:
    def build_member_dict(self,row):
        result = {}
        result['username'] = row[0]
        result['firstName'] = row[1]
        result['lastName'] = row[2]

    def build_member_attributes(self, gid, pid):
        result = {}
        result['gid'] = gid
        result['pid'] = pid
        return result

    def getMembers(self, gid):
        dao = MembersDAO()
        member_list = dao.getMembersINFO(gid)
        result_list = []
        for m in member_list:
            result_list.append(self.build_member_dict(m))
        return jsonify(Members=result_list)

    def addMember(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            gid = form['gid']
            pid = form['pid']

            if pid and gid:
                dao = MembersDAO()
                pid = dao.insertMember(gid, pid)
                result = self.build_member_attributes(gid, pid)
                return jsonify(new_Member=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def delete(self, gid, pid):
        dao = MembersDAO()
        if not dao.getMemberById(gid, pid):
            return jsonify(Error="Member not found."), 404
        else:
            dao.delete(gid)
            return jsonify(DeleteStatus="OK"), 200
