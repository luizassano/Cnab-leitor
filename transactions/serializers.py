import ipdb
from rest_framework import serializers
from stores.serializers import StoreSerializer

from transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"