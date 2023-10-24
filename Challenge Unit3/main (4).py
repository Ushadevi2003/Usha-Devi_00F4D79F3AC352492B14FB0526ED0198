class Student:
    def __init__(self, name, roll_number ,cgpa):
      self.name=name
      self.roll_number=roll_number
      self.cgpa=cgpa
def sort_student(student_list):
  #Sort the list of students in descending order of CGPA
  sorted_students =sorted(student_list,key=lambda 
                        student:student.cgpa,reverse=True)
  return sorted_students
  students=[
    student("Hari","A124",7.8),
    student("Srikanth","A125",8.9),
    student("Mahindhar","A126",9.9),
  ]
  sorted_students =sort_students(students)
  for student in sorted_students:
    print("Name:{},Roll Number:{},CGPA:{}".format(student.name,student.roll_number,student.cgpa))
  

