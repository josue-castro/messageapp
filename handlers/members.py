from flask import jsonify
from dao.member import MembersDAO
from dao.user import UserDAO
from dao.group import GroupsDAO


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

    def addMember(self, pid, json):
        if len(json) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            gid = json['gid']
            username = json['username']

            if username and gid:
                member_dao = MembersDAO()
                user_dao = UserDAO()
                group_dao = GroupsDAO()
                if group_dao.getAllGroupsAdminByUserINFO(pid):
                    if gid in group_dao.getAllGroupsAdminByUserINFO(pid)[0]:
                        if user_dao.getUserByUsername(username):
                            user_id = user_dao.getUserByUsername(username)[0]
                            if not user_dao.getUserGroups(user_id):
                                member_dao.insertMember(gid, user_id)
                                result = self.build_member_attributes(gid, user_id)
                                return jsonify(new_Member=result), 201
                            elif gid not in user_dao.getUserGroups(user_id)[0]:
                                member_dao.insertMember(gid, user_id)
                                result = self.build_member_attributes(gid, user_id)
                                return jsonify(new_Member=result), 201
                            else:
                                return jsonify(Error="User is already a member"), 400
                        else:
                            return jsonify(Error="User does not exist"), 400
                    else:
                        return jsonify(Error="You are not administrator of group"), 400
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def delete(self, gid, pid):
        dao = MembersDAO()
        if not dao.getMemberById(gid, pid):
            return jsonify(Error="Member not found."), 404
        else:
            dao.delete(gid)
            return jsonify(DeleteStatus="OK"), 200
