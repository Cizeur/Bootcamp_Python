class Account():
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank():
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def get_account_by_id(self, account_id):
        for account in self.account:
            if not hasattr(account, "id"):
                self.fix_account(account)
            if account.id == account_id:
                return account
        return None

    def get_account_by_name(self, account_name):
        counter = 0
        for account in self.account:
            if not hasattr(account, "name"):
                self.fix_account(account)
            if account.name == account_name:
                counter += 1
                output = account
        if counter == 1:
            return output
        return None

    def transfer(self, origin, dest, amount):
        if isinstance(origin, str):
            origin = self.get_account_by_name(origin)
        elif isinstance(origin, int):
            origin = self.get_account_by_id(origin)
        else:
            return False
        if isinstance(dest, str):
            dest = self.get_account_by_name(dest)
        elif isinstance(dest, int):
            dest = self.get_account_by_id(dest)
        else:
            return False
        if not origin or not dest:
            return False
        if isinstance(amount, int):
            amount = float(amount)
        if not isinstance(amount, float) or amount < 0:
            return False
        if origin.value < amount:
            return False
        origin.transfer(-1.0 * amount)
        dest.transfer(amount)
        return True

    def fix_account(self, account):
        if not hasattr(account, "id"):
            setattr(account, "id", Account.ID_COUNT)
            Account.ID_COUNT += 1
        att = [a for a in dir(account) if not callable(getattr(account, a))]
        to_rem = [key for key in att if key.startswith("b")]
        for elm in to_rem:
            delattr(account, elm)
        if not any(key.startswith("zip") for key in att):
            setattr(account, "zip", "42042")
        if not any(key.startswith("addr") for key in att):
            setattr(account, "addr", "There")
        if "name" not in att:
            setattr(account, "name", "Unknown " + str(account.id))
        if "value" not in att:
            setattr(account, "value", 0)

    def __repr__(self):
        string = "< Bank class : "
        for account in bank.account:
            self.fix_account(account)
            string += "{name:" + account.name + ", id: "\
                + str(account.id) + ", value: "\
                + str(account.value) + "}"
        string += ">"
        return string


if __name__ == '__main__':
    ac1 = Account("joe", bank="royal bank")
    ac2 = Account("billy", bank="royal bank")
    ac3 = Account("billy", bank="royal bank")
    ac4 = Account("remy", bank="royal bank")
    ac3.value = 10000
    ac4.value = 10000
    bank = Bank()
    bank.add(ac1)
    bank.add(ac2)
    bank.add(ac3)
    bank.add(ac4)
    delattr(ac2, "id")
    ac1.value = 1000
    print(ac2.__dict__)
    bank.fix_account(ac2)
    print(ac2.__dict__)
    ac2.value = 10000
    print(ac1.id)
    if bank.transfer("remy", "billy", 10):
        print("Success")
    print(bank)
