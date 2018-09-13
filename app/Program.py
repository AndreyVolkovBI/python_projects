from API import VkAPI as API, APIKeys as keys
from SearchLogic import FirstLevel as algo


# works for both
# get way from you to another user
# and get way from you to verified user
def getWay(fromId, toId, friendsUserFrom):
    toId = API.getUsers(toId)
    if toId:
        toId = toId[0]['id']
        friendsUserTo = API.getFriends(toId)
        if len(friendsUserTo) == 0:
            return keys.noFriends
        result = algo.calculations(fromId, friendsUserFrom, toId, friendsUserTo)
        if len(result) == 0:
            return keys.tooFar
        return result
    return keys.noSuchUser


# works for get way between users only
def getWayBetween(fromId, toId):
    users = API.getUsers(fromId + ',' + toId)
    if users:
        fromId = users[0].get('id')  # id userFrom
        toId = users[1].get('id')  # id of userTo

        code = API.getVkScriptForExecute([fromId, toId])[0]
        friends = API.getExecute(code, keys.firstPair[1])
        friendsUserFrom = friends[0].get('items')  # list of ids of friends of userFrom
        friendsUserTo = friends[1].get('items', False)  # list of ids of friends of userTo
        if len(friendsUserFrom) == 0 or len(friendsUserTo) == 0:
            return keys.noFriends
        result = algo.calculations(fromId, friendsUserFrom, toId, friendsUserTo)
        if len(result) == 0:
            return keys.tooFar
        return result
    return keys.noSuchUser