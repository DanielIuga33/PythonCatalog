from dataclasses import dataclass


@dataclass
class Discipline:
    __id_entity: str
    __name: str
    __teacher: str

    def __str__(self):
        return f"id: {self.get_id()}, name: {self.get_name()}, teacher: {self.get_teacher()}"

    def __eq__(self, other):
        return (self.get_id() == other.get_id() and
                self.get_name() == other.get_name() and
                self.get_teacher() == other.get_teacher())
    def get_id(self):
        return self.__id_entity

    def get_name(self):
        return self.__name

    def get_teacher(self):
        return self.__teacher

