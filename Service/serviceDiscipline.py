from Domain.Discipline import Discipline
from Domain.DisciplineValidator import DisciplineValidator
from Repository.repoDiscipline import RepoDiscipline


class ServiceDiscipline:
    def __init__(self, repo: RepoDiscipline, val: DisciplineValidator):
        self.__repo = repo
        self.__val = val
    def add(self, ids, name, teacher):
        disp = Discipline(ids, name, teacher)
        self.__val.validate(disp)
        self.__repo.add(disp)

    def delete(self, poz):
        self.__repo.delete(poz)

    def delete_by_id(self, ids):
        poz = self.find_poz_by_id(ids)
        self.__repo.delete(poz)

    def exists_id(self, ids):
        for elem in self.get_all():
            if elem.get_id() == ids:
                return True
        return False

    def find_poz_by_id(self, ids):
        if self.exists_id(ids):
            for i in range(0, self.get_size()):
                if self.get_all()[i].get_id() == ids:
                    return i
        else:
            raise ValueError("There is no entity with this id !")

    def find_discipline_by_id(self, ids):
        if self.exists_id(ids):
            for elem in self.get_all():
                if elem.get_id() == ids:
                    return elem

    def get_all(self):
        return self.__repo.get_all()

    def get_size(self):
        return self.__repo.get_size()
