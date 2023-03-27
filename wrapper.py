import json
import requests

from requests.exceptions import HTTPError

class EDRWrapper:
    # init with endpoint
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get_collection_by_id(self, collection_id: str) -> json:
        url = '/'.join([self.endpoint, "collections", collection_id])
        res = requests.get(url)

        # succeed
        if res.status_code == 200:
            return res

        else:
            raise HTTPError(f'An error occured: {res}')