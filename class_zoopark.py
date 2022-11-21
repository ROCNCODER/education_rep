
class animal:
    def __init__(self,aName,aSpeed):
        self.name=aName
        self.speed=aSpeed
        print("Creating class object")


    def time_passing(self):
        messege_one="Задай длину трасы в км для %s"% (self.name)
        length=int(input(messege_one))
        time=length/self.speed
        print("%s , пробежал дистанцию %d км за %d s" %(self.name,length, time))



animal_one=animal("лев",12)
animal_two=animal("Выдра",15)
animal_tree=animal("Медоед",50)

print(animal_one.name)
print(animal_two.speed)

animal_one.time_passing()

animal_two.time_passing()

animal_tree.time_passing()
