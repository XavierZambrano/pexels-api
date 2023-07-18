class Collection:
    def __init__(self, json_collection):
        self.__collection = json_collection
    @property
    def id(self):
        return int(self.__collection["id"])
    @property
    def title(self):
        return int(self.__collection["title"])
    @property
    def description(self):
        return int(self.__collection["description"])
    @property
    def private(self):
        return self.__collection["private"]
    @property
    def media_count(self):
        return self.__collection["media_count"]
    @property
    def photos_count(self):
        return self.__collection["photos_count"]
    @property
    def videos_count(self):
        return self.__collection["videos_count"]
