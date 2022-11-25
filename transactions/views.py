from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from utils import handle_file
from .models import Transaction


def upload(request):
    if request.method == "POST":
        file_uploaded = request.FILES["document"]

        database = FileSystemStorage()
        database.save(file_uploaded.name, file_uploaded)

        transactions = handle_file.transactions(f"upload/{file_uploaded}")

        for transaction in transactions:
            Transaction.objects.create(**transaction)

        return redirect("/api/transactions")

    return render(request, "upload.html")


def show_transactions(req):
    card_transactions = Transaction.objects.values(
        "type",
        "date",
        "value",
        "cpf",
        "card",
        "hour",
        "owner_shop",
        "shop",
    )

    total = handle_file.sum(card_transactions)

    return render(
        req,
        "show_transactions.html",
        context={"card_transactions": card_transactions, "total": total},
    )
