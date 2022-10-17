import uuid

from django.db import models


class Transaction(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.CharField(max_length=1)
    date = models.DateField()
    value = models.FloatField()
    hour = models.TimeField()
    card = models.CharField(max_length=12)

    store = models.ForeignKey(
        "stores.Store", related_name="transactions", on_delete=models.CASCADE
    )