from Factory.WollPlatz.WollPlatzAdapter import WollPLatzAdapter
from Factory.MarketExpress.MarketExpressAdapter import MarketExpressAdapter
from Factory.LasTijerasMagicas.LasTijerasMagicasAdapter import LasTijerasMagicasAdapter

class SitesAdapterFactory:

    def __init__(self):
        self.adapters = dict (
            LasTijerasMagicas = LasTijerasMagicasAdapter(),
            #WollPlatz = WollPLatzAdapter(),
            #MarketExpress=MarketExpressAdapter(),
            #Other Website Adapters will be initialized here
        )

    def initialize_scrapping(self):
        all_products = dict()

        for site in self.adapters:
             all_products[site] = self.adapters[site].read_website_info()

        return all_products

