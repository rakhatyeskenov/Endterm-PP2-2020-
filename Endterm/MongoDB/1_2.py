# 1111111111111111111111111111111
import pymongo
import ssl

# 2222222222222222222222222222222
client = pymongo.MongoClient(
    "mongodb+srv://pp2:pp2password@cluster0-83kv7.mongodb.net/test?retryWrites=true&w=majority",
    ssl_cert_reqs=ssl.CERT_NONE)

# connect to mydatabase
mydb = client["mydatabase"]
print(client.list_database_names())

dblist = client.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")

# connect to collection
# mycol = mydb["students"]

# adding data in collection
# mydict = {"name": "Rakhat", "surname": "Yeskenov", "id": "19BD"}
# x = mycol.insert_one(mydict)
# x.inserted_id
# print(mydb.list_collection_names())

# 33333333333333333333333333333333


# create collection customers
mycol = mydb["customers"]

collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")
else: print
