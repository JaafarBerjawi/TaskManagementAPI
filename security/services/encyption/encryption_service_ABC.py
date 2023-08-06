from abc import ABC, abstractmethod


class EncryptionServiceABC(ABC):
    @abstractmethod
    def encrypt(self, text_to_encrypt):
        pass
