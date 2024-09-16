# Abstract class

from abc import ABC, abstractmethod

class SocialMediaInterface(ABC):
    @abstractmethod
    def login(self, username, password):
        pass

    @abstractmethod
    def scrap(self):
        pass