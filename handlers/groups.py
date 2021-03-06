from flask import jsonify
from dao.group import GroupsDAO


class GroupHandler:
    def build_group_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gname'] = row[1]
        result['pid'] = row[2]
        return result

    def build_user_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        result['username'] = row[3]
        result['phone'] = row[4]
        result['email'] = row[5]
        return result

    def build_group_attributes(self, gid, gname, pid):
        result = {}
        result['gid'] = gid
        result['gname'] = gname
        result['pid'] = pid
        return result

    def getAllGroupsINFO(self):
        dao = GroupsDAO()
        group_list = dao.getAllGroupsINFO()
        result_list = []
        for row in group_list:
            result_list.append(self.build_group_dict(row))
        return jsonify(Groups=result_list)

    def getGroupByIdINFO(self, gid):
        dao = GroupsDAO()
        row = dao.getGroupByIdINFO(gid)
        if not row:
            return jsonify(Error="Group Not Found"), 404
        else:
            group = self.build_group_dict(row)
            return jsonify(Group=group)

    def getGroupByGroupNameINFO(self, gname):
        dao = GroupsDAO()
        group_list = dao.getGroupByGroupNameINFO(gname)
        result_list = []
        for row in group_list:
            result_list.append(self.build_group_dict(row))
        return jsonify(Groups=result_list)

    def getGroupAdminInfo(self, gid):
        dao = GroupsDAO()
        admin = dao.getGroupAdminINFO(gid)
        result = self.build_user_dict(admin)
        return jsonify(Admin=result)

    def getAllGroupsAdminByUser(self, pid):
        dao = GroupsDAO()
        group_list = dao.getAllGroupsAdminByUserINFO(pid)
        result_list = []
        for row in group_list:
            result_list.append(self.build_group_dict(row))
        return jsonify(Groups=result_list)

    def getGroupMembersINFO(self, gid):
        dao = GroupsDAO()
        member_list = dao.getGroupMembersINFO(gid)
        result_list = []
        for row in member_list:
            result_list.append(self.build_user_dict(row))
        return jsonify(Members=result_list)

    def insertGroup(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            gname = form['gname']
            pid = form['pid']
            if gname and pid:
                dao = GroupsDAO()
                gid = dao.insertGroup(gname, pid)
                result = self.build_group_attributes(gid, gname, pid)
                return jsonify(Group=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def createGroup(self, pid, json):
        if len(json) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            gname = json['gname']
            if gname:
                dao = GroupsDAO()
                gid = dao.insertGroup(gname, pid)
                result = self.build_group_attributes(gid, gname, pid)
                return jsonify(new_Group=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def delete(self, gid):
        dao = GroupsDAO()
        if not dao.getGroupByIdINFO(gid):
            return jsonify(Error="User not found."), 404
        else:
            dao.delete(gid)
            return jsonify(DeleteStatus="OK"), 200