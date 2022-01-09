from DB.DB import DB


class ProductDBModelAdapter:
    def __init__(self):
        self.table_name = "Products"
        # create DB
        self.create_table()

    def create_table(self):
        try:
            db = DB()
            connection = db.create_connection()
            sql = '''CREATE TABLE {} (
                                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Store VARCHAR(255),
                                Brand TEXT,
                                Name TEXT,
                                ShortName VARCHAR(255),
                                Price DOUBLE,
                                Currency VARCHAR(20),
                                Composition TEXT,
                                DeliveryTime TEXT,
                                Size TEXT,
                                Link TEXT,
                                Image TEXT,
                                Description TEXT,
                                CreatedAt TEXT DEFAULT CURRENT_TIMESTAMP,
                                LastModified TEXT DEFAULT CURRENT_TIMESTAMP
                            );
                        '''.format(self.table_name)

            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            return False

        return True

    def merge_products(self, product):

        try:

            db = DB()
            connection = db.create_connection()
            is_product_exists = self.try_find_product(connection, product)

            if is_product_exists == True:
                self.update_product(connection, product)
            else:
                self.insert_product(connection, product)

            connection.close()
        except Exception as e:
            print(e)
            return False

        return True

    def insert_product(self, sql_connection, product):

        try:
            COLUMNS = ''
            VALUES_STR = ''
            VALUES_LIST = []

            for key in product:
                if COLUMNS != '':
                    COLUMNS += ','
                    VALUES_STR += ','

                COLUMNS += str(key)
                VALUES_STR += '?'
                VALUES_LIST.append(product[key])

            VALUES = tuple(VALUES_LIST)

            connection = sql_connection
            cursor = connection.cursor()

            sql = 'INSERT INTO {} ({}) VALUES ({});'.format(self.table_name, COLUMNS, VALUES_STR)

            cursor.execute(sql, VALUES)
            connection.commit()
        except Exception as e:
            print(e)
            return False

        return True

    def try_find_product(self, sql_connection, product):
        store = product['Store']
        brand = product['Brand']
        name = product['Name']

        cursor = sql_connection.cursor()
        sql = 'SELECT * FROM {} WHERE Store=? AND Brand=? AND Name=?'.format(self.table_name)
        cursor.execute(sql, (store, brand, name))
        rows = cursor.fetchall()
        count_rows = len(rows)

        if count_rows == 0:
            return False

        return True

    def update_product(self, sql_connection, product):
        try:
            COLUMNS = ''
            SKIP = ['Store', 'Brand', 'Name']
            VALUES_LIST = []

            for key in product:
                if COLUMNS != '':
                    COLUMNS += ','

                if key not in SKIP:
                    COLUMNS += " {}=? ".format(key)
                    VALUES_LIST.append(product[key])

            VALUES_LIST.append(product['Store'])
            VALUES_LIST.append(product['Brand'])
            VALUES_LIST.append(product['Name'])

            VALUES = tuple(VALUES_LIST)

            connection = sql_connection
            cursor = connection.cursor()

            sql = "UPDATE {} SET {}, LastModified=date('now') WHERE Store=? AND Brand=? AND Name=?".format(self.table_name, COLUMNS)

            cursor.execute(sql, VALUES)
            connection.commit()
        except Exception as e:
            print(e)
            return False

        return True

    def get_products(self, WHERE=None, Limit=None):

        try:

            db = DB()
            connection = db.create_connection()
            cursor = connection.cursor()
            sql = 'SELECT * FROM ' + self.table_name
            if WHERE != None:
                sql += ' {} '.format(WHERE)

            if Limit != None:
                sql += ' LIMIT {}'.format(Limit)

            products = []

            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                products.append({
                    'Id': row[0],
                    'Store': row[1],
                    'Brand': row[2],
                    'Name': row[3],
                    'ShortName': row[4],
                    'Price': row[5],
                    'Currency': row[6],
                    'Composition': row[7],
                    'DeliveryTime': row[8],
                    'Size': row[9],
                    'Link': row[10],
                    'Image': row[11],
                    'Description': row[12],
                    'CreatedAt': row[13],
                    'LastModified': row[14],
                })

            connection.close()
        except Exception as e:
            print(e)
            return None

        return products
