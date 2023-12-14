from Domain.Discipline import Discipline


class DisciplineValidator:
    def validate(self, dp: Discipline):
        errors = []
        if dp.get_name() == "":
            errors.append("Name cannot be Null !")
        if dp.get_teacher() == "":
            errors.append("Teacher name cannot be Null !")
        if errors:
            raise ValueError(errors)
