import datetime
class Person:
    def_init_(self, name, surname, middle_name, birthdate, address, telephone, email):
        self.name= name 
        self.surname =surname 
        self.middle_name = middle_name
        self.birthdate = birthdate
        self.address = address # object
        self.telephone= telephone 
        self.email =email

    def age(self):
        today=datetime.date.today()
        age =today.year -self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, selfbirthdate.day):
            age -=1

        return age

