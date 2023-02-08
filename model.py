import uuid
import time
from pprint import pprint


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
            "type": "transaction",
            "giver": giver,
            "receiver": receiver,
            "amount": amount
        })

    def add_payment(self, payer, participants, amount, individual_amounts):
        if amount < sum(individual_amounts):
            raise Exception("Individual amounts does not add up to total amount")
        self._transactions.append({
            "time_stamp": time.time(),
            "type": "payment",
            "payer": payer,
            "participants": participants,
            "amount": amount,
            "individual_amounts": individual_amounts
        })

    def add_even_payment(self, payer, participants, amount):
        self._transactions.append({
            "time_stamp": time.time(),
            "type": "shared_payment",
            "payer": payer,
            "participants": participants,
            "amount": amount
        })

    def get_transactions(self):
        return self._transactions

    def get_net_summary(self):
        net_dict = dict()
        for transaction in self.get_transactions():
            if transaction["type"] == 'transaction':
                net_dict[transaction["giver"]] = net_dict.get(transaction["giver"], 0) - transaction["amount"]
                net_dict[transaction["receiver"]] = net_dict.get(transaction["receiver"], 0) + transaction["amount"]
            if transaction["type"] == 'payment':
                total_amount = transaction["amount"]
                net_dict[transaction["payer"]] = net_dict.get(transaction["payer"], 0) - total_amount
                for participant, individual_amount in zip(transaction["participants"],
                                                          transaction["individual_amounts"]):
                    net_dict[participant] = net_dict.get(participant, 0) + individual_amount
            if transaction["type"] == 'shared_payment':
                portion_amount = transaction["amount"] / (len(transaction["participants"]) + 1)
                net_dict[transaction["payer"]] = net_dict.get(transaction["payer"], 0) - (
                        portion_amount * len(transaction["participants"]))
                for participant in transaction["participants"]:
                    net_dict[participant] = net_dict.get(participant, 0) + portion_amount
        return net_dict


def main():
    jason = User("Jason")
    chris = User("Chris")
    thomas = User("Thomas")

    print(f"{'New Ledger':-^80}")
    ledger = Ledger()
    ledger.add_transaction(jason, chris, 7)
    ledger.add_transaction(jason, thomas, 10)
    ledger.add_transaction(thomas, chris, 25)
    ledger.add_transaction(chris, jason, 3)
    print('Transactions')
    pprint(ledger.get_transactions())
    print('Net Summary')
    pprint(ledger.get_net_summary())
    print()

    print(f"{'New Ledger':-^80}")
    ledger = Ledger()
    ledger.add_even_payment(chris, [jason, thomas], 25)
    ledger.add_even_payment(chris, [jason, thomas], 25)
    ledger.add_even_payment(chris, [jason, thomas], 25)
    print('Transactions')
    pprint(ledger.get_transactions())
    print('Net Summary')
    pprint(ledger.get_net_summary())
    print()


if __name__ == "__main__":
    main()
