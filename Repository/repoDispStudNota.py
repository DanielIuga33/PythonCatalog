class RepoDispStudNota:
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
                lista = []
                for elem in line:
                    lista.append(elem)
                result.append(lista)
        return result

    def __write(self):
        with open(self.__filename, "w") as f:
            for elem in self.__repo:
                f.write(f"{elem[0]}~{elem[1]}~{elem[2]}\n")

    def add(self, id_dp, id_sd, nota: list):
        elem = [id_dp, id_sd, nota]
        self.__repo.append(elem)
        self.__write()

    def delete(self, poz):
        self.__repo.pop(poz)
        self.__write()

    def update(self, poz, id_dp, id_sd, nota):
        self.__repo[poz][0] = id_dp
        self.__repo[poz][1] = id_sd
        self.__repo[poz][2] = nota
        self.__write()

    def get_all(self):
        return self.__repo

    def get_size(self):
        return len(self.__repo)
