
class Student:

    def __init__(self, name="michael jordan", student_id=23):
        self.name = name
        self.student_id = student_id


    def __str__(self):
        return "{}'s number is: {}".format(self.name, self.student_id)
