from repository import userQuery
from flask import request
import json
import requests

class User:

    DEEPLINK_PREFIX = "ms-windows-store://pdp/?productId="
    URL = "https://localhost:44372/NotificationService"

    def __init__(self):
        self.userQueryInstance = userQuery();

    def addGenre(self):
        userId = request.form['userId']
        genre = request.form['genre']
        existingUser = self.userQueryInstance.getUser(userId)
        if existingUser:
            if genre not in existingUser['genres']:
                existingUser['genres'].append(genre)
            return self.userQueryInstance.addUser(existingUser)
        else:
            newUser = {}
            newUser['userId'] = userId
            newUser['genres'] = [genre]
            newUser['providers'] = {}
            newUser['providers']['netflix'] = []
            newUser['providers']['prime'] = []
            return self.userQueryInstance.addUser(newUser)

    def addProviderForProduct(self):
        userId = request.form['userId']
        provider = request.form['provider']
        productId = request.form['productId']
        existingUser = self.userQueryInstance.getUser(userId)
        if existingUser:
            if productId not in existingUser['providers'][provider]:
                existingUser['providers'][provider].append(productId)
            return self.userQueryInstance.addUser(existingUser)
        else:
            newUser = {}
            newUser['userId'] = userId
            newUser['genres'] = []
            newUser['providers'] = {}
            newUser['providers']['netflix'] = []
            newUser['providers']['prime'] = []
            newUser['providers'][provider] = [productId]
            return self.userQueryInstance.addUser(newUser)

    def sendNotificationUsingGenre(self, genres, movieName, productId):
        users = self.userQueryInstance.getAllUsers()
        for user in users:
            diff = list(set(genres) & set(user['genres']))
            if diff:
                deepLink = self.DEEPLINK_PREFIX + productId
                notificationMessage = movieName + " has been added in " + ', '.join(genres)
                data = {'notificationMessage': notificationMessage, 'deepLink': deepLink}
                r = requests.post(url=self.URL, verify=False, data=data)

    def sendNotificationUsingProvider(self, providers, productId, movieName):
        users = self.userQueryInstance.getAllUsers()
        for user in users:
            for provider in providers:
                if productId in user["providers"][provider]:
                    notificationMessage = movieName + " is now available on " + provider
                    deepLink = self.DEEPLINK_PREFIX + productId
                    data = {'notificationMessage': notificationMessage, 'deepLink': deepLink}
                    r = requests.post(url=self.URL, verify=False, data=data)


