#*--------------------------------------------------
#* proxy.py
#* excerpt from https://refactoring.guru/design-patterns/proxy/python/example
#*--------------------------------------------------

from abc import ABC, abstractmethod
from textblob import TextBlob


class Subject(ABC):
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """

    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    """
    The RealSubject contains some core business logic. Usually, RealSubjects are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the RealSubject's code.
    """

    def request(self) -> None:
        eb1=TextBlob("RealSubject: Handling request.")
        print(eb1.translate(from_lang="in",to="es"))


class Proxy(Subject):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.
        """

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        eb2=TextBlob("Proxy: Checking access prior to firing a real request.")
        print(eb2.translate(from_lang="in",to="es"))
        return True

    def log_access(self) -> None:
        eb3=TextBlob("Proxy: Logging the time of request.")
        print(eb3.translate(from_lang="in",to="es"), end="")        


def client_code(subject: Subject) -> None:
    """
    The client code is supposed to work with all objects (both subjects and
    proxies) via the Subject interface in order to support both real subjects
    and proxies. In real life, however, clients mostly work with their real
    subjects directly. In this case, to implement the pattern more easily, you
    can extend your proxy from the real subject's class.
    """

    # ...

    subject.request()

    # ...


if __name__ == "__main__":
    eb4=TextBlob("Client: Executing the client code with a real subject:")
    print(eb4.translate(from_lang="in",to="es"))    
    real_subject = RealSubject()
    client_code(real_subject)

    print("")
    
    eb5=TextBlob("Client: Executing the same client code with a proxy:")
    print(eb5.translate(from_lang="in",to="es"))   
    proxy = Proxy(real_subject)
    client_code(proxy)

    print("")

