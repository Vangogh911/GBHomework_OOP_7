class Address:
    def __init__(self, id=0, streetName="None"):
        self.__id = id
        self.__streetName = streetName

    def getStreetName(self):
        return self.__streetName
