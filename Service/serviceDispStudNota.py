from Repository.repoDispStudNota import RepoDispStudNota


class ServiceDispStudNota:
    def __init__(self, repo: RepoDispStudNota):
        self.__repo = repo

    def add(self, id_dp, id_sd, nota):
        if self.exists(id_dp, id_sd):
            self.add_mark(id_dp, id_sd, nota)
            return
        self.__repo.add(id_dp, id_sd, [nota])

    def add_mark(self, id_dp, id_sd, nota: int):
        if self.exists(id_dp, id_sd):
            lista = []
            for elem in self.get_all():
                if elem[0] == id_dp and elem[1] == id_sd:
                    for el in elem[2]:
                        lista.append(el)
                    lista.append(nota)
                    self.__repo.update(self.find_poz(id_dp, id_sd), id_dp, id_sd, lista)

    def delete(self, id_dp, id_sd):
        if self.exists(id_dp, id_sd):
            self.__repo.delete(self.find_poz(id_dp, id_sd))

    def delete_in_cascade_stud(self, ids):
        for elem in self.__repo.get_all():
            if elem[1] == ids:
                self.delete(elem[0], elem[1])

    def delete_in_cascade_disp(self, ids):
        for elem in self.__repo.get_all():
            if elem[0] == ids:
                self.delete(elem[0], elem[1])

    def exists(self, id_dp, id_sd):
        for elem in self.get_all():
            if elem[0] == id_dp and elem[1] == id_sd:
                return True
        return False

    def find(self, id_dp, id_sd):
        if self.exists(id_dp, id_sd):
            for elem in self.get_all():
                if elem[0] == id_dp and elem[1] == id_sd:
                    return elem

    def find_poz(self, id_dp, id_sd):
        if self.exists(id_dp, id_sd):
            for i in range(0, self.get_size()):
                if self.get_all()[i][0] == id_dp and self.get_all()[i][1] == id_sd:
                    return i

    def calculate_average(self, lista):
        suma = 0
        if type(lista) is not list:
            lista = self.from_string_to_list(lista)
        for elem in lista:
            suma += elem
        return suma / len(lista)

    @staticmethod
    def from_string_to_list(string):
        string = string[1:len(string) - 1]
        string = string.split(",")
        result = []
        for elem in string:
            result.append(int(elem))
        return result

    def find_studs_to_discipline(self, idd, index):
        result = []
        for elem in self.get_all():
            if elem[0] == idd and elem[1] not in result:
                if index == 1:
                    result.append([elem[1], self.calculate_average(elem[2])])
                elif index == 2:
                    result.append(elem[1])
        return result

    @staticmethod
    def find_poz_max(lista):
        maxim = 0
        for i in range(0, len(lista)):
            if lista[i][1] > maxim:
                maxim = lista[i][1]
        for i in range(0, len(lista)):
            if lista[i][1] == maxim:
                return i

    @staticmethod
    def find_poz_max_normal_list(lista):
        maxim = 0
        for i in range(0, len(lista)):
            if lista[i] > maxim:
                maxim = lista[i]
        for i in range(0, len(lista)):
            if lista[i] == maxim:
                return i

    def sort_by_mark(self, idd):
        result = []
        lista = self.find_studs_to_discipline(idd, 1)
        while len(lista) > 0:
            i = self.find_poz_max(lista)
            result.append(lista[i])
            lista.pop(i)
        return result

    def get_disc_with_studs(self):
        result = []
        for elem in self.get_all():
            if elem[0] not in result:
                result.append(elem[0])
        return result

    def no_studs_for_a_discipline(self):
        result = []
        for idd in self.get_disc_with_studs():
            i = 0
            for elem in self.get_all():
                if idd == elem[0]:
                    i += 1
            result.append(i)
        return result

    def no_disciplines_for_a_stud(self, ids):
        nr = 0
        for elem in self.get_all():
            if elem[1] == ids:
                nr += 1
        return nr

    def find_average_for_every_discipline(self, ids):
        result = []
        lista = []
        for elem in self.get_all():
            if elem[1] == ids:
                lista.append(elem[2])
        for elem in lista:
            result.append(self.calculate_average(elem))
        return result

    def calculate_average_for_all_disciplines(self, ids):
        no_disciplines = self.no_disciplines_for_a_stud(ids)
        if no_disciplines == 0:
            return 0
        suma = 0
        for elem in self.find_average_for_every_discipline(ids):
            suma += elem
        return suma / no_disciplines

    def get_students_with_grades(self):
        result = []
        for ids in self.get_all():
            if ids[1] not in result:
                result.append(ids[1])
        return result

    def first_20pr_studs_by_avg(self):
        lista = []
        avg = []
        sorted_avg = []
        result = []
        studs = self.get_students_with_grades()
        for i in range(0, len(studs)):
            lista.append([studs[i], self.calculate_average_for_all_disciplines(studs[i])])
            avg.append(self.calculate_average_for_all_disciplines(studs[i]))
        while len(avg) > 0:
            i = self.find_poz_max_normal_list(avg)
            sorted_avg.append(avg[i])
            avg.pop(i)
        for i in range(0, len(sorted_avg)):
            for ids in lista:
                if ids[1] == sorted_avg[i] and ids not in result:
                    result.append(ids)
        return result

    def get_marks(self, id_dp, id_sd):
        return self.find(id_dp, id_sd)[2]

    def get_all(self):
        return self.__repo.get_all()

    def get_size(self):
        return self.__repo.get_size()
