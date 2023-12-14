from Service.serviceDiscipline import ServiceDiscipline
from Service.serviceDispStudNota import ServiceDispStudNota
from Service.serviceStudent import ServiceStudent
import time


class Ui:
    def __init__(self, srv_stud: ServiceStudent, srv_disp: ServiceDiscipline, srv_dsn: ServiceDispStudNota):
        self.srv_stud = srv_stud
        self.srv_dp = srv_disp
        self.srv_dsn = srv_dsn

    def run_menu(self):
        while True:
            self.print_main_menu()
            option = input("Give your option: ")
            match option:
                case "1":
                    self.run_student_menu()
                case "2":
                    self.run_discipline_menu()
                case "3":
                    self.run_dsn_menu()
                case "x":
                    return
                case _:
                    print("Wrong Option...Try again")
                    time.sleep(1.5)

    def run_student_menu(self):
        while True:
            self.print_student_menu()
            option = input("Give your option: ")
            match option:
                case "1":
                    self.add_stud()
                case "2":
                    self.delete_stud()
                case "a":
                    self.show_all(self.srv_stud.get_all())
                    time.sleep(1.5)
                case "x":
                    return
                case _:
                    print("Wrong Option...Try again")
                    time.sleep(1.5)

    def run_discipline_menu(self):
        while True:
            self.print_discipline_menu()
            option = input("Give your option: ")
            match option:
                case "1":
                    self.add_disc()
                case "2":
                    self.delete_disc()
                case "a":
                    self.show_all(self.srv_dp.get_all())
                    time.sleep(1.5)
                case "x":
                    return
                case _:
                    print("Wrong Option...Try again")
                    time.sleep(1.5)

    def run_dsn_menu(self):
        while True:
            self.print_dsn_menu()
            option = input("Give your option: ")
            match option:
                case "1":
                    self.add_dsn()
                case "2":
                    self.delete_dsn()
                case "3":
                    self.sort_studs()
                case "4":
                    self.sort_studs_proc()
                case "a":
                    self.show_all_dsn_disp()
                case "a1":
                    self.show_all_dsn()
                case "x":
                    return
                case _:
                    print("Wrong Option...Try again")

    @staticmethod
    def print_main_menu():
        print("\tHello and Welcome to our Faculty !")
        print(" [1] Student Menu")
        print(" [2] Discipline Menu")
        print(" [3] DSN Menu")
        print(" [x] Leave the Application")

    @staticmethod
    def print_student_menu():
        print("\t Welcome to Student Menu")
        print(" |{1}| Add a Student")
        print(" |{2}| Delete a Student")
        print(" |{a}| Show all Students")
        print(" |{x}| Go to main menu")

    @staticmethod
    def print_discipline_menu():
        print("\t Welcome to Discipline Menu")
        print(" -{1}- Add a Discipline")
        print(" -{2}- Delete a Discipline")
        print(" -{a}- Show all Disciplines")
        print(" -{x}- Go to main menu")

    @staticmethod
    def print_dsn_menu():
        print("\t Welcome to Discipline and Notes Menu")
        print(" >{1}< Add a grade/grades to a Student")
        print(" >{2}< Delete all the grades for a student at a discipline")
        print(" >{3}< Find and sort student to a discipline")
        print(" >{4}< First n students sorted by marks average")
        print("   at all disciplines (name and mark)")
        print(" >{a}< Show all the students with marks at a specific discipline")
        print(" >{a1}< Show all DSN")
        print(" >{x}< Go to main menu")

    @staticmethod
    def show_all(lista):
        for elem in lista:
            print(elem)

    """ CRUD """

    def add_stud(self):
        i = 1
        while self.srv_stud.exists_id(str(i)):
            i = i + 1
        ids = str(i)
        name = input("Give the student name: ")
        surname = input("Give the student surname: ")
        try:
            self.srv_stud.add(ids, name, surname)
        except Exception as e:
            print(f"Errors: {e}")

    def delete_stud(self):
        self.show_all(self.srv_stud.get_all())
        ids = input("Give the id of the Student you want to delete: ")
        try:
            self.srv_stud.delete_by_id(ids)
            self.srv_dsn.delete_in_cascade_stud(ids)
        except Exception as e:
            print(f"Error: {e}")

    def add_disc(self):
        i = 1
        while self.srv_dp.exists_id(str(i)):
            i = i + 1
        ids = str(i)
        name = input("Give the name of the Discipline: ")
        teacher = input("Give the teacher's name: ")
        try:
            self.srv_dp.add(ids, name, teacher)
        except Exception as e:
            print(f"Error: {e}")

    def delete_disc(self):
        self.show_all(self.srv_dp.get_all())
        idd = input("Give the id of the Discipline you want to delete: ")
        try:
            self.srv_dp.delete_by_id(idd)
            self.srv_dsn.delete_in_cascade_disp(idd)
        except Exception as e:
            print(f"Error: {e}")

    def add_dsn(self):
        try:
            self.show_all(self.srv_dp.get_all())
            idd = input("Give the id of the Discipline: ")
            if not self.srv_dp.exists_id(idd):
                print("There is no Discipline with this id !")
                return
            self.show_all(self.srv_stud.get_all())
            ids = input("Give the id of the Student: : ")
            if not self.srv_stud.exists_id(ids):
                print("There is no Student with this id !")
                return
            no_grades = int(input("How many grades do you want to add: "))
            if no_grades < 0 or no_grades > 20:
                print("Invalid number of grades !")
                return
            for i in range(0, no_grades):
                mark = int(input("Give here the grade: "))
                if mark < 0 or mark > 10:
                    print("Invalid grade !")
                    continue
                self.srv_dsn.add(idd, ids, mark)
        except Exception as e:
            print(f"Error: {e}")

    def delete_dsn(self):
        idd = input("Give the id of the Discipline: ")
        if not self.srv_dp.exists_id(idd):
            print("There is no Discipline with this id !")
            return
        ids = input("Give the id of the Student you want to delete: ")
        if not self.srv_stud.exists_id(ids):
            print("There is no Student with this id !")
            return
        self.srv_dsn.delete(idd, ids)

    def show_all_dsn(self):
        for elem in self.srv_dsn.get_all():
            print(f"Discipline: [id={self.srv_dp.find_discipline_by_id(elem[0]).get_id()}]->"
                  f"{self.srv_dp.find_discipline_by_id(elem[0]).get_name()},  "
                  f"Student: [id={self.srv_stud.find_student_by_id(elem[1]).get_id()}]->"
                  f"{self.srv_stud.find_student_by_id(elem[1]).get_name()} "
                  f"{self.srv_stud.find_student_by_id(elem[1]).get_surname()}, "
                  f"Grade: {elem[2]}")
        time.sleep(1.5)

    def show_all_dsn_disp(self):
        self.show_all(self.srv_dp.get_all())
        idd = input("Enter the id of the discipline: ")
        for elem in self.srv_dsn.get_all():
            if elem[0] == idd:
                print(f"Student: [id={self.srv_stud.find_student_by_id(elem[1]).get_id()}]->"
                      f"{self.srv_stud.find_student_by_id(elem[1]).get_name()} "
                      f"{self.srv_stud.find_student_by_id(elem[1]).get_surname()}, "
                      f"Grade: {elem[2]}")
        time.sleep(1.5)

    """CRUD END"""

    """FUNCTIONALITATI"""

    def sort_studs(self):
        i = 0
        for idd in self.srv_dsn.get_disc_with_studs():
            print(f"{self.srv_dp.find_discipline_by_id(idd)}, Number of students with grades:"
                  f" {self.srv_dsn.no_studs_for_a_discipline()[i]}")
            i += 1
        idd = input("Give the id of the Discipline: ")
        if not self.srv_dp.exists_id(idd):
            print("There is no Discipline with this id !")
            return
        option = input(" [1] Sort by grades \n [2] Sort by name \n Give your option: ")
        if option == "1":
            lista = self.srv_dsn.sort_by_mark(idd)
            for elem in lista:
                print(f"id: {elem[0]}, name: {self.srv_stud.find_student_by_id(elem[0]).get_surname()}"
                      f" {self.srv_stud.find_student_by_id(elem[0]).get_name()},"
                      f" Average = {elem[1]}")
        elif option == "2":
            lista = self.srv_dsn.find_studs_to_discipline(idd, 2)
            result = []
            for elem in lista:
                result.append(self.srv_stud.find_student_by_id(elem).get_name())
            for elem in sorted(result):
                print(self.srv_stud.find_student_by_name(elem))
        time.sleep(1.5)

    def sort_studs_proc(self):
        try:
            studs = self.srv_dsn.first_20pr_studs_by_avg()
            nr = int(input(f"Give the number of students you want see the results (max is {len(studs)}): "))
            if nr < 1 or nr > len(studs):
                print("Invalid number of students entered !")
                return
            for i in range(0, nr):
                std = self.srv_stud.find_student_by_id(studs[i][0])
                print(f"Student: [id={std.get_id()}]->"
                      f"{std.get_name()}"
                      f" {std.get_surname()}, "
                      f"Grade: {studs[i][1]}")
            time.sleep(1.5)
        except Exception as e:
            print(e)

    """FUNCTIONALITATI END"""
