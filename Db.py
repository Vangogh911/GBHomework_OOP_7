from typing import List
from Address import Address
from ClassIndex import ClassIndex
from Phone import Phone
from Status import Status
from Student import Student


class Db:
    def __init__(self, students: List[Student] = [Student()], addresses: List[Address] = [Address()], statuses: List[Status] = [Status()], classes: List[ClassIndex] = [ClassIndex()], phones: List[Phone] = [Phone()]):
        self.students = students
        self. addresses = addresses
        self.statuses = statuses
        self.classes = classes
        self.phones = phones
