
class Student:
    def __init__(self, name, course, email):
        self.name = name
        self.course = course
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "course": self.course,
            "email": self.email
        }
