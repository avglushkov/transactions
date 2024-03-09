from datetime import datetime
import pytest

from utils.functions import transactions_data, date_conversion, datetime_conversion, get_latest_transactions, card_accaunt_masking

def test_date_conversion():

    assert date_conversion('2019-07-03T18:35:29.512364') == '03.07.2019'

def test_datetime_conversion():

    assert str(datetime_conversion('2019-07-03T18:35:29.512364')) == '2019-07-03 18:35:29'
    assert datetime_conversion('2019-07-03T18:35:29.512364').year == 2019
    assert datetime_conversion('2019-07-03T18:35:29.512364').month == 7
    assert datetime_conversion('2019-07-03T18:35:29.512364').day == 3
    assert datetime_conversion('2019-07-03T18:35:29.512364').hour == 18
    assert datetime_conversion('2019-07-03T18:35:29.512364').minute == 35
    assert datetime_conversion('2019-07-03T18:35:29.512364').second == 29

@pytest.fixture
def coll1():
    return get_latest_transactions([{"state": "EXECUTED","date": "2019-08-26T10:50:58.294041"},
                                    {"state": "EXECUTED","date": "2019-04-26T10:50:58.294041"},
                                    {"state": "EXECUTED","date": "2019-07-26T10:50:58.294041"}])
def test_get_latest_transactions_1(coll1):

    assert len(coll1) == 3
    assert str(coll1[0]) == "2019-08-26 10:50:58"
    assert str(coll1[1]) == "2019-07-26 10:50:58"
    assert str(coll1[2]) == "2019-04-26 10:50:58"

@pytest.fixture
def coll2():
    return get_latest_transactions([{"state": "CANCELED","date": "2019-08-26T10:50:58.294041"},
                                    {"state": "EXECUTED","date": "2019-04-26T10:50:58.294041"},
                                    {"state": "EXECUTED","date": "2019-07-26T10:50:58.294041"}])
def test_get_latest_transactions_2(coll2):

    assert len(coll2) == 2
    assert str(coll2[0]) == "2019-07-26 10:50:58"
    assert str(coll2[1]) == "2019-04-26 10:50:58"



def test_card_accaunt_masking():
    assert card_accaunt_masking('Счет 64686473678894779589')[0] == 'Счет'
    assert card_accaunt_masking('Счет 64686473678894779589')[1] == '**9589'
    assert card_accaunt_masking('Maestro 1596837868705199')[0] == 'Maestro'
    assert card_accaunt_masking('Maestro 1596837868705199')[1] == '1596 8 ** ** ** 5199'
    assert card_accaunt_masking('Visa Platinum 8990922113665229')[0] == 'Visa Platinum'
    assert card_accaunt_masking('Visa Platinum 8990922113665229')[1] == '8990 9 ** ** ** 5229'

