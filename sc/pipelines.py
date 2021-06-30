# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector

class ScPipeline(object):
    def __init__(self):
    	self.create_connection()
    	self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(host = 'localhost',user = 'root',password = 'root',database = 'products')
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""DROP TABLE IF EXISTS products""")
        self.cur.execute("""create table products(product_name varchar(255),product_price varchar(255))""")	
	
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.cur.execute("""insert into products values (%s,%s)""",(item['product_name'],item['product_price']))
        self.conn.commit()
