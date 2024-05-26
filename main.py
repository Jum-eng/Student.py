class Student:
    def __init__(self, name, studentID):
        self.name = name
        self.studentID = studentID
        self.courseList = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setStudentID(self, studentID):
        self.studentID = studentID

    def getStudentID(self):
        return self.studentID

    def addCourse(self, course):
        self.courseList.append(course)

    def removeCourse(self, course):
        if course in self.courseList:  # check if the course is in the list before removing it
            self.courseList.remove(course)

    def displayCourses(self):
        print("Courses:")  # print out all the courses in the course list
        for course in self.courseList:  # loop through the list and print each item
            print("- " + course)


# main file
student1 = Student("Jumah", "10948795")  # create one Student object
student1.setName("Jumah Musah")  # set its attributes
student1.addCourse("Math")  # add some courses to the object
student1.addCourse("Multimedia and web designs")
student1.addCourse("Programming")
student1.removeCourse("Multimedia and web designs")  # remove some courses from the object
student1.displayCourses()  # print out the courses in the object