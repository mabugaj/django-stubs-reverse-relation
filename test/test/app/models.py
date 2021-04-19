from django.db import models


class Transaction(models.Model):
    def test(self) -> None:
        print(self.transactionlog_set)

class TransactionLog(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
