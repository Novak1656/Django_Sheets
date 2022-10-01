import os
import gspread
import requests
from bs4 import BeautifulSoup
from celery import shared_task
from .models import SheetData
from django.conf import settings
from datetime import datetime


# Задача на получение и изменение данных в базе данных, которая вызывается каждую минуту
@shared_task
def get_sheet_data():
    # Подключение к сервису
    ser_acc = gspread.service_account(filename=os.path.join(settings.BASE_DIR, 'service_account.json'))
    # Получение листа с данными
    sheets = ser_acc.open('test')
    worksheet = sheets.sheet1
    # Определение количества записей в листе и получение данных полей листа
    cols = worksheet.row_count
    orders = worksheet.get(f'B2:B{cols}')
    prices_dol = worksheet.get(f'C2:C{cols}')
    shipment_dates = worksheet.get(f'D2:D{cols}')
    # Формирование кортежа с данными листа: ( ([orders], [prices_dol], [shipment_dates]), )
    sheet_data = tuple(zip(orders, prices_dol, shipment_dates))
    # Удаление текущих данных из базы данных
    SheetData.objects.all().delete()

    for num, data_row in enumerate(sheet_data):
        order = data_row[0][0]
        price_dol = float(data_row[1][0])
        shipment_date = datetime.strptime(data_row[2][0], "%d.%m.%Y").date()
        # Получение цены в рублях с учётом курса доллара
        price_rub = float(price_dol) * float(get_dollar_course())
        # Сохранение данных в таблицу базы данных
        SheetData.objects.create(
            number=num + 1,
            order=order,
            price_dol=price_dol,
            price_rub=price_rub,
            shipment_date=shipment_date
        )


# Функция получения текущего курса доллара
def get_dollar_course():
    resp = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    data = resp.content
    soup = BeautifulSoup(data, "xml")
    result = soup.find("Valute", {"ID": "R01235"})
    dollar = result.Value.text
    dollar_result = float(dollar.replace(',', '.'))
    return dollar_result
