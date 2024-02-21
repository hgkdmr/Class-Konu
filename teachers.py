class teacher:
    teachers_list = []  #Öğretmenleri listelemek için

    def __init__(self,name,surname,age,lesson):
        self.name = name 
        self.surname = surname
        self.age = age 
        self.lesson = lesson
        self.teachers_list.append(self) #Yeni bir öğretmen eklemek için

    def show_info(self):
        print(f"Ad:{self.name} Soyad:{self.surname} Yaş:{self.age} Ders:{self.lesson}")  #instance method

    def onvacation(self):
        print(f"{self.name} is on vacation")

    @classmethod                                        #classmethod olmadan kod çalışmıyor
    def add_teacher(cls, name, surname, age, lesson):
        new_teacher = cls(name, surname, age, lesson)  # Yeni bir öğretmen nesnesi oluşturuyoruz.
        print(f"{new_teacher.name} {new_teacher.surname} {new_teacher.age} {new_teacher.lesson} is added to the teacher list.")    

teacher1 = teacher("Filiz","Doğan",38,"Tarih")
teacher1.show_info()
teacher2 = teacher("Osman","Deniz",45,"Kimya")
teacher2.show_info()
teacher3 =teacher("Defne","Ülkü",50,"Edebiyat")
teacher3.show_info()
teacher3.onvacation()
teacher4 =teacher("Tuğba","Tosun",30,"İngilizce")
teacher4.show_info()

teacher.add_teacher("Alev", "İkinci", 30, "Matematik")
