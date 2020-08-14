
class Student:

    def __init__(self):
        self.name = "michael jordan"
        self.student_id = 23


    def __str__(self):
        return "{}'s number is: {}".format(self.name, self.student_id)
