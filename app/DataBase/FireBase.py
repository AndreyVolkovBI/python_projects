import os
import datetime
import time
import pytz
import firebase_admin
from firebase_admin import credentials, firestore

sep = os.sep

cred = credentials.Certificate("app" + sep + "DataBase" + sep + "vkConnectionsAppKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# global variables to post data to FireBase every hour
requests = []
timeInterval = 10800  # time interval in sec - 3 hours
previousTime = 0


class User:
    def __init__(self, id, fullName, joinTime, deviceModel, androidVersion):
        self.Id = id
        self.FullName = fullName
        self.JoinTime = joinTime
        self.DeviceModel = deviceModel
        self.AndroidVersion = androidVersion


class Request:
    def __init__(self, owner, method, fromId, toId, friends, outputCount, time):
        self.Owner = owner
        self.Method = method
        self.FromId = fromId
        self.ToId = toId
        self.Friends = friends
        self.OutputCount = outputCount
        # self.Content = content
        self.Time = time


# post user at first entrance to the app
def postUserToDb(id, fullName, deviceModel, androidVersion):
    user = User(id, fullName, getTimeForRequests(), deviceModel, androidVersion)
    user = user.__dict__
    usersRef = db.collection(u'Data').document(u'Users')
    usersRef.update({str(id): user})
    return True


# all requests post to global list of requests
def postRequestToStorage(owner, method, fromId, toId, friends, outputCount):
    global requests
    request = Request(owner, method, fromId, toId, friends, outputCount, getTimeForRequests())
    request = request.__dict__
    requests.append(request)
    checkInterval()
    

def checkInterval():
    global previousTime
    global timeInterval
    currentTime = int(str(time.time()).split(".")[0])
    print("Check")
    if currentTime - previousTime > timeInterval:
        print("GOT IT!!!!!!!!!!!!")
        postRequestsToDb()
        previousTime = currentTime


# updates all the info from global variable requests to FireBase
def postRequestsToDb():
    global requests
    requestsRef = db.collection(u'Data').document(u'Requests')
    requestsRef.update({str(getTimeForRequests()).replace(".", "-"): requests})
    requests = []


def getTimeForRequests():
    time = str(datetime.datetime.now(pytz.timezone("Europe/Moscow"))).split('-')
    date = time[2].split(' ')[0] + '.' + time[1] + '.' + time[0]
    time = time[2].split(' ')[1].split('.')[0]
    return date + ' ' + time
