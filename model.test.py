import unittest
import model


class LedgerTest(unittest.TestCase):
    def setUp(self):
        self.ledger = model.Ledger()
        self.userA = model.User('A')
        self.userB = model.User('A')
        self.userC = model.User('A')

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


if __name__ == "__main__":
    unittest.main()
