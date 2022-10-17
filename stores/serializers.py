import ipdb
from rest_framework import serializers
from rest_framework.views import Request, Response, status

from stores.models import Store


class StoreSerializer(serializers.ModelSerializer):

    transactions = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = "__all__"
        read_only_fields = ["id", "transactions"]

    def get_transactions(self, obj: Store):

        transactions = obj.transactions.all()

        transaction_type = []
        value = 0

        for item in transactions:
            if item.type == ("2") or item.type == ("3") or item.type == ("9"):
                transaction_type.append(item.type)
                value = value - item.value
            else:
                transaction_type.append(item.type)
                value = value + item.value

        return {"total": round(value, 2), "transactions": transaction_type}