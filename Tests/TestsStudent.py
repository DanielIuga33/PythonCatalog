from Domain.Student import Student
from Domain.StudentValidator import StudentValidator
from Repository.repoStudent import RepoStudent
from Service.serviceStudent import ServiceStudent


def test_student():
    student = Student("1", "Iuga", "Daniel")

    assert student.get_id() == "1"
    assert student.get_name() == "Iuga"
    assert student.get_surname() == "Daniel"


def test_repository():
    repo = RepoStudent("Test")

    student1 = Student("1", "Iuga", "Daniel")
    student2 = Student("2", "Bala", "Daniel")
    student3 = Student("3", "Vlad", "Alexandrescu")
    student4 = Student("4", "Gigi", "Becali")
    assert repo.get_size() == 0
    repo.add(student1)
    assert repo.get_size() == 1
    repo.add(student2)
    assert repo.get_size() == 2
    assert repo.get_all()[0] == student1
    repo.delete(1)
    assert repo.get_size() == 1
    repo.add(student3)
    assert repo.get_size() == 2
    repo.add(student4)
    repo.add(student1)
    assert repo.get_size() == 4
    assert repo.get_all()[3] == student1
    repo.delete(0)
    repo.delete(0)
    repo.delete(0)
    repo.delete(0)


def test_service():
    repo = RepoStudent("Test")
    val = StudentValidator()
    srv = ServiceStudent(repo, val)

    assert srv.get_size() == 0
    srv.add("1", "Iuga", "Daniel")
    srv.add("4", "Benjamin", "Franklin")
    srv.add("2", "Bala", "Daniel")
    srv.add("3", "Giovani", "Becali")
    assert srv.find_poz_by_id("4") == 1
    assert srv.exists_id("10") is False
    assert srv.get_size() == 4
    srv.delete(3)
    assert srv.exists_id("3") is False
    assert srv.exists_id("1") is True
    assert srv.get_size() == 3
    srv.delete_by_id("1")
    assert srv.exists_id("1") is False
    srv.delete(0)
    srv.delete(0)

def test_all_student():
    test_student()
    test_repository()
    test_service()

