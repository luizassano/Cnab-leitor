import ipdb
from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from stores.models import Store
from stores.serializers import StoreSerializer
from utils.format_data import format_data
from utils.format_list_to_obj import format_list_to_obj

from transactions.models import Transaction


def upload(request: Request):
    if request.method == "POST":
        uploaded_file = request.FILES["file"]

        file = format_data(uploaded_file)
        obj = format_list_to_obj(file)

        for item in obj:
            store_obj = {
                "store_name": item["store_name"],
                "store_owner": item["store_owner"],
                "cpf": item["cpf"],
            }
            transaction_obj = {
                "type": item["type"],
                "value": item["value"],
                "date": item["date"],
                "card": item["card"],
                "hour": item["hour"],
            }

            store, _ = Store.objects.get_or_create(**store_obj)

            transaction = Transaction(**transaction_obj, store=store)
            transaction.save()

    return render(request, "cnab.html")


class TransactionView(APIView):
    def get(self, request):
        store = Store.objects.all()

        serializer = StoreSerializer(store, many=True)

        return Response(serializer.data, status.HTTP_200_OK)