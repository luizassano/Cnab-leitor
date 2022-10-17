import uuid

from django.db import models


class Store(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)
    cpf = models.CharField(max_length=11)