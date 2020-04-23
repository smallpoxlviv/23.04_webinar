from abc import ABC


class AbstractParent(ABC):

    def random_method(self):
        raise NotImplementedError


class Mother:
    def init(self, age):
        self.age = age
        print("mother cons")

    def do_work(self):
        print("do work")

    def do_house_work(self):
        print("do house")


class Father(AbstractParent):
    def init(self):
        print("father cons")

    def play_guitar(self):
        print("play guitar")

    def do_house_work(self):
        print("do house by mother")


class Daughter(Mother, Father):
    def init(self, age = 0):
        Father.init(self)
        Mother.init(self, age = age)

    def random_method(self):
        print("yep")

    def do_work(self):
        print("work as horse")
        
    def ask_for_a_walk(self):
        print("can I go for a walk with Bogdan Shwadchack?")


class Friend:
    pass


def greet_mother(mother : Mother):
    print("hello ")
    mother.do_work()


def greet_father(father : Father):
    print("beer ")
    father.do_work()


if __name__ == "__main__":

    daughter = Daughter()
    #daughter.class = Friend
    greet_father(daughter)
    greet_mother(daughter)
    daughter.do_house_work()
    daughter.ask_for_a_walk()
    
    for x in [daughter]:
        x.do_work()
    
    #list
    povtorka_list = ["math", "programming", "superprice"]
      
    #tuple      
    vasian = ("11 y/o", 12, 3.14, daughter)
    
    #set
    my_set = {23, 11, 10, 10, "call"}
    print(my_set)
    
    #frozen set
    another_set = frozenset(["di_", "mi", "do"])
    
    #dictionary
    my_dict = {1: "first", "2": 123, (1,2,3):"tuple_as_a_key"}
    
    
    
    
    
    
    