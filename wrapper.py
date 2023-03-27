import json
import requests
from requests.exceptions import HTTPError

class EDRWrapper:

    # init with endpoint
    def __init__(self, endpoint, collectionId = None, instanceId = None):
        self.endpoint = endpoint
        self.collectionId = collectionId
        self.instanceId = instanceId
        self.collection_options = ["instances", "position", "radius", "area", "cube", "trajectory", "corridor", "items", "locations"]

    def set_CollectionId(self, collectionId: str):
        self.collectionId = collectionId

    def set_InstanceId(self, instanceId: str):
        self.instanceId = instanceId

    def help(self):
        functions = ["get_Collection(input_collectionId: Optional, query_option: Optional)", "get_Instance(query_option: str, input_collectionId: Optional, input_instanceId: Optional)",
                     "get_CollectionItem_byId(itemId: str)", "get_CollectionLocation_byId(locId: str)", "set_CollectionId(collectionId: str)", "set_InstanceId(instanceId: str)"]
        print(functions)
        print("query_options: ",  self.collection_options)

    def helper_Request(self, url) -> json:
        res = requests.get(url)

        # succeed
        if res.status_code == 200:
            return res

        else:
            raise HTTPError(f'An error occured: {res}')

    def helper_Option(self, isCollection, option):
        if isCollection:
            url = '/'.join([self.endpoint, "collections", self.collectionId, option])
        else:
            url = '/'.join([self.endpoint, "collections", self.collectionId, "instance", self.instanceId, option])
        return self.helper_request(url)

    def get_Collection(self, input_collectionId = None, option = None) -> json:

        if not self.collectionId or not input_collectionId:
            raise ValueError("Please type collection id.")

        # using stored collection id if exist else using user input
        self.collectionId = input_collectionId if input_collectionId else self.collectionId

        # check if user request valid specific collection queries
        if option in self.collection_options:
            return self.helper_Option(True, option)
        elif option:
            raise ValueError("Please type valid queries.")

        url = '/'.join([self.endpoint, "collections", self.collectionId])
        return self.helper_Request(url)

    def get_Instance(self, option: str, input_collectionId = None, input_instanceId= None) -> json:

        if not self.collectionId or not input_collectionId:
            raise ValueError("Please type collection id.")
        if not self.instanceId or not input_instanceId:
            raise ValueError("Please type instance id.")

        # using stored id if exist else using user input
        self.collectionId = input_collectionId if input_collectionId else self.collectionId
        self.instanceId = input_instanceId if input_instanceId else self.instanceId

        # check if user request valid specific instance queries
        if option in self.collection_options:
            return self.helper_option(False, option)
        else:
            raise ValueError("Please type valid queries.")

    def get_CollectionItem_byId(self, itemId: str) -> json:
        url = '/'.join([self.endpoint, "collections", "items", itemId])
        return self.helper_request(url)

    def get_CollectionLocation_byId(self, locId: str) -> json:
        url = '/'.join([self.endpoint, "collections", "locations", locId])
        return self.helper_request(url)
