from utils.functions import transactions_data, date_conversion, datetime_conversion, get_latest_transactions, card_accaunt_masking


latest_transactions = get_latest_transactions(transactions_data)[:50] #выбираем пять последних транзакций со статусом EXECUTED

for n in latest_transactions: # Запускаем цикл по пяти выбранным транзакциям
    for m in transactions_data(): # Для каждой записи из загруженного json файла
        if datetime_conversion(m['date']) == n: # выбираем записи, соответствующие последним пяти транзакциям

            if m['description'] != "Открытие вклада": # Для всех выбранных записей, кроме операций Открытия вклада, так как для него просто создается счет
                show_from_name, show_from_number = card_accaunt_masking(m['from']) # получаем название карты или счета списания и маскированного номера
                show_to_name, show_to_number = card_accaunt_masking(m['to']) # получаем название карты или счета пополнения и маскированного номера
                show_amount = m['operationAmount']['amount'] # получаем сумму операции
                show_currency = m['operationAmount']['currency']['name'] # # получаем валюту операции
                print(f'{date_conversion(m['date'])} {m['description']}')
                print(f'{show_from_name} {show_from_number} -> {show_to_name} {show_to_number}')
                print(f'{show_amount} {show_currency}\n')
            else: # Здесь все тоже самое, только мы просто никуда не переводим, а открываем счет
                show_to_name, show_to_number = card_accaunt_masking(m['to'])
                show_amount = m['operationAmount']['amount']
                show_currency = m['operationAmount']['currency']['name']
                print(f'{date_conversion(m['date'])} {m['description']}')
                print(f'{show_to_name} {show_to_number}')
                print(f'{show_amount} {show_currency}\n')







