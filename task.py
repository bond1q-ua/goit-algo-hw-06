from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name=None):
        if name is None:
            raise ValueError
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        if len(phone) != 10:
            raise ValueError
        super().__init__(phone)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = list()

    def add_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return
        raise ValueError

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError

    def __str__(self):
        return f'Record(Name: {self.name} Phones: {self.phones})'

    def __repr__(self):
        return f'Record(Name: {self.name} Phones: {self.phones})'


class AddressBook(UserDict):
    def add_record(self, record: Record):
        name = record.name.value
        self.data.update({name: record})

    def find(self, name):
        return self.get(name)

    def delete(self, name):
        del self[name]


viktor = Record('Viktor')
viktor.add_phone('9999988812')

addressBook = AddressBook()
addressBook.add_record(viktor)

maria = Record('Maria')
maria.add_phone('8888877721')

addressBook.add_record(maria)

print(addressBook.find('Viktor'))
print(addressBook.find('Maria'))