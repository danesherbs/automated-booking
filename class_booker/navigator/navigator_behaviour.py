from abc import ABC, abstractmethod


class NavigatorBehaviour(ABC):

    @abstractmethod
    def login(self, username, password):
        pass

    @abstractmethod
    def book_class(self, details):
        pass
