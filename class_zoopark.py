# бахнули обычный класс и его экземпляры 
# class animal:
#     def __init__(self,aName,aSpeed):
#         self.name=aName
#         self.speed=aSpeed
#         print("Creating class object")


#     def time_passing(self):
#         messege_one="Задай длину трасы в км для %s"% (self.name)
#         length=int(input(messege_one))
#         time=length/self.speed
#         print("%s , пробежал дистанцию %d км за %d s" %(self.name,length, time))



# animal_one=animal("лев",12)
# animal_two=animal("Выдра",15)
# animal_tree=animal("Медоед",50)

# print(animal_one.name)
# print(animal_two.speed)

# animal_one.time_passing()

# animal_two.time_passing()

# animal_tree.time_passing()


# Пробуем реализовать основыне концепции ООП Инкапсуляцию, Наследование, Полимофизм

class distans_trass:
    def __init__(self,Adistance):
        self.distans=Adistance
    

class Animals(distans_trass):
    def __init__(self,Aname,Aspeed,Adistance):
        super().__init__(Adistance)
        self.name=Aname
        self.speed=Aspeed
        self.distans
    def run(self):
        resald=self.distans/self.speed
        print (resald)



class lion(Animals):
    _name="Лев"
    mnochitel_speed=1.5

    def run(self):
        resald=(self.mnochitel_speed * self.speed)/self.distans
        print(self._name,resald)

class honey_badger(Animals):
    _name="медоед"
    mnochitel_speed=0.5

    def run(self):
        resald=(self.mnochitel_speed * self.speed)/self.distans
        print(self._name,resald)



animal_one=lion("Лпро",50,100)
animal_two=honey_badger("ысс",50,100)

animal_one.run()
animal_two.run()