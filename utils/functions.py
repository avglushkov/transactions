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

    result_date_list = [] # В этот список мы собираем дату из строки по отдельным символам в нужном нам формате
    result_date_list = (original_date[8] +
                        original_date[9] + "." +
                        original_date[5] +
                        original_date[6] + "." +
                        original_date[0] +
                        original_date[1] +
                        original_date[2] +
                        original_date[3])
    return ''.join(result_date_list) # из списка формируем дату в нужном формате

def datetime_conversion(original_date):
    """Конвертация времени из формата '2019-07-03T18:35:29.512364' в формат datetime, что """

    converted_date = datetime(int(original_date[0:4]), int(original_date[5:7]), int(original_date[8:10]),
                    int(original_date[11:13]), int(original_date[14:16]), int(original_date[17:19]))

    return converted_date


def get_latest_transactions(tr_data):
    """функция формирует список дат для транзакций в фомате datatime "ГГГГ-ММ-ДД ЧЧ:ММ:СС" и сортирует их от самой последней """

    trans_date = []
    for transaction in tr_data:
        if transaction['state'] == 'EXECUTED':
            trans_date.append(datetime_conversion(transaction['date']))
            trans_date = sorted(trans_date, reverse=True)
    return trans_date


def card_accaunt_masking(from_or_to_text):
    """функция маскирования номера карты"""

    if from_or_to_text[:4] != 'Счет': # если наименование в from и to не начинается со слова "Счет", то мы имеем дело с одной из карт
        card_number = from_or_to_text[-16:] # номер карты - это 16 символов с конца
        show_card_name = from_or_to_text[:-17] # для получения наименования карты, мы отбрасываем с конца номер карты и один пробел
        show_card_number = ''.join(card_number[:4] + " " + card_number[4:5] + " ** ** ** " + card_number[-4:]) # собираем маску для карты

        return show_card_name, show_card_number
    else: # Если не карта, то мы имеем дело со счетом
        accaunt_number = from_or_to_text[-20:] #номер счета состоит из 20 символов
        show_accaunt_name = from_or_to_text[:-21] # для наименования счета отбрасываем его номер и пробел
        show_accaunt_number = ''.join("**" + accaunt_number[-4:]) # собираем маску номера счета

        return show_accaunt_name, show_accaunt_number


#


