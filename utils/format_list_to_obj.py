from datetime import date, datetime, time


def format_date(str: str) -> datetime:

    return date(int(str[0:4]), int(str[4:6]), int(str[6:8]))


def format_hour(str: str) -> datetime:

    return time(int(str[0:2]), int(str[2:4]), int(str[4:6]))


def format_list_to_obj(list: list) -> object:
    obj = []

    for item in list:
        obj.append(
            {
                "type": item[0:1],
                "date": format_date(item[1:9]),
                "value": int(item[9:19]) / 100,
                "cpf": item[19:30],
                "card": item[30:42],
                "hour": format_hour(item[42:48]),
                "store_owner": item[48:62],
                "store_name": item[62:81],
            }
        )
    return obj