from DB.ProductDBModelAdapter import ProductDBModelAdapter
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    product_1 = {'Store': 'Ghana', 'Brand': 'Drink', 'Name': 'Heineken Can 330ml (6 Pack)', 'Price': 90,
                 'Currency': 'GHS'}
    product_2 = {'Store': 'Ghana', 'Brand': 'Water', 'Name': 'Voltic 500ml Bottled Water (Pack of 15)', 'Price': 25,
                 'Currency': 'GHS'}
    product_3 = {'Store': 'Ghana', 'Brand': 'Bulk-Store', 'Name': 'Phoenix Jewel Thai Fragrant Rice (5 x 5 kg)',
                 'Price': 90, 'Currency': 'GHS'}
    product_4 = {'Store': 'Ghana', 'Brand': 'Drink', 'Name': 'Heineken Can 330ml (6 Pack)', 'Price': 120,
                 'Currency': 'GHS'}
    product_5 = {'Store': 'Ghana', 'Brand': 'Bulk-Store', 'Name': 'Lele Rice 5x5 Kg', 'Price': 90, 'Currency': 'GHS'}
    product_6 = {'Store': 'Ghana', 'Brand': 'Bulk-Store', 'Name': 'Phoenix Jewel Thai Fragrant Rice (5 x 5 kg)',
                 'Price': 390, 'Currency': 'GHS'}

    def show_products(self):
        product_db_model_adapter = ProductDBModelAdapter()
        products = product_db_model_adapter.get_products()
        print(products)

    def run_tests(self):
        product_db_model_adapter = ProductDBModelAdapter()

        self.show_products()

        results_1 = product_db_model_adapter.merge_products(self.product_1)
        self.show_products()

        results_2 = product_db_model_adapter.merge_products(self.product_2)
        self.show_products()

        results_3 = product_db_model_adapter.merge_products(self.product_3)
        self.show_products()

        results_4 = product_db_model_adapter.merge_products(self.product_4)
        self.show_products()

        results_5 = product_db_model_adapter.merge_products(self.product_5)
        self.show_products()

        results_6 = product_db_model_adapter.merge_products(self.product_6)
        self.show_products()


if __name__ == '__main__':
    unittest.main()
