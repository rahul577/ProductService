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
            self.userInstance.sendNotificationUsingGenre(newGenres, "")

            # check if new provider is added
            newProviders = list(set(product['providers']) - set(existingProduct['providers']) )
            self.userInstance.sendNotificationUsingProvider(newProviders, product['productId'], "")
        else:
            self.userInstance.sendNotificationUsingGenre(product['genres'], "")
        return self.queryInstance.addProduct(product)