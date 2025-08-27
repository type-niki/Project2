# Base class
class PersonalTimetable:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = [] 

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added for {self.owner}.")

    def view_tasks(self):
        print(f"\n{self.owner}'s Timetable:")
        for task in self.tasks:
            print(f"- {task}")


# Subclass
class StudentTimetable(PersonalTimetable):
    def __init__(self, owner, course):
        super().__init__(owner)
        self.course = course

    # Polymorphism: override view_tasks
    def view_tasks(self):
        print(f"\n{self.owner}'s Timetable ({self.course} Student):")
        for task in self.tasks:
            print(f"- {task}")


# Example usage
p1 = PersonalTimetable("Renne")
p1.add_task("Morning Run")
p1.add_task("Doctor Appointment")
p1.view_tasks()

s1 = StudentTimetable("Renne", "Computer Science")
s1.add_task("Data Structures Lecture")
s1.add_task("Lab Session")
s1.view_tasks()
