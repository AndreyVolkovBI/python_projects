def getPureLink(link):
    link = link.strip().lower()
    if 'vk.com/' in link:
        link = link.split('vk.com/')[1]
    if link.startswith('/'):
        link = link.split('/')[1]
    if link.endswith('/'):
        link = link.split('/')[0]
    return link


def clearCircles(circles):
    circles = {k: v for k, v in circles.items() if v is not None}
    circles = {k: v for k, v in circles.items() if v is not False}
    return circles


def getItems(circles):
    returnDict = {}
    for key in circles:
        returnDict[key] = circles[key].get('items')
    return returnDict


def fillAllTheVertices(circles):
    tempDict = {}
    for item in circles:
        for index in circles[item]:
            if index not in circles:
                if tempDict.get(index):
                    tempDict[index].append(item)
                else:
                    tempDict[index] = [item]
    for item in tempDict:
        circles[item] = tempDict[item]
    return circles

def makeListsNicer(outputList):
    resultList = []
    tempList = []
    for index in outputList:
        for item in index:
            tempList.append(
                {'id': item['id'],
                 'full_name': item['first_name'] + ' ' + item['last_name'],
                 'photo': item['photo_100']})
        resultList.append(tempList)
        tempList = []
    return resultList

def BFS(s, Adj):
    parent = {s: None}
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            if u in Adj:
                for v in Adj[u]:
                    if v not in parent:
                        parent[v] = u
                        next.append(v)
        frontier = next
    return parent


def getWay(parents, listFinal, userTo):
    for item in parents:
        if item == userTo:
            listFinal.append(parents[item])
            getWay(parents, listFinal, parents[item])
    return listFinal


def algorithm(parents, userTo):
    listFinal = []
    listFinal = getWay(parents, listFinal, userTo)
    if listFinal:
        listFinal.remove(None)
        listFinal.reverse()
        listFinal.append(userTo)
        return listFinal
    else:
        return []
