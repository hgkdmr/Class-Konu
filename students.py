class student:
    students_list = []   #Öğrenci listeleme

    def __init__(self,name,surname,lesson,score):
        self.name = name
        self.surname = surname
        self.lesson = lesson
        self.score = score 
        self.students_list.append(self)   #Yeni öğrenci ekleme

    def show_info(self):
        print(f"Ad:{self.name} Soyad:{self.surname} Ders:{self.lesson} Puan:{self.score}")   #instance method

    def successful(self):
        print(f"{self.name} is successful")

    @classmethod
    def add_student(cls, name, surname, lesson, score):         #classmetod olmadan kod çalışmıyor.
        new_student =cls(name, surname, lesson, score) 
        print(f"{new_student.name} {new_student.surname} {new_student.lesson} {new_student.score} is added to the student list.")

student1 = student ("Gizem","Bener","Tarih",74)
student1.show_info()
student1.successful()
student2 = student("Görkem","Yavuz","Edebiyat",90)
student2.show_info()
student2.successful()
student3 = student("Özgür","Duman","İngilizce",88)
student3.show_info()
student3.successful()

student.add_student("Beril","Yılmaz","Matematik",65)
student.add_student("Ayşe", "Yücel","Felsefe",55)
