from security.services.encyption.encryption_service_ABC import EncryptionServiceABC


class EncryptionServiceMock(EncryptionServiceABC):

    def encrypt(self, text_to_encrypt):
        return text_to_encrypt
