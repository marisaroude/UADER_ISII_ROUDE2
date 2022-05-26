from __future__ import annotations
from abc import ABC, abstractmethod
from textblob import TextBlob


class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """
        eb=TextBlob("Context: Transition to")
        print(eb.translate(from_lang="in",to="es"),f"{type(state).__name__}")
        
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""


class ConcreteStateA(State):
    def handle1(self) -> None:
        eb1=TextBlob("Concrete State A handles request1.")
        print(eb1.translate(from_lang="in",to="es")) #Traductor 
        eb2=TextBlob("Concrete State A wants to change the state of the context.")
        print(eb2.translate(from_lang="in",to="es")) #Traductor 
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        eb3=TextBlob("Concrete State A handles request2.")
        print(eb3.translate(from_lang="in",to="es")) #Traductor 



class ConcreteStateB(State):
    def handle1(self) -> None:
        eb4=TextBlob("Concrete State B handles request1.")
        print(eb4.translate(from_lang="in",to="es")) #Traductor 

    def handle2(self) -> None:
        eb5=TextBlob("Concrete State B handles request2.")
        print(eb5.translate(from_lang="in",to="es")) #Traductor 
        eb6=TextBlob("Concrete State B wants to change the state of the context.")
        print(eb6.translate(from_lang="in",to="es")) #Traductor 
        self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    # The client code.

    context = Context(ConcreteStateA())
    context.request1()
    context.request2()
