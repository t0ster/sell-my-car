import json

import mechanize


br = mechanize.Browser()
br.open('http://auto.ria.ua/ajax.php?target=auto&event=load_subcategory&host=&category_id=1&marka_id=0&modelId=0&targetId=modelId&sourceId=markaId&lang_id=2&catCon=1&zone=add_auto')
makes = json.loads(br.response().get_data())
# [{u'count': u'24524',
#   u'eng': u'mercedes-benz',
#   u'main_category': u'1',
#   u'marka_id': u'48',
#   u'name': u'Mercedes'}]
make = [make for make in makes['markaArr'] if 'Mercedes' in make['name']][0]
