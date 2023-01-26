from Address import Address
from ClassIndex import ClassIndex
from Db import Db
from Phone import Phone
from Status import Status
from Student import Student


class Infrastructure:

    db = Db()

    db.addresses.append(Address(1, "Энергетиков"))
    db.addresses.append(Address(2, "Ленина"))
    db.addresses.append(Address(3, "Воровского"))
    db.addresses.append(Address(4, "Степана Разина"))
    db.addresses.append(Address(5, "Победы"))
    db.addresses.append(Address(6, "Аношкина"))
    db.addresses.append(Address(7, "Чичерина"))
    db.addresses.append(Address(8, "Молодогвардейцев"))
    db.addresses.append(Address(9, "Шота Руставели"))
    db.addresses.append(Address(10, "Гагарина"))
    db.addresses.append(Address(11, "Дзержинского"))
    db.addresses.append(Address(12, "Бажова"))
    db.addresses.append(Address(13, "Кулибина"))
    db.addresses.append(Address(14, "Сергея Герасимова"))
    db.addresses.append(Address(15, "Жукова"))

    db.statuses.append(Status(1, "Отличник"))
    db.statuses.append(Status(2, "Ударник"))
    db.statuses.append(Status(3, "Троечник"))
    db.statuses.append(Status(4, "Двоечник"))

    db.classes.append(ClassIndex(1, "5А"))
    db.classes.append(ClassIndex(2, "6А"))
    db.classes.append(ClassIndex(3, "7Б"))
    db.classes.append(ClassIndex(4, "9А"))

    db.phones.append(Phone(1, "89270569009"))
    db.phones.append(Phone(2, "89271189845"))
    db.phones.append(Phone(3, "89379797230"))
    db.phones.append(Phone(4, "89093313065"))
    db.phones.append(Phone(5, "88005553535"))
    db.phones.append(Phone(6, "89276222498"))
    db.phones.append(Phone(7, "89119012450"))
    db.phones.append(Phone(8, "89678087775"))
    db.phones.append(Phone(9, "89878209939"))
    db.phones.append(Phone(10, "89272291788"))

    db.students.append(Student(1, "Буханова Жанна", "2010", 1, 1, 1, 1))
    db.students.append(Student(2, "Волков Никита", "2006", 2, 2, 4, 2))
    db.students.append(Student(3, "Голева Алина", "2009", 3, 3, 2, 3))
    db.students.append(Student(4, "Емельянов Арсений", "2008", 4, 1, 3, 4))
    db.students.append(Student(5, "Казакова Надежда", "2010", 5, 2, 1, 5))
    db.students.append(Student(6, "Морозова Ольга", "2006", 6, 3, 4, 6))
    db.students.append(Student(7, "Неклюдова Мария", "2009", 7, 1, 2, 7))
    db.students.append(Student(8, "Поляков Данил", "2008", 8, 2, 3, 8))
    db.students.append(Student(9, "Сковородская Карина", "2008", 9, 3, 3, 9))
    db.students.append(Student(10, "Тараканов Артём", "2006", 10, 1, 4, 10))
    db.students.append(Student(id=11, name="Василий Пупкин"))

    def getAllInfo(self, idStudent: int):
        if idStudent < len(self.db.students):
            for i in range(len(self.db.students)):
                if self.db.students[i].getId() == idStudent:
                    s = self.db.students[i]
                    print(f"{s.getId()} "
                          f"{s.getName()} "
                          f"{s.getBirthYear()} "
                          f"{self.db.addresses[s.getAddress()].getStreetName()} "
                          f"{self.db.statuses[s.getStatus()].getStatus()} "
                          f"{self.db.classes[s.getClassIndex()].getIndex()} "
                          f"{self.db.phones[s.getPhone()].getPhone()}")
        else:
            print("Неверный Id.")

    def showBirthYear(self, year: str):
        print("Ученики запрашиваемого года рождения:")
        for i in range(len(self.db.students)):
            if year in self.db.students[i].getBirthYear():
                self.getAllInfo(self.db.students[i].getId())

    def showAddress(self, addressId: int):
        print("Ученики проживающие по запрашиваемой улице:")
        for i in range(len(self.db.students)):
            if self.db.students[i].getAddress() == addressId:
                self.getAllInfo(self.db.students[i].getId())

    def showStatus(self, statusId: int):
        print("Ученики запрашиваемой успеваемости:")
        for i in range(len(self.db.students)):
            if self.db.students[i].getStatus() == statusId:
                self.getAllInfo(self.db.students[i].getId())

    def showClass(self, classId: int):
        print("Ученики запрашиваемого класса:")
        for i in range(len(self.db.students)):
            if self.db.students[i].getClassIndex() == classId:
                self.getAllInfo(self.db.students[i].getId())
