import json

class userQuery:

    def addUser(self, newUser):
        file = open('D:/hackathon/loadingService/src/repository/userData.json', 'r')
        users = json.load(file)
        file.close()
        index = -1
        for idx, user in enumerate(users):
            if user['userId'] == newUser['userId']:
                index = idx
        if index != -1:
            users.pop(index)
        users.append(newUser)
        data = json.dumps(users)
        file = open('D:/hackathon/loadingService/src/repository/userData.json', 'w')
        file.write(data)
        file.close()
        return data

    def getAllUsers(self):
        file = open('D:/hackathon/loadingService/src/repository/userData.json', 'r')
        users = json.load(file)
        file.close()
        return users

    def getUser(self, userId):
        requiredUser = {}
        file = open('D:/hackathon/loadingService/src/repository/userData.json', 'r')
        users = json.load(file)
        file.close()
        for user in users:
            if user['userId'] == userId:
                requiredUser = user
                break
        return requiredUser