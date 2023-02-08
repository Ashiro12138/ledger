import unittest
import model


class LedgerTest(unittest.TestCase):
    def setUp(self):
        self.ledger = model.Ledger()
        self.userA = model.User('A')
        self.userB = model.User('B')
        self.userC = model.User('C')

    def test_simple_transaction(self):
        amount = 10
        self.ledger.add_transaction(self.userA, self.userB, amount)
        transactions = self.ledger.get_transactions()
        self.assertEqual(len(transactions), 1)
        transaction = transactions[0]
        self.assertEqual(transaction.get("type"), "transaction")
        self.assertEqual(transaction.get("giver"), self.userA)
        self.assertEqual(transaction.get("receiver"), self.userB)
        self.assertEqual(transaction.get("amount"), amount)

    def test_simple_transactions(self):
        self.ledger.add_transaction(self.userA, self.userB, 10)
        self.ledger.add_transaction(self.userA, self.userC, 10)
        net_summary = self.ledger.get_net_summary()
        self.assertEqual(net_summary, {self.userA: -20, self.userB: 10, self.userC: 10})

    def test_simple_transactions2(self):
        self.ledger.add_transaction(self.userA, self.userB, 10)
        self.ledger.add_transaction(self.userB, self.userC, 10)
        net_summary = self.ledger.get_net_summary()
        self.assertEqual(net_summary, {self.userA: -10, self.userB: 0, self.userC: 10})

    def test_even_payment(self):
        self.ledger.add_even_payment(self.userA, [self.userB, self.userC], 25)
        self.ledger.add_even_payment(self.userA, [self.userB, self.userC], 25)
        self.ledger.add_even_payment(self.userA, [self.userB, self.userC], 25)
        net_summary = self.ledger.get_net_summary()
        self.assertEqual(net_summary, {self.userA: -50, self.userB: 25, self.userC: 25})

    def test_payment(self):
        self.ledger.add_payment(self.userA, [self.userB, self.userC], 50, [15, 20])
        net_summary = self.ledger.get_net_summary()
        self.assertEqual(net_summary, {self.userA: -50, self.userB: 15, self.userC: 20})


if __name__ == "__main__":
    unittest.main()