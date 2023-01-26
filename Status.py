class Status:
    def __init__(self, id=0, status="None"):
        self.__id = id
        self.__status = status

    def getStatus(self):
        return self.__status
