import json
from datetime import datetime

def transactions_data():
    """чтение данных о транзакциях из json файла """

    transactions = []
    with open('operations.json', 'r', encoding ="utf-8") as f:
        trans_load = f.read()
        transactions = json.loads(trans_load)
    return transactions



def date_conversion(original_date):
    """Конвертация даты из формата '2019-07-03T18:35:29.512364' в 'ДД.ММ.ГГГГ' """

    result_date_list = []
    result_date_list = (original_date[8] +
                        original_date[9] + "." +
                        original_date[5] +
                        original_date[6] + "." +
                        original_date[0] +
                        original_date[1] +
                        original_date[2] +
                        original_date[3])
    return ''.join(result_date_list)

def datetime_conversion(original_date):
    """Конвертация времени из формата '2019-07-03T18:35:29.512364' в формат datetime, что """

    return datetime(int(original_date[0:4]), int(original_date[5:7]), int(original_date[8:10]),
                    int(original_date[11:13]), int(original_date[14:16]), int(original_date[17:19]))


def get_latest_transactions(tr_data):
    """функция формирует список дат для транзакций в фомате datatime "ГГГГ-ММ-ДД ЧЧ:ММ:СС" и сортирует их от самой последней """
    trans_date = []
    for transaction in tr_data():
        if transaction['state'] == 'EXECUTED':
            trans_date.append(datetime_conversion(transaction['date']))
            trans_date = sorted(trans_date, reverse=True)
    return trans_date

def card_accaunt_masking(from_or_to_text):
    """функция маскирования номера карты"""

    if from_or_to_text[:4] != 'Счет':
        card_number = from_or_to_text[-16:]
        show_card_name = from_or_to_text[:-17]
        show_card_number = ''.join(card_number[:4] + " " + card_number[4:5] + " ** ** ** " + card_number[-4:])

        return show_card_name, show_card_number
    else:
        accaunt_number = from_or_to_text[-20:]
        show_accaunt_name = from_or_to_text[:-21]
        show_accaunt_number = ''.join("**" + accaunt_number[-4:])

        return show_accaunt_name, show_accaunt_number


#


