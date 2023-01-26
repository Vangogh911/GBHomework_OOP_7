from typing import List
from Address import Address
from ClassIndex import ClassIndex
from Phone import Phone
from Status import Status
from Student import Student


class Db:
    def __init__(self, students: List[Student] = [], addresses: List[Address] = [], statuses: List[Status] = [], classes: List[ClassIndex] = [], phones: List[Phone] = []):
        self.students = students
        self. addresses = addresses
        self.statuses = statuses
        self.classes = classes
        self.phones = phones
