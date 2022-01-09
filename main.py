# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 15:05:42 2022

@author: marth
"""

import pandas as pd
from Factory.SitesAdapterFactory import SitesAdapterFactory
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/scrapper', methods=("POST", "GET"))
def scrapper():

    adapter_factory = SitesAdapterFactory()
    global site_products
    site_products = adapter_factory.initialize_scrapping()
    
    return site_products

@app.route('/results', methods=("POST", "GET"))
def html_table():
    for site in site_products:
        df = pd.DataFrame(site_products[site])
        df.to_csv('{}_wool_comparison.csv'.format(site))
        print(df)
    #return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)
    return render_template('simple.html',  tables=[df.to_html(classes='data', header="true")])


if __name__ == '_main_':
    app.run(host='0.0.0.0')