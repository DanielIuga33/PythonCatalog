from Domain.Student import Student


class StudentValidator:
    def validate(self, std: Student):
        errors = []
        if std.get_name() == "":
            errors.append("Name cannot be Null")
        if std.get_surname() == "":
            errors.append("Surname cannot be Null")
        if errors:
            raise ValueError(errors)
