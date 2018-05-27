from flask import jsonify
from dao.dashboard import DashboardDAO


class DashboardHandler:
    def build_date_count(self, row):
        result = {}
        result['date'] = row[0]
        result['count'] = row[1]
        return result

    def build_hashtag_count(self, row):
        result = {}
        result['hashtag'] = row[0]
        result['count'] = row[1]
        return result

    def build_user_activity(self, row):
        result = {}
        result['username'] = row[0]
        result['posts'] = row[1]
        return result

    def messagesPerDay(self):
        dao = DashboardDAO()
        list = dao.messagesPerDay()
        result_list = []
        for row in list:
            result_list.append(self.build_date_count(row))
        return jsonify(Message_count=result_list)

    def topTenHashtags(self):
        dao = DashboardDAO()
        list = dao.topTenHashtags()
        result_list = []
        for row in list:
            result_list.append(row)
        return jsonify(Hashtag_count=result_list)

    def repliesPerDay(self):
        dao = DashboardDAO()
        list = dao.repliesPerDay()
        result_list = []
        for row in list:
            result_list.append(self.build_date_count(row))
        return jsonify(Reply_count=result_list)

    def topActiveUsers(self):
        dao = DashboardDAO()
        list = dao.topActiveUsers()
        result_list = []
        for row in list:
            result_list.append(self.build_user_activity(row))
        return jsonify(Active_users=result_list)

    def likesPerDay(self):
        dao = DashboardDAO()
        list = dao.likesPerDay()
        result_list = []
        for row in list:
            result_list.append(self.build_date_count(row))
        return jsonify(Like_count=result_list)

    def dislikesPerDay(self):
        dao = DashboardDAO()
        list = dao.dislikesPerDay()
        result_list = []
        for row in list:
            result_list.append(self.build_date_count(row))
        return jsonify(Dislike_count=result_list)
