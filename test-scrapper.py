from Factory.SitesAdapterFactory import SitesAdapterFactory
from DB.ProductDBModelAdapter import ProductDBModelAdapter

import pandas as pd

adapter_factory = SitesAdapterFactory()

site_products = adapter_factory.initialize_scrapping()

for site in site_products:
    df = pd.DataFrame(site_products[site])
    df.to_csv('{}_comparison.csv'.format(site))
    print(df)
