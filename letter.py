class Letter:
    def __init__(self, content, recipient):
        """
        Letter object that contains a content string.
        
        :param content: string
        """
        self.content = content
        self.read = False
        self.recipient = recipient
        self.encryption_status = False

    def mark_as_read(self):
        """
        Sets read to True.
        """
        self.read = True

    def encrypt(self):
        self.encryption_status = True

    def decrypt(self):
        self.encryption_status = False

    def check_if_readable(self):
        """
        Returns bool of the readability status of the letter (if it is encrypted or marked as read).

        :return: bool
        """
        if not self.encryption_status and not self.read:
            return True

        else:
            return False
