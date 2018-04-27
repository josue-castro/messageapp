from flask import jsonify
from dao.reaction import ReactionDAO


class ReactionHandler:
    def mapToDic(self, row):
        result = {}
        result['mid'] = row[0]
        result['pid'] = row[1]
        return result

    def mapLikesToDic(self, row):
        result = {'username': row}
        return result

    def getMessageLikes(self, mid):
        dao = ReactionDAO()
        result = dao.getMessageLikes(mid)
        return jsonify(Likes=result)

    def getWhoLikedMessage(self, mid):
        dao = ReactionDAO()
        result = dao.getMessageLikes(mid)
        mapped_results = []
        for m in result:
            mapped_results.append(self.mapLikesToDic(m))
        return jsonify(Like_list=result)

    def getMessageDislikes(self, mid):
        dao = ReactionDAO()
        result = dao.getMessageDislikes(mid)
        return jsonify(Dislikes=result)

    def getWhoDislikedMessage(self, mid):
        dao = ReactionDAO()
        result = dao.getWhoDisLikedMessage(mid)
        mapped_results = []
        for m in result:
            mapped_results.append(self.mapLikesToDic(m))
        return jsonify(Dislike_list=result)
