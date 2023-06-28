from django.test import TestCase


class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    # def test_about(self):
    #     response = self.client.get('/about/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(
    #         '''Привет, мы команда VIA MOTO VIAMOTO это мотосервис, магазин мото запчастей,
    #         расходных материалов и аксессуаров для мотоциклов, скутеров, квадроциклов, снегоходов,
    #         масла и фильтры для лодочных моторов, гидроциклов. Доставка по всей России
    #         а так-же большой выбор шлемов, маек, футболок, пирсинга, колец, сувенирной и подарочной продукции.
    #         Вкуснейший итальянский кофе, сэндвичи.''',
    #         response.content.decode())
    #
