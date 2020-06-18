from django.core.management.base import BaseCommand

from market.models import Category, SubCategory, Company
from market.management.commands.load_cat import Command

import requests
from bs4 import BeautifulSoup as bs
#import lxml
import shutil
from prj.settings import BASE_DIR
from django.core.files import File


class CommandFirm(BaseCommand):

    def handle(self, *args, **options):
        print('Clearing DB ...')
        # удаляем записи и картинки
        Category.objects.all().delete()
        SubCategory.objects.all().delete()
        Company.objects.all().delete()
        try:
            shutil.rmtree('%s/media' % BASE_DIR)
        except FileNotFoundError:
            pass

        # парсим главную страницу
        base_url = 'https://west-info.biz/katalog-predpriyatij/'
        print(f'Start import from {base_url}')
        res = requests.get(base_url)
        soup = BeautifulSoup(rez.text, 'html.parser')

        # находим нужный контент
        categories = soup.findAll('li', {'class': 'submenu_item'})
        for it in categories[:5]:
            c = Category()
            c.name = it.find('a').text
            c.save()
            print(f'Import {c.name}')
            subcategories = it.findAll('a', {'class': 'sub2menu_link'})
            for kat in subcategories:
                sub = SubCategory()
                sub.name = kat.text
                sub.category = c
                sub.save()
                print(f'Import {sub.name}')              
                new_url = f"https://west-info.biz/katalog-predpriyatij{k['href']}"
                catalog = requests.get(new_url)
                new_soup = bs(catalog.text, 'html.parser')
                div = new_soup.findAll('div', {'class': 'teaser-item'})
                for item in div:
                    firm_name = item.find('h2', {'class': 'pos-title'})
                    firm_description = item.find('p')
                    firm_city = item.find('div', {'class': 'element element-text'})
                    firm_adress = item.findAll('div', {'class': 'element element-text'})
                    firm_phones = item.find('div', {'class': 'element element-text last'})
                    a = item.findAll('img')
                    for link in a:
                        print(link['src'])

                    if firm_phones:
                        phones_list = firm_phones.text.replace(' ', '').replace(',', ' ').replace(';', ' ').split()
                    com = Company()
                    if firm_name:
                        com.name = firm_name.text
                    if firm_description:
                        com.description = firm_description.text
                    if firm_city:
                        com.city = firm_city.text
                    if firm_adress and len(firm_adress) >= 2:
                        com.adress = firm_adress[1].text
                    else:
                        com.adress = '-'
                    
                    for z in phones_list:
                        com.phone = p
                    com.category = c
                    com.sub_category = sub
                    com.save()
                    print(f'{com.name} save...')
       