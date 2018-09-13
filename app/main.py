from flask import Flask, request, render_template
from json import loads, dumps
import os
import Program as p
import SearchLogic.Helper as h
import DataBase.FireBase as fb

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')

@app.route("/")
def index():
    return 'Hello, world!'

    method = str(request.args.get('method'))  # post || simple || between || verified
    # user's params
    id = request.args.get('id')  # user's vk id
    fullName = str(request.args.get('full_name'))  # full vk name
    deviceModel = str(request.args.get('device_model'))
    androidVersion = str(request.args.get('android_version'))

    # request's params
    owner = str(request.args.get('owner'))  # vk id of application owner
    fromId = str(request.args.get('from'))  # id user from
    toId = str(request.args.get('to'))  # id user to
    friends = request.args.get('friends')  # list of friends in case we search from owner (owner id == fromId)

    if method == 'simple':
        output = p.getWay(int(fromId), h.getPureLink(toId), loads(friends))
    elif method == 'between':
        output = p.getWayBetween(h.getPureLink(fromId), h.getPureLink(toId))
    elif method == 'verified':
        output = p.getWay(int(fromId), h.getPureLink(toId), loads(friends))
    elif method == 'post':
        output = fb.postUserToDb(int(id), fullName, deviceModel, androidVersion)
    else:
        return dumps(method) + " " + dumps(owner)

    if friends:
        fb.postRequestToStorage(owner, method, fromId, toId, loads(friends), output, fb.getTimeForRequests())
    else:
        fb.postRequestToStorage(owner, method, fromId, toId, friends, output, fb.getTimeForRequests())
        
    output = dumps(output, ensure_ascii=False)
    return output

if __name__ == '__main__':
	app.run(host='0.0.0.0')

