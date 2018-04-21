from flask import jsonify
from dao.group import GroupsDAO


class GroupHandler:
    def build_group_chat_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gName'] = row[1]
        result['pid'] = row[2]
        return result

    def getAllGroups(self):
        dao = GroupsDAO()
        groups_list = dao.getAllGroupsINFO()
        result_list = []
        for row in groups_list:
            result_list.append(self.build_group_chat_dict(row))
        return jsonify(Groups=result_list)

    def getGroupOwner(self, gid):
        dao = GroupsDAO()
        group_owner = dao.getGroupOwnerINFO(gid)
        mapped_result = self.build_group_chat_dict(group_owner)
        return jsonify(Owner_is=mapped_result)
