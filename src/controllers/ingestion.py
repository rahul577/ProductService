from repository import query
from flask import request
from controllers.user import User
import json

class Ingestion:

    def __init__(self):
        self.queryInstance = query();
        self.userInstance = User();

    def getProduct(self):
        productId = request.form['productId']
        return self.queryInstance.getProduct(productId)

    def addProduct(self):
        productString = request.form['product']
        product = json.loads(productString)
        existingProduct = self.queryInstance.getProduct(product['productId'])
        if existingProduct:
            # check if new genres are added
            newGenres = list(set(product['genres']) - set(existingProduct['genres']) )
            if newGenres:
                self.userInstance.sendNotificationUsingGenre(newGenres, product['movieName'], product['productId'])

            # check if new provider is added
            newProviders = list(set(product['providers']) - set(existingProduct['providers']) )
            if newProviders:
                self.userInstance.sendNotificationUsingProvider(newProviders, product['productId'], product['movieName'])
        else:
            self.userInstance.sendNotificationUsingGenre(product['genres'], product['movieName'], product['productId'])
        return self.queryInstance.addProduct(product)