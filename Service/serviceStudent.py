from Domain.Student import Student
from Domain.StudentValidator import StudentValidator
from Repository.repoStudent import RepoStudent


class ServiceStudent:
    def __init__(self, repo: RepoStudent, std_val: StudentValidator):
        self.__repo = repo
        self.__validator = std_val

    def add(self, ids, name, surname):
        std = Student(ids, name, surname)
        self.__validator.validate(std)
        self.__repo.add(std)

    def delete(self, poz):
        self.__repo.delete(poz)

    def delete_by_id(self, ids):
        poz = self.find_poz_by_id(ids)
        self.delete(poz)

    def find_poz_by_id(self, ids):
        if self.exists_id(ids):
            for i in range(0, self.get_size()):
                if self.__repo.get_all()[i].get_id() == ids:
                    return i
        else:
            raise ValueError("There is no entity with this id !")

    def exists_id(self, ids):
        for std in self.get_all():
            if std.get_id() == ids:
                return True
        return False

    def find_student_by_id(self, ids):
        if self.exists_id(ids):
            for std in self.get_all():
                if std.get_id() == ids:
                    return std

    def find_student_by_name(self, name):
        for std in self.get_all():
            if std.get_name() == name:
                return std

    def get_all(self):
        return self.__repo.get_all()

    def get_size(self):
        return self.__repo.get_size()
