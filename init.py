# -*- coding: utf-8 -*-
import urllib.request
import datetime
from xml.etree import ElementTree as ET


def get_exchange_rate():
    """Получает значения доллара и евро в рублях на время запуска. Данные берутся с сайта ЦБР. Возвращает значение доллара в рублях, евро в рублях, дату."""

    id_dollar = "R01235"
    id_evro = "R01239"
    id_yuan = "R01375"
    valuta = ET.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req"))

    for line in valuta.findall('Valute'):
        id_v = line.get('ID')
        if id_v == id_dollar:
            rub_dollar = line.find('Value').text
        if id_v == id_evro:
            rub_evro = line.find('Value').text
        if id_v == id_yuan:
            rub_yuan = line.find('Value').text
    today = datetime.date.today()
    return rub_dollar.replace(',', '.'), rub_evro.replace(',', '.'), rub_yuan.replace(',', '.'), today


if __name__ == "__main__":
    get_exchange_rate()

