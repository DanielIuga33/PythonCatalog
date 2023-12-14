from Domain.DisciplineValidator import DisciplineValidator
from Domain.StudentValidator import StudentValidator
from Repository.repoDiscipline import RepoDiscipline
from Repository.repoDispStudNota import RepoDispStudNota
from Repository.repoStudent import RepoStudent
from Service.serviceDiscipline import ServiceDiscipline
from Service.serviceDispStudNota import ServiceDispStudNota
from Service.serviceStudent import ServiceStudent
from Tests.TestsDiscipline import test_all_discipline
from Tests.TestsStudent import test_all_student
from UI.userInterface import Ui


def main():
    repo_stud = RepoStudent("Files/Students")
    stud_val = StudentValidator()
    srv_stud = ServiceStudent(repo_stud, stud_val)

    repo_disp = RepoDiscipline("Files/Disciplines")
    disp_val = DisciplineValidator()
    srv_disp = ServiceDiscipline(repo_disp, disp_val)

    repo_dsn = RepoDispStudNota("Files/DSN")
    srv_dsn = ServiceDispStudNota(repo_dsn)

    ui = Ui(srv_stud, srv_disp, srv_dsn)

    ui.run_menu()


if __name__ == '__main__':
    test_all_student()
    test_all_discipline()
    main()
