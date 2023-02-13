#Parent Class to store course details
class Course:
    #Static variables
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office_location = "Cape Town"

    #method to print contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    #method to location details of head office
    def head_office_location(self):
        print(f"Head office location : {self.head_office_location}")

#Subclass of Class object for specific course
class OOPCourse(Course):
    #Static veriable
    course_id = 12345

    def __init__(self, description, trainer):
        #instance level variables
        self.description = description
        self.trainer = trainer

    #Method to print description and trainer of coures
    def trainer_details(self):
        print(f"Description: {self.description}\n Trainer: {self.trainer}")

    #Method to print out course ID
    def show_course_id(self):
        print(f"Course ID: {self.course_id}")

#Object of OOPCourse sublass
course_1 = OOPCourse("OOP Fundamentals", "Mr Anon A. Mouse")

#printing out Course details, trainer detials & course ID
Course.contact_details(course_1)
course_1.trainer_details()
course_1.show_course_id()