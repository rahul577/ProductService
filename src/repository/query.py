import os
import json

class query:

    def getProduct(self, productId):
        requiredProduct = {}
        file = open('../repository/data.json', 'r')
        products = json.load(file)
        for product in products:
            if product['productId'] == productId:
                requiredProduct = product
        file.close()
        return requiredProduct

    def addProduct(self, newProduct):
        file = open('../repository/data.json', 'r')
        data = json.load(file)
        file.close()
        index = -1
        for idx, product in enumerate(data):
            if product['productId'] == newProduct['productId']:
                index = idx
        if index != -1:
            data.pop(index)
        data.append(newProduct)
        data = json.dumps(data)
        file = open('../repository/data.json', 'w')
        file.write(data)
        file.close()
        return data