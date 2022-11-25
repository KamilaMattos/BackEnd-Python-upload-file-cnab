def read_file(path):
    infos = []

    with open(path, "r", encoding="utf-8") as file:
        for info in file:
            infos.append(info)

        return infos


def split_transactions_infos(transaction):
    type = transaction[0:1]
    date = transaction[1:9]
    value = transaction[9:19]
    cpf = transaction[19:30]
    card = transaction[30:42]
    time = transaction[42:48]
    owner_shop = transaction[48:62]
    shop = transaction[62:79]
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    final_date = f"{year}/{month}/{day}"
    hour = time[0:2]
    minutes = time[2:4]
    seconds = time[4:6]
    final_hour = f"{hour}:{minutes}:{seconds}"
    value = int(value) / 100

    infos_transactions = {
        "type": type,
        "date": final_date,
        "value": value,
        "cpf": cpf,
        "card": card,
        "hour": final_hour,
        "owner_shop": owner_shop,
        "shop": shop,
    }

    return infos_transactions


def transactions(path):
    cnab_file = read_file(path)
    transactions_list = []

    for transactions in cnab_file:
        transaction = split_transactions_infos(transactions)
        transactions_list.append(transaction)

    return transactions_list


def sum(transaction_list):
    total = 0

    for transaction in transaction_list:
        if (
            transaction["type"] == "2"
            or transaction["type"] == "3"
            or transaction["type"] == "9"
        ):
            total -= transaction["value"]
        else:
            total += transaction["value"]

    return total
