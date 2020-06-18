from django.core.management.base import BaseCommand

from market.models import Category, SubCategory

import requests
from bs4 import BeautifulSoup as bs
#import lxml
import shutil
from prj.settings import BASE_DIR
from django.core.files import File



class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Clearing DB ...')
        # удаляем записи и картинки
        Category.objects.all().delete()
        SubCategory.objects.all().delete()
        try:
            shutil.rmtree('%s/media' % BASE_DIR)
        except FileNotFoundError:
            pass

        # парсим главную страницу
        base_url = 'https://west-info.biz/katalog-predpriyatij/'
        print(f'Start import from {base_url}')
        res = requests.get(base_url)
        soup = bs(res.text, 'html.parser')

        # находим нужный контент
        content = soup.find('ul', {'class': 'submenu'})
        for item in content.findAll('li',{'class':'submenu_item'}):
            c = Category()
            c.name = item.find('a').text
            c.save()
            print(f'Import {c.name}')
            subcategories = item.findAll('a', {'class': 'sub2menu_link'})
            for k in subcategories:
                sub = SubCategory()
                sub.name = k.text
                sub.category = c
                sub.save()
                print(f'Import {sub.name}')
    