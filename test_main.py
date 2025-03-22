from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import datetime
import pandas as pd
import time


hotels = ['Отель Карелия', 'Отель Фрегат', 'Piter Inn', 'Гостиница Северная', 'Гостиница Cosmos']
dates = []
prices = {
    'Отель Карелия': {'ostrovok': [], 'yandex': []},
    'Отель Фрегат': {'ostrovok': [], 'yandex': []},
    'Piter Inn': {'ostrovok': [], 'yandex': []},
    'Гостиница Северная': {'ostrovok': [], 'yandex': []},
    'Гостиница Cosmos': {'ostrovok': [], 'yandex': []}
}

sources = ['ostrovok', 'yandex']

def test_open_ostrovok(driver, start_date, end_date):

    # driver = webdriver.Chrome()
    driver.maximize_window()

    wait = WebDriverWait(driver, 5)


    hotels = ['Отель Карелия', 'Отель Фрегат', 'Piter Inn', 'Гостиница Северная', 'Гостиница Cosmos']
    dates = []
    prices = {
        'Отель Карелия': {'ostrovok': [], 'yandex': []},
        'Отель Фрегат': {'ostrovok': [], 'yandex': []},
        'Piter Inn': {'ostrovok': [], 'yandex': []},
        'Гостиница Северная': {'ostrovok': [], 'yandex': []},
        'Гостиница Cosmos': {'ostrovok': [], 'yandex': []}
    }

    sources = ['ostrovok', 'yandex']

    # Сайт островок
    current_date = start_date
    next_day = start_date + datetime.timedelta(days=1)
    while current_date <= end_date:

        driver.get(f"https://ostrovok.ru/hotel/russia/petrozavodsk/?q=2768&dates={current_date.strftime('%d.%m.%Y')}-{next_day.strftime('%d.%m.%Y')}&guests=2&meal_types=breakfast&price=one&stars=4")
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='zen-hotels-main']"))
        )


        karelia_price = None
        try:
            # Пытаемся найти элемент по первому XPath
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Карелия')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']"))
            )
            karelia_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Карелия')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")
        except:
            try:
                # Пытаемся найти элемент по второму XPath
                wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Карелия')]//ancestor::div[contains(@class, 'zen-hotelcard-wide')]//div[@class='zen-hotelcard-rate-price-value']//span"))
                )
                karelia_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Карелия')]//ancestor::div[contains(@class, 'zen-hotelcard-wide')]//div[@class='zen-hotelcard-rate-price-value']//span")
            except:
                print("Элемент не найден по обоим путям.")


        # # Цены по отелю Карелия //a[contains(text(), 'Карелия')]//ancestor::div[contains(@class, 'zen-hotelcard-wide')]//div[@class='zen-hotelcard-rate-price-value']//span or //a[contains(text(), 'Карелия')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']
        # wait.until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, "//a[contains(text(), 'Карелия')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")
        #         or
        #         (By.XPATH, "//a[contains(text(), 'Карелия')]//ancestor::div[contains(@class, 'zen-hotelcard-wide')]//div[@class='zen-hotelcard-rate-price-value']//span")
        #     )
        # )

        # karelia_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Карелия')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")

        if karelia_price == None:
            prices['Отель Карелия']['ostrovok'].append(karelia_price)
        else:
            karelia_price_value = karelia_price.text
            karelia_price_value_fix = karelia_price_value.split()
            karelia_price_value_for_append = ' '.join(karelia_price_value_fix[:-1])
            int_karelia_price_value_for_append = int(karelia_price_value_for_append.replace(' ', ''))
            prices['Отель Карелия']['ostrovok'].append(int_karelia_price_value_for_append)

        # # Цены по отелю Фрегат
        # wait.until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, "//a[contains(text(), 'Фрегат')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")
        #     )
        # )

        fregat_price = None
        try:
            # Пытаемся найти элемент по первому XPath
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Фрегат')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']"))
            )
            fregat_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Фрегат')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")
        except:
            try:
                # Пытаемся найти элемент по второму XPath
                wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Фрегат')]//ancestor::div[contains(@class, 'zen-hotelcard-wide')]//div[@class='zen-hotelcard-rate-price-value']//span"))
                )
                fregat_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Фрегат')]//ancestor::div[contains(@class, 'zen-hotelcard-wide')]//div[@class='zen-hotelcard-rate-price-value']//span")
            except:
                print("Элемент не найден по обоим путям.")


        # fregat_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Фрегат')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")

        if fregat_price == None:
            prices['Отель Фрегат']['ostrovok'].append(fregat_price)
        else:
            fregat_price_value = fregat_price.text
            fregat_price_value_fix = fregat_price_value.split()
            fregat_price_value_for_append = ' '.join(fregat_price_value_fix[:-1])
            int_fregat_price_value_for_append = int(fregat_price_value_for_append.replace(' ', ''))
            prices['Отель Фрегат']['ostrovok'].append(int_fregat_price_value_for_append)

        # # Цены по отелю piter inn
        # wait.until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, "//a[contains(text(), 'Piter')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")
        #     )
        # )

        piter_inn_price = None
        try:
            # Пытаемся найти элемент по первому XPath
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Piter')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']"))
            )
            piter_inn_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Piter')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")
        except:
            try:
                # Пытаемся найти элемент по второму XPath
                wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Piter')]//ancestor::div[contains(@class, 'zen-hotelcard-wide')]//div[@class='zen-hotelcard-rate-price-value']//span"))
                )
                piter_inn_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Piter')]//ancestor::div[contains(@class, 'zen-hotelcard-wide')]//div[@class='zen-hotelcard-rate-price-value']//span")
            except:
                print("Элемент не найден по обоим путям.")


        # piter_inn_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Piter')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")
        if piter_inn_price == None:
            prices['Piter Inn']['ostrovok'].append(piter_inn_price)
        else:
            piter_inn_price_value = piter_inn_price.text
            piter_inn_price_fix = piter_inn_price_value.split()
            piter_inn_price_value_for_append = ' '.join(piter_inn_price_fix[:-1])
            int_piter_inn_price_value_for_append = int(piter_inn_price_value_for_append.replace(' ', ''))
            prices['Piter Inn']['ostrovok'].append(int_piter_inn_price_value_for_append)

        # # Цены по отелю Северная
        # wait.until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, "//a[contains(text(), 'Северная')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")
        #     )
        # )

        severnaya_price = None
        try:
            # Пытаемся найти элемент по первому XPath
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Северная')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']"))
            )
            severnaya_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Северная')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")
        except:
            try:
                # Пытаемся найти элемент по второму XPath
                wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Северная')]//ancestor::div[contains(@class, 'zen-hotelcard-wide')]//div[@class='zen-hotelcard-rate-price-value']//span"))
                )
                severnaya_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Северная')]//ancestor::div[contains(@class, 'zen-hotelcard-wide')]//div[@class='zen-hotelcard-rate-price-value']//span")
            except:
                print("Элемент не найден по обоим путям.")


        # severnaya_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Северная')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")

        if severnaya_price == None:
            prices['Гостиница Северная']['ostrovok'].append(severnaya_price)
        else:
            severnaya_value = severnaya_price.text
            severnaya_value_fix = severnaya_value.split()
            severnaya_price_value_for_append = ' '.join(severnaya_value_fix[:-1])
            int_severnaya_price_value_for_append = int(severnaya_price_value_for_append.replace(' ', ''))
            prices['Гостиница Северная']['ostrovok'].append(int_severnaya_price_value_for_append)

        # # Цены по отелю Cosmos
        # wait.until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, "//a[contains(text(), 'Cosmos')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")
        #     )
        # )

        cosmos_price = None
        try:
            # Пытаемся найти элемент по первому XPath
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Cosmos')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']"))
            )
            cosmos_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Cosmos')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")
        except:
            try:
                # Пытаемся найти элемент по второму XPath
                wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Cosmos')]//ancestor::div[contains(@class, 'zen-hotelcard-wide')]//div[@class='zen-hotelcard-rate-price-value']//span"))
                )
                cosmos_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Cosmos')]//ancestor::div[contains(@class, 'zen-hotelcard-wide')]//div[@class='zen-hotelcard-rate-price-value']//span")
            except:
                print("Элемент не найден по обоим путям.")


        # cosmos_price = driver.find_element(By.XPATH, "//a[contains(text(), 'Cosmos')]//ancestor::div[contains(@class, 'HotelCard-module__container--2hORD')]//span[@class='HotelCard-module__ratePriceValue--2dXPQ']")
        if cosmos_price == None:
            prices['Гостиница Cosmos']['ostrovok'].append(cosmos_price)
        else:
            cosmos_value = cosmos_price.text
            cosmos_value_fix = cosmos_value.split()
            cosmos_value_for_append = ' '.join(cosmos_value_fix[:-1])
            int_cosmos_value_for_append = int(cosmos_value_for_append.replace(' ', ''))
            prices['Гостиница Cosmos']['ostrovok'].append(int_cosmos_value_for_append)


        format_date_for_table = current_date.strftime("%d %B")
        dates.append(format_date_for_table)

        current_date += datetime.timedelta(days=1)
        next_day += datetime.timedelta(days=1)



    # сайт яндекса

    current_date_for_yandex = start_date
    next_day_for_yandex = start_date + datetime.timedelta(days=1)
    while current_date_for_yandex <= end_date:

        driver.get(f"https://travel.yandex.ru/hotels/petrozavodsk/filter-4-star/?adults=2&bbox=34.23200130238226%2C61.7344387019741~34.50040476503552%2C61.842914754566046&checkinDate={current_date_for_yandex.strftime('%Y-%m-%d')}&checkoutDate={next_day_for_yandex.strftime('%Y-%m-%d')}&childrenAges=&filterAtoms=hotel_pansion_with_offerdata%3Ahotel_pansion_breakfast_included%2Cstar%3Afour&geoId=18&lastSearchTimeMarker=1741343363529&navigationToken=0&oneNightChecked=false&searchPagePollingId=4a3dd154e29adaa14f09570fbe1e2921-0-newsearch&selectedSortId=relevant-first")
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='CWzx3']"))
        )

        # Цены по отелю Карелия

        karelia_price_yandex = None
        try:
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[contains(text(), 'Карелия')]//ancestor::div[contains(@class, 'EhCXF CQVql X-rt5 _6aDIU wU8vz qMXCQ')]//span[@class='bQcBE']")
                )
            )
            karelia_price_yandex = driver.find_element(By.XPATH, "//span[contains(text(), 'Карелия')]//ancestor::div[contains(@class, 'EhCXF CQVql X-rt5 _6aDIU wU8vz qMXCQ')]//span[@class='bQcBE']")
        except:
            print("Элемент не найден.")

        if  karelia_price_yandex == None:
            prices['Отель Карелия']['yandex'].append(karelia_price_yandex)
        else:
            karelia_price_yandex_value = karelia_price_yandex.text
            karelia_price_yandex_value_fix = karelia_price_yandex_value.split()
            karelia_price_yandex_value_for_append = ' '.join(karelia_price_yandex_value_fix)[0:-1].strip()
            int_karelia_price_yandex_value_for_append = int(karelia_price_yandex_value_for_append.replace(' ', ''))
            prices['Отель Карелия']['yandex'].append(int_karelia_price_yandex_value_for_append)

        # Цены по отелю Фрегат

        fregat_price_yandex = None

        try:
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[contains(text(), 'Фрегат')]//ancestor::div[contains(@class, 'EhCXF CQVql X-rt5 _6aDIU wU8vz qMXCQ')]//span[@class='bQcBE']")
                )
            )
            fregat_price_yandex = driver.find_element(By.XPATH, "//span[contains(text(), 'Фрегат')]//ancestor::div[contains(@class, 'EhCXF CQVql X-rt5 _6aDIU wU8vz qMXCQ')]//span[@class='bQcBE']")
        except:
            print("Элемент не найден.")

        if fregat_price_yandex == None:
            prices['Отель Фрегат']['yandex'].append(fregat_price_yandex)
        else:
            fregat_price_yandex_value = fregat_price_yandex.text
            fregat_price_yandex_value_fix = fregat_price_yandex_value.split()
            fregat_price_yandex_value_for_append = ' '.join(fregat_price_yandex_value_fix)[0:-1].strip()
            int_fregat_price_yandex_value_for_append = int(fregat_price_yandex_value_for_append.replace(' ', ''))
            prices['Отель Фрегат']['yandex'].append(int_fregat_price_yandex_value_for_append)

        # Цены по отелю piter inn

        piter_price_yandex = None

        try:
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(text(), 'Piter')]//ancestor::div[contains(@class, 'EhCXF CQVql X-rt5 _6aDIU wU8vz qMXCQ')]//span[@class='bQcBE']")
                )
            )
            piter_price_yandex = driver.find_element(By.XPATH, "//a[contains(text(), 'Piter')]//ancestor::div[contains(@class, 'EhCXF CQVql X-rt5 _6aDIU wU8vz qMXCQ')]//span[@class='bQcBE']")
        except:
            print("Элемент не найден.")

        if  piter_price_yandex == None:
            prices['Piter Inn']['yandex'].append(piter_price_yandex)
        else:
            piter_price_yandex_value = piter_price_yandex.text
            piter_price_yandex_value_fix = piter_price_yandex_value.split()
            piter_price_yandex_value_for_append = ' '.join(piter_price_yandex_value_fix)[0:-1].strip()
            int_piter_price_yandex_value_for_append = int(piter_price_yandex_value_for_append.replace(' ', ''))
            prices['Piter Inn']['yandex'].append(int_piter_price_yandex_value_for_append)

        # Цены по отелю Северная

        severnaya_price_yandex = None

        try:
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[contains(text(), 'Северная')]//ancestor::div[contains(@class, 'EhCXF CQVql X-rt5 _6aDIU wU8vz qMXCQ')]//span[@class='bQcBE']")
                )
            )
            severnaya_price_yandex = driver.find_element(By.XPATH, "//span[contains(text(), 'Северная')]//ancestor::div[contains(@class, 'EhCXF CQVql X-rt5 _6aDIU wU8vz qMXCQ')]//span[@class='bQcBE']")
        except:
            print("Элемент не найден.")

        if severnaya_price_yandex == None:
            prices['Гостиница Северная']['yandex'].append(severnaya_price_yandex)
        else:
            severnaya_price_yandex_value = severnaya_price_yandex.text
            severnaya_price_yandex_value_fix = severnaya_price_yandex_value.split()
            severnaya_price_yandex_value_for_append = ' '.join(severnaya_price_yandex_value_fix)[0:-1].strip()
            int_severnaya_price_yandex_value_for_append = int(severnaya_price_yandex_value_for_append.replace(' ', ''))
            prices['Гостиница Северная']['yandex'].append(int_severnaya_price_yandex_value_for_append)

        # Цены по отелю Cosmos

        cosmos_price_yandex = None

        try:
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(text(), 'Cosmos')]//ancestor::div[contains(@class, 'EhCXF CQVql X-rt5 _6aDIU wU8vz qMXCQ')]//span[@class='bQcBE']")
                )
            )
            cosmos_price_yandex = driver.find_element(By.XPATH, "//a[contains(text(), 'Cosmos')]//ancestor::div[contains(@class, 'EhCXF CQVql X-rt5 _6aDIU wU8vz qMXCQ')]//span[@class='bQcBE']")
        except:
            print("Элемент не найден.")

        if cosmos_price_yandex == None:
            prices['Гостиница Cosmos']['yandex'].append(cosmos_price_yandex)
        else:
            cosmos_price_yandex_value = cosmos_price_yandex.text
            cosmos_price_yandex_value_fix = cosmos_price_yandex_value.split()
            cosmos_price_yandex_value_for_append = ' '.join(cosmos_price_yandex_value_fix)[0:-1].strip()
            int_cosmos_price_yandex_value_for_append = int(cosmos_price_yandex_value_for_append.replace(' ', ''))
            prices['Гостиница Cosmos']['yandex'].append(int_cosmos_price_yandex_value_for_append)

        current_date_for_yandex += datetime.timedelta(days=1)
        next_day_for_yandex += datetime.timedelta(days=1)

    driver.quit()

    # Настройка

    excluded_hotels = ['Отель Карелия']  # Исключенные отели для нахождения среднего и процентного соотношения
    target_hotel = 'Отель Карелия'  # Название отеля для определения места
    excel_path = 'C:\\Users\\Вилле\\Desktop\\hotel_ex\\отели.xlsx'

    # Названия столбцов
    date_col = 'Дата'
    hotel_col = 'Отель'
    source_col = 'Источник'
    price_col = 'Цена'
    mean_all_hotels_col = 'Средняя цена конкурентов'
    percentage_ratio_col = 'Индекс (%)'
    hotel_rank_col = 'Позиция по цене'

    # Преобразование данных в удобный для pandas формат
    data = []
    for hotel, sources in prices.items():
        for i, date in enumerate(dates):
            for source, price_list in sources.items():
                price = price_list[i] if i < len(price_list) else None  # Проверка длины списка
                data.append({date_col: date, hotel_col: hotel, source_col: source, price_col: price})

    df = pd.DataFrame(data)

    # Удаление строк с отсутствующими ценами
    df = df.dropna(subset=[price_col])

    # Среднее значение для всех гостиниц без учета исключённых отелей
    filtered_df = df[~df[hotel_col].isin(excluded_hotels)]
    mean_values = filtered_df.pivot_table(values=price_col, columns=[date_col, source_col], aggfunc='mean')

    # Создание сводной таблицы и добавление среднего значения
    pivot_table = df.pivot_table(values=price_col, index=hotel_col, columns=[date_col, source_col], aggfunc='mean')
    if not mean_values.empty:
        pivot_table.loc[mean_all_hotels_col] = mean_values.mean()

    # Рассчитаем процентное соотношение для исключённых отелей
    for excluded_hotel in excluded_hotels:
        excluded_hotel_df = df[df[hotel_col] == excluded_hotel].pivot_table(values=price_col, index=hotel_col,
                                                                            columns=[date_col, source_col],
                                                                            aggfunc='mean')
        if excluded_hotel in excluded_hotel_df.index and not mean_values.empty:
            excluded_hotel_mean = excluded_hotel_df.loc[excluded_hotel]
            percentage_ratio = (excluded_hotel_mean / mean_values.mean()) * 100
            pivot_table.loc[percentage_ratio_col.format(excluded_hotel)] = percentage_ratio.round(2)

    # Определение места отеля по стоимости
    if target_hotel in pivot_table.index:
        ranks = []
        for col in pivot_table.columns:
            target_price = pivot_table.loc[target_hotel, col]
            other_prices = pivot_table.drop(
                [target_hotel, mean_all_hotels_col] + [percentage_ratio_col.format(h) for h in excluded_hotels],
                errors='ignore')[col]
            rank = sum(1 for p in other_prices if p is not None and target_price is not None and p < target_price) + 1
            ranks.append(f'{rank}/{len(hotels)}')
        pivot_table.loc[hotel_rank_col.format(target_hotel)] = ranks

    # Изменение порядка гостиниц на основе переменной hotels
    new_index = hotels + [mean_all_hotels_col, hotel_rank_col.format(target_hotel)]
    for excluded_hotel in excluded_hotels:
        new_index.append(percentage_ratio_col.format(excluded_hotel))
    pivot_table = pivot_table.reindex(new_index)

    # Сохранение в Excel
    pivot_table.to_excel(excel_path, sheet_name='Цены', engine='openpyxl')





