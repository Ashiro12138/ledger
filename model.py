import uuid
import time


class User:
    def __init__(self, name):
        self._id = str(uuid.uuid4())
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def __repr__(self):
        return f"({self._name}, {self._id})"


class Ledger:
    def __init__(self):
        self._transactions = list()

    def add_transaction(self, giver, receiver, amount):
        self._transactions.append({
            "time_stamp": time.time(),
            "giver": giver,
            "receiver": receiver,
            "amount": amount
        })

    def get_transactions(self):
        return self._transactions

    def get_net_summary(self):
        net_dict = dict()
        for transaction in self.get_transactions():
            net_dict[transaction["giver"]] = net_dict.get(transaction["giver"], 0) - transaction["amount"]
            net_dict[transaction["receiver"]] = net_dict.get(transaction["receiver"], 0) + transaction["amount"]
        return net_dict


def main():
    jason = User("Jason")
    chris = User("Chris")
    thomas = User("Thomas")

    ledger = Ledger()
    ledger.add_transaction(jason, chris, 7)
    ledger.add_transaction(jason, thomas, 10)
    ledger.add_transaction(thomas, chris, 25)
    ledger.add_transaction(chris, jason, 3)
    print('Transactions')
    print(ledger.get_transactions())
    print('Net Summary')
    print(ledger.get_net_summary())


if __name__ == "__main__":
    main()
