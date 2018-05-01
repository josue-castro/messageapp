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

    def map_likes_dislikes_attributes(self, mid, pid):
        result = {}
        result['mid'] = mid
        result['pid'] = pid
        return result

    def map_message_tags_attributes(self, mid, hid):
        result = {}
        result['mid'] = mid
        result['hid'] = hid
        return result

    def map_hashtag_attributes(self, hid, tag):
        result = {}
        result['hid'] = hid
        result['tag'] = tag
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

    def like(self, form):
        """Add a like on the message"""
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            mid = form['mid']
            pid = form['pid']
            if pid and mid:
                dao = ReactionDAO()
                mid = dao.insertLike(mid, pid)
                result = self.map_likes_dislikes_attributes(mid, pid)
                return jsonify(Message=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def unlike(self, mid, pid):
        """delete a like on a message"""
        dao = ReactionDAO()
        if not dao.getWhoLikedById(mid, pid):
            return jsonify(Error="User not found."), 404
        else:
            dao.deleteDislike(mid, pid)
            return jsonify(DeleteStatus="OK"), 200

    def dislike(self, form):
        """Add a like on the message"""
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            mid = form['mid']
            pid = form['pid']
            if pid and mid:
                dao = ReactionDAO()
                mid = dao.insertDislike(mid, pid)
                result = self.map_likes_dislikes_attributes(mid, pid)
                return jsonify(Dislike=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def undislike(self, mid, pid):
        """delete a like on a message"""
        dao = ReactionDAO()
        if not dao.getWhoDislikedById(mid, pid):
            return jsonify(Error="User not found."), 404
        else:
            dao.deleteDislike(mid, pid)
            return jsonify(DeleteStatus="OK"), 200

    def tagToMessage(self, form):
        """Add a hashtag on a specified message"""
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            mid = form['mid']
            hid = form['hid']
            if hid and mid:
                dao = ReactionDAO()
                mid = dao.insertTag(mid, hid)
                result = self.map_message_tags_attributes(mid, hid)
                return jsonify(Hashtag=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def un_tagToMessage(self, mid, hid):
        """delete a hashtag from a specified message"""
        dao = ReactionDAO()
        if not dao.getMessageHashtagById(mid, hid):
            return jsonify(Error="User not found."), 404
        else:
            dao.deleteDislike(mid, pid)
            return jsonify(DeleteStatus="OK"), 200

    def createNewHashtag(self, form):
        """Create a new Hashtag"""
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            tag = form['tag']
            if tag:
                dao = ReactionDAO()
                hid = dao.createHashtag(tag)
                result = self.map_hashtag_attributes(hid, tag)
                return jsonify(Hashtag=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def removeHashtag(self, hid):
        """delete a hashtag."""
        dao = ReactionDAO()
        if not dao.getHashtagById(hid):
            return jsonify(Error="User not found."), 404
        else:
            dao.deleteHashtag(hid)
            return jsonify(DeleteStatus="OK"), 200
