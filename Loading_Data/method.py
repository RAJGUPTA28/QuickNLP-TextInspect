# Load CSV (using python)
import csv
import numpy
filename = 'pima-indians-diabetes.data.csv'
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)


# using Numpy
from numpy import loadtxt
from urllib.request import urlopen
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indiansiabetes.data.csv'
raw_data = urlopen(url)
dataset = loadtxt(raw_data, delimiter=",")
print(dataset.shape)




#load Data from SQL
import sqlite3
import pandas as pd
conn = sqlite3.connect('test_database') 
sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM products
                               ''', conn)
df = pd.DataFrame(sql_query, columns = ['product_id', 'product_name', 'price'])
print (df)
