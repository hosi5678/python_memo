# repr()関数は、オブジェクトの「公式な」文字列表現を返す
# __repr__()メソッドは、repr()関数によって呼び出される
# __repr__()メソッドは、オブジェクトの「公式な」文字列表現を返す
# __str__()メソッドは、str()関数によって呼び出される
# __str__()メソッドは、オブジェクトの「非公式な」文字列表現を返す
# __str__()メソッドは、print()関数によって呼び出される

class Pet:
    # def __init__(self, name, species):
    #     self.name = name
    #     self.species = species

    # def __repr__(self):
    #     return f"{self.name} is a {self.species}"

    def __init__(self,name: str,master: str)->None:
        self.__name = name
        self.__master = master
        
    def introduce(self)->None:
        print("my name is {}.".format(self.__name))
        print("my master is {}.".format(self.__master))
        
    def __str__(self)->str:
        return self.__name + "<<"+self.__master +">>"
      
    def print(self)->None:
        print(self.__str__())
        
kurt = Pet("kurt", "eye")
print(str(kurt))
