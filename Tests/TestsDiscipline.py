from Domain.Discipline import Discipline
from Domain.DisciplineValidator import DisciplineValidator
from Repository.repoDiscipline import RepoDiscipline
from Service.serviceDiscipline import ServiceDiscipline


def test_discipline():
    disp = Discipline("1", "Math", "Einstein")

    assert disp.get_id() == "1"
    assert disp.get_name() == "Math"
    assert disp.get_teacher() == "Einstein"


def test_repository():
    repo = RepoDiscipline("Test")

    disp1 = Discipline("1", "Math", "Einstein")
    disp2 = Discipline("2", "English", "Iohanis")
    disp3 = Discipline("3", "Biology", "Rabbit")
    disp4 = Discipline("4", "History", "Lincoln")
    assert repo.get_size() == 0
    repo.add(disp1)
    assert repo.get_size() == 1
    repo.add(disp2)
    assert repo.get_size() == 2
    assert repo.get_all()[0] == disp1
    repo.delete(1)
    assert repo.get_size() == 1
    repo.add(disp3)
    assert repo.get_size() == 2
    repo.add(disp4)
    repo.add(disp1)
    assert repo.get_size() == 4
    assert repo.get_all()[3] == disp1
    repo.delete(0)
    repo.delete(0)
    repo.delete(0)
    repo.delete(0)


def test_service():
    repo = RepoDiscipline("Test")
    val = DisciplineValidator()
    srv = ServiceDiscipline(repo, val)

    assert srv.get_size() == 0
    srv.add("1", "Math", "Einstein")
    srv.add("4", "History", "Lincoln")
    srv.add("2", "English", "Iohanis")
    srv.add("3", "Biology", "Rabbit")
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


def test_all_discipline():
    test_discipline()
    test_repository()
    test_service()
