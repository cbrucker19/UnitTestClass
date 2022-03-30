class Student:
    def __init__(self, lname, fname, major, gpa = 0.0):
        self.lastname = lname
        self.firstname = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.lastname + "," + self.firstname + " has major " + self.major + " with gpa: " + str(self.gpa)
