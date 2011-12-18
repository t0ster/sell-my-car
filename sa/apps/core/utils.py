# -*- coding: utf-8 -*-
import re
import json

import mechanize

br = mechanize.Browser()


# login('wtf@bravetstudio.com', '19891010')
def login(login, password):
    br.open("http://auto.ria.ua/?target=login")
    br.select_form(nr=1)
    br["email"] = login
    br["password"] = password
    br.submit()


def post_ad():
    # Step 1
    br.open('http://auto.ria.ua/add_auto.html')
    br.select_form(nr=1)
    br['stateId'] = ['10-10']  # Регион Киев

    # Тип транспорта
    br.form.find_control("categoryId").readonly = False
    br['categoryId'] = '1'  # Легковые
    # br['categoryId'] = '2'  # Мото
    # br['categoryId'] = '3'  # Водный транспорт
    # br['categoryId'] = '4'  # Спецтехника
    # br['categoryId'] = '5'  # Прицепы
    # br['categoryId'] = '6'  # Грузовики
    # br['categoryId'] = '7'  # Автобусы
    # br['categoryId'] = '8'  # Автодома
    # br['categoryId'] = '9'  # Воздушный транспорт

    br['markaId'] = ['48']  # Марка
    mechanize.Item(br.form.find_control('modelId'), attrs={'value': '422'})
    br['modelId'] = ['422']  # Модель
    # br['version'] = 'Wtf'  # Версия
    # br['VIN'] = '123456'  # VIN

    # Коробка передач
    br.form.find_control('gearId').set_value_by_label(['Автомат'])
    # br.form.find_control('gearId').set_value_by_label(['Адаптивная'])
    # br.form.find_control('gearId').set_value_by_label(['Вариатор'])
    # br.form.find_control('gearId').set_value_by_label(['Ручная / Механика'])
    # br.form.find_control('gearId').set_value_by_label(['Типтроник'])

    # Тип привода
    br.form.find_control('driveId').get(label='Задний').selected = True
    # br.form.find_control('driveId').set_value_by_label(['Передний'])
    # br.form.find_control('driveId').set_value_by_label(['Полный'])

    br['yers'] = ['2010']  # Год выпуска
    br['race'] = '10'  # Пробег
    br['price'] = '20000'  # Цена

    br.submit()

    # Step 2
    br.select_form(nr=1)
    br.submit()

    # Step 3
    # For some reason can't complete last step, ad remains draft
    # url = "%s/type/1/period/7" % br.geturl()
    # br.open(url)


def get_make_id(make):
    def find_make(crawled_makes, make):
        for _make in make.split('-'):
            crawled_make = find_in_list_of_dicts(crawled_makes['markaArr'], 'name', _make)
            if crawled_make:
                break
        assert crawled_make, "No such make"
        return crawled_make

    br.open('http://auto.ria.ua/ajax.php?target=auto&event=load_subcategory&host=&category_id=1&marka_id=0&modelId=0&targetId=modelId&sourceId=markaId&lang_id=2&catCon=1&zone=add_auto')
    crawled_makes = json.loads(br.response().get_data())
    crawled_make = find_make(crawled_makes, make)
    return crawled_make['marka_id']


def get_model_id(make_id, model):
    def find_model(crawled_models, model):
        for _model in model.split('-'):
            crawled_model = find_in_list_of_dicts(crawled_models['modelArr'], 'name', _model)
            if crawled_model:
                break
        if not crawled_model:
            match = re.match('\w{1,3}?(\d+)', 'S600')
            if match:
                _model = match.group(1)
            crawled_model = find_in_list_of_dicts(crawled_models['modelArr'], 'name', _model)
        assert crawled_model, "No such model"
        return crawled_model

    br.open('http://auto.ria.ua/ajax.php?target=auto&event=load_subcategory&host=&category_id=1&marka_id=%s&modelId=0&targetId=modelId&sourceId=markaId&lang_id=2&zone=add_auto' % make_id)
    crawled_models = json.loads(br.response().get_data())
    crawled_model = find_model(crawled_models, model)
    return crawled_model['model_id']


def find_in_list_of_dicts(list_, key, text):
    try:
        res = [m for m in list_ if text in m[key]][0]
    except IndexError:
        res = None
    return res
