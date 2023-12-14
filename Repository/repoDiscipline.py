from Domain.Discipline import Discipline


class RepoDiscipline:
    def __init__(self, filename):
        self.__filename = filename
        self.__repo = self.__read()

    def __read(self):
        with open(self.__filename, "r") as f:
            lines = f.read()
        if len(lines) == 0:
            return []
        result = []
        lines = lines.split("\n")
        for line in lines:
            line = line.split("~")
            if len(line) > 1:
                dp = Discipline(line[0], line[1], line[2])
                result.append(dp)
        return result

    def __write(self):
        with open(self.__filename, "w") as f:
            for elem in self.get_all():
                f.write(f"{elem.get_id()}~{elem.get_name()}~{elem.get_teacher()}\n")

    def get_all(self):
        return self.__repo

    def get_size(self):
        return len(self.__repo)

    def add(self, disp: Discipline):
        self.__repo.append(disp)
        self.__write()

    def delete(self, poz):
        self.__repo.pop(poz)
        self.__write()


