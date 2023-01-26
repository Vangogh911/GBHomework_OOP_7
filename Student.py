class Student:
    def __init__(self, id=0, name="None", birthYear="None", address=0, status=0, classIndex=0, phone=0):
        self.__id = id
        self.__address = address
        self.__name = name
        self.__birthYear = birthYear
        self.__status = status
        self.__classIndex = classIndex
        self.__phone = phone

    def getId(self):
        return self.__id

    def getAddress(self):
        return self.__address

    def getName(self):
        return self.__name

    def getBirthYear(self):
        return self.__birthYear

    def getStatus(self):
        return self.__status

    def getClassIndex(self):
        return self.__classIndex

    def getPhone(self):
        return self.__phone
