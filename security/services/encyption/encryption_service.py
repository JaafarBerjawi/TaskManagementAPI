import hashlib
from security.services.encyption.encryption_service_ABC import EncryptionServiceABC


class EncryptionService(EncryptionServiceABC):

    def encrypt(self, text_to_encrypt):
        return hashlib.sha256(text_to_encrypt.encode()).hexdigest()
