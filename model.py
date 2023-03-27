"""
Self use template
"""

from typing import Dict

# Dao for Post
class DTO:
    __slots__ = ['id_'] # json string

    # init val
    def __init__(self, id_: str) -> None:
        self.id_ = id_

    # map value to json
    def to_dict(self) -> Dict:
        return {attr: getattr(self, attr) for attr in self.__slots__}