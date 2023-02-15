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

    def add_transaction(self, giver: User, receiver: User, amount: float):
        self._transactions.append({
            "time_stamp": time.time(),
            "type": "transaction",
            "giver": giver,
            "receiver": receiver,
            "amount": amount
        })

    def get_transactions(self) -> list[dict]:
        return self._transactions

    def get_net_summary(self) -> dict:
        net_dict = dict()
        for transaction in self.get_transactions():
            if transaction["type"] == 'transaction':
                net_dict[transaction["giver"]] = net_dict.get(
                    transaction["giver"], 0) - transaction["amount"]
                net_dict[transaction["receiver"]] = net_dict.get(
                    transaction["receiver"], 0) + transaction["amount"]
        return net_dict


def main():
    pass


if __name__ == "__main__":
    main()
