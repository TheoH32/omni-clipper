from abc import ABC, abstractmethod

class SocialPlatform(ABC):
    @abstractmethod
    def auth(self): pass

    @abstractmethod
    def upload(self, file_path): pass
