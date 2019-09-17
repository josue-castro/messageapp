from flask import jsonify
from dao.dashboard import DashboardDAO


class DashboardHandler:
    def build_chart_dict(self, row):
        result = {}
        result['info'] = row[0]
        result['count'] = row[1]
        return result

    def messagesPerDay(self):
        dao = DashboardDAO()
        list = dao.messagesPerDay()
        result_list = []
        for row in list:
            result_list.append(self.build_chart_dict(row))
        return jsonify(Result=result_list)

    def topTenHashtags(self):
        dao = DashboardDAO()
        list = dao.topTenHashtags()
        result_list = []
        for row in list:
            result_list.append(self.build_chart_dict(row))
        return jsonify(Result=result_list)

    def repliesPerDay(self):
        dao = DashboardDAO()
        list = dao.repliesPerDay()
        result_list = []
        for row in list:
            result_list.append(self.build_chart_dict(row))
        return jsonify(Result=result_list)

    def topActiveUsers(self):
        dao = DashboardDAO()
        list = dao.topActiveUsers()
        result_list = []
        for row in list:
            result_list.append(self.build_chart_dict(row))
        return jsonify(Result=result_list)

    def likesPerDay(self):
        dao = DashboardDAO()
        list = dao.likesPerDay()
        result_list = []
        for row in list:
            result_list.append(self.build_chart_dict(row))
        return jsonify(Result=result_list)

    def dislikesPerDay(self):
        dao = DashboardDAO()
        list = dao.dislikesPerDay()
        result_list = []
        for row in list:
            result_list.append(self.build_chart_dict(row))
        return jsonify(Result=result_list)

    def topActiveUsers(self):
        dao = DashboardDAO()
        list = dao.topActiveUsers()
        result_list = []
        for row in list:
            result_list.append(self.build_chart_dict(row))
        return jsonify(Result=result_list)