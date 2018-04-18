from flask import jsonify
from dao.groups import GroupsDAO


class GroupHandler:
    def build_group_chat_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gName'] = row[1]
        result['admin'] = row[2]
        return result


    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['scity'] = row[2]
        result['sphone'] = row[3]
        return result

    def build_part_attributes(self, pid, pname, pcolor, pmaterial, pprice):
        result = {}
        result['pid'] = pid
        result['pname'] = pname
        result['pmaterial'] = pcolor
        result['pcolor'] = pmaterial
        result['pprice'] = pprice
        return result

    def getAllGroups(self):
        dao = GroupsDAO()
        groups_list = dao.getAllGroups()
        result_list = []
        for row in groups_list:
            result_list.append(self.build_group_chat_dict(row))
        return jsonify(Groups=result_list)