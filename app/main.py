from flask import Flask, request, render_template
from json import loads, dumps
import os
from os import environ
import time
import Program as p
import SearchLogic.Helper as h
import DataBase.FireBase as fb

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')

@app.route("/")
def index():
    print("Time start - " + str(time.ctime()))
    method = str(request.args.get('method'))  # post || simple || between || verified || bot
    print(method)
    print(type(method))
    # user's params
    id = request.args.get('id')  # user's vk id
    fullName = str(request.args.get('full_name'))  # full vk name, friends will be later, on line 24
    deviceModel = str(request.args.get('device_model'))
    androidVersion = str(request.args.get('android_version'))

    # request's params
    owner = str(request.args.get('owner'))  # vk id of application owner
    fromId = h.getPureLink(str(request.args.get('from')))  # id user from
    toId = h.getPureLink(str(request.args.get('to')))  # id user to
    friends = request.args.get('friends')  # list of friends in case we search from owner (owner id == fromId)

    if method == 'simple':
        output = p.getWay(int(fromId), toId, loads(friends))
    elif method == 'between':
        output = p.getWayBetween(fromId, toId)
    elif method == 'verified':
        output = p.getWay(int(fromId), toId, loads(friends))
    elif method == 'post':
        output = fb.postUserToDb(int(id), fullName, deviceModel, androidVersion)
    elif method == 'bot':
        output = p.getWayBetween(fromId, toId)
    else:
        return 'You have not done anything'

    if friends:
        fb.postRequestToStorage(owner, method, fromId, toId, loads(friends), output)
    elif owner:
        fb.postRequestToStorage(owner, method, fromId, toId, friends, output)
        
    output = dumps(output, ensure_ascii=False)
    print("Time end - " + str(time.ctime()))
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ.get("PORT", 5000))

