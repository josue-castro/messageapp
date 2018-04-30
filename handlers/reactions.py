from flask import jsonify
from dao.reaction import ReactionDAO


class ReactionHandler:
    def mapToDic(self, row):
        result = {}
        result['mid'] = row[0]
        result['pid'] = row[1]
        return result

    def mapLikesToDic(self, row):
        result = {}
        result['username'] = row[0]
        return result

    def getMessageLikes(self, mid):
        dao = ReactionDAO()
        likes = dao.getMessageLikes(mid)
        return jsonify(Likes=likes)

    def getWhoLikedMessage(self, mid):
        dao = ReactionDAO()
        like_list = dao.getWhoLikedMessage(mid)
        result_list = []
        for m in like_list:
            result_list.append(self.mapLikesToDic(m))
        return jsonify(Like_list=result_list)

    def getMessageDislikes(self, mid):
        dao = ReactionDAO()
        dislikes = dao.getMessageDislikes(mid)
        return jsonify(Dislikes=dislikes)

    def getWhoDislikedMessage(self, mid):
        dao = ReactionDAO()
        dislike_list = dao.getWhoDisLikedMessage(mid)
        result_list = []
        for m in dislike_list:
            result_list.append(self.mapLikesToDic(m))
        return jsonify(Dislike_list=result_list)
