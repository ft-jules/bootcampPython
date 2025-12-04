class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    def __init__(self):
        self.account = []

    def add(self, account):
        if not isinstance(account, Account):
            return False
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        if not isinstance(origin, Account) or not isinstance(dest, Account):
            return False
        if self.is_corrupted(origin) or self.is_corrupted(dest):
            return False
        if amount < 0 or origin.value < amount:
            return False
        origin.transfer(-amount)
        dest.transfer(amount)

    def fix_account(self, account):
        if not isinstance(account, Account):
            return False
        if not self.is_corrupted(account):
            return True
        attrs = account.__dict__
        keys_to_delete = [key for key in attrs if key.startswith('b')]
        for key in keys_to_delete:
            delattr(account, key)
        if not ('zip' in attrs or 'addr' in attrs):
            account.zip = "00000"
        if 'name' not in attrs or not isinstance(attrs['name'], str):
            account.name = "fixed Account"
        if 'id' not in attrs or not isinstance(attrs['id'], int):
            account.id = Account.ID_COUNT
            Account.ID_COUNT += 1
        if 'value' not in attrs or not isinstance(attrs['value'], (int, float)):
            account.value = 0
        if len(attrs) % 2 != 0:
            account.padding_fix = None
        if self.is_corrupted(account):
            return False
        return True

    def is_corrupted(self, account):
        attrs = account.__dict__
        if len(attrs) % 2 != 0:
            return True
        for key in attrs:
            if key.startswith('b'):
                return True
        if not ('name' in attrs and 'id' in attrs and 'value' in attrs):
            return True
        if not isinstance(account.name, str):
            return True
        if not isinstance(account.id, int):
            return True
        if not isinstance(account.value, (int, float)):
            return True
        return False