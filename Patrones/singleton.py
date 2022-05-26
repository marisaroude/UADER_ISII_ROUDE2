#!/usr/python
#*--------------------------------------------------
#* singleton.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------
from textblob import TextBlob
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...
    def getid(self):
        eb1=TextBlob("My Unique ID")
        return print(eb1.translate(from_lang="in",to="es"))

if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        eb2=TextBlob("Singleton works, both variables contain the same instance.")
        print(eb2.translate(from_lang="in",to="es")) #Traductor 
        print()
        print(s1.getid())
    else:
        eb3=TextBlob("Singleton failed, variables contain different instances.")
        print(eb3.translate(from_lang="in",to="es")) #Traductor 


