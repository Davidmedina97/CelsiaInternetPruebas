from pymongo import MongoClient

uri= "mongodb+srv://josedavid:gxpd0Lzk6Y4CU86E@cluster0.v4sp5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

db = client["CelsiaInternet"]
clientes_collection = db["Clientes"]