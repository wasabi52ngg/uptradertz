from django.test import TestCase, Client
from .models import MenuItem

class PageAvailabilityTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.home_item, _ = MenuItem.objects.get_or_create(
            menu_name='main_menu',
            title='Главная',
            slug='home',
            url='home',
            order=0
        )

        self.about_item, _ = MenuItem.objects.get_or_create(
            menu_name='main_menu',
            title='О нас',
            slug='about',
            url='/about/',
            order=1
        )

        self.services_item, _ = MenuItem.objects.get_or_create(
            menu_name='main_menu',
            title='Услуги',
            slug='services',
            url='/services/',
            order=2
        )

    def test_menu_root_page_accessibility(self):
        """Тест доступности корневой страницы меню"""
        response = self.client.get('/menu/main_menu/')
        self.assertEqual(response.status_code, 200)

    def test_home_item_page_accessibility(self):
        """Тест доступности страницы элемента 'Главная'"""
        response = self.client.get(self.home_item.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_about_item_page_accessibility(self):
        """Тест доступности страницы элемента 'О нас'"""
        response = self.client.get(self.about_item.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_services_item_page_accessibility(self):
        """Тест доступности страницы элемента 'Услуги'"""
        response = self.client.get(self.services_item.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_menu_rendering(self):
        """Тест отображения меню"""
        response = self.client.get('/menu/main_menu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Главная')
        self.assertContains(response, 'О нас')
        self.assertContains(response, 'Услуги')