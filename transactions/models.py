from django.db import models
import uuid


class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.CharField(max_length=1)
    date = models.CharField(max_length=8)
    value = models.IntegerField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.CharField(max_length=6)
    owner_shop = models.CharField(max_length=14)
    shop = models.CharField(max_length=19)
