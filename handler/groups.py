from flask import jsonify
from dao.groups import GroupsDAO


class GroupHandler:
    def build_group_chat_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gName'] = row[1]
        result['admin'] = row[2]
        return result


    def getAllGroups(self):
        dao = GroupsDAO()
        groups_list = dao.getAllGroups()
        result_list = []
        for row in groups_list:
            result_list.append(self.build_group_chat_dict(row))
        return jsonify(Groups=result_list)
