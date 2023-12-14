from dataclasses import dataclass


@dataclass
class Student:
    __id_entity: str
    __name: str
    __surname: str

    def __str__(self):
        return f"id: {self.__id_entity}, name: {self.__name}, surname: {self.__surname}"

    def __eq__(self, other):
        return (self.get_id() == other.get_id() and
                self.get_name() == other.get_name() and
                self.get_surname() == other.get_surname())

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_id(self):
        return self.__id_entity
