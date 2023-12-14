from Domain.Student import Student


class RepoStudent:
    def __init__(self, filename):
        self.__filename = filename
        self.__repo = self.__read()

    def __write_file(self):
        with open(self.__filename, "w") as file:
            for student in self.get_all():
                file.write(f"{student.get_id()}~{student.get_name()}~{student.get_surname()}\n")

    def __read(self):
        with open(self.__filename, "r") as file:
            lines = file.read()
        if len(lines) == 0:
            return []
        result = []
        lines = lines.split("\n")
        for line in lines:
            line = line.split("~")
            if len(line) > 1:
                stud = Student(line[0], line[1], line[2])
                result.append(stud)
        return result

    def get_all(self):
        return self.__repo

    def get_size(self):
        return len(self.__repo)

    def add(self, student: Student):
        self.__repo.append(student)
        self.__write_file()

    def delete(self, poz):
        self.__repo.pop(poz)
        self.__write_file()

    def update(self, poz, student: Student):
        self.__repo[poz] = student

