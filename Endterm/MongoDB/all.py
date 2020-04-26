import pymongo
import ssl

myclient = pymongo.MongoClient(
    "mongodb+srv://pp2:pp2password@cluster0-83kv7.mongodb.net/test?retryWrites=true&w=majority",
    ssl_cert_reqs=ssl.CERT_NONE)


mydb = myclient["mydatabase"]

mycol = mydb["customers"]

print(mydb.list_collection_names())

collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")

# insert #################################### 4 #######################################

mydict = {"name": "John", "address": "Highway 37"}
x = mycol.insert_one(mydict)


# Return the _id Field
mydict = {"name": "Peter", "address": "Lowstreet 27"}
x = mycol.insert_one(mydict)
print(x.inserted_id)


# Insert Multiple Documents


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents:
print(x.inserted_ids)


# Insert Multiple Documents, with Specified IDs
mylist = [
    {"_id": 1, "name": "John", "address": "Highway 37"},
    {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    {"_id": 3, "name": "Amy", "address": "Apple st 652"},
    {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
    {"_id": 5, "name": "Michael", "address": "Valley 345"},
    {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
    {"_id": 8, "name": "Richard", "address": "Sky st 331"},
    {"_id": 9, "name": "Susan", "address": "One way 98"},
    {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
    {"_id": 12, "name": "William", "address": "Central st 954"},
    {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
    {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents:
print(x.inserted_ids)


# Find One #################################### 5 #######################################
x = mycol.find_one()
print(x)

# Find all
for x in mycol.find():
  print(x)

# Return Only Some Fields
for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
  print(x)

for x in mycol.find({}, {"address": 0}):
  print(x)


#Filter the Result  #################################### 6 #######################################
myquery = {"address": "Park Lane 38"}

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

# Advanced Query 
for x in mydoc:
  print(x)

# Filter With Regular Expressions
myquery = {"address": {"$regex": "^S"}}

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)


# Sort the Result #################################### 7 #######################################

mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)

# Sort Descending


mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x)

# # delete #################################### 8 #######################################
# myquery = {"address": "Mountain 21"}
# mycol.delete_one(myquery)

# # Delete Many Documents
# myquery = {"address": {"$regex": "^S"}}
# x = mycol.delete_many(myquery)
# print(x.deleted_count, " documents deleted.")

# # Delete All Documents in a Collection
# x = mycol.delete_many({})
# print(x.deleted_count, " documents deleted.")



# Python MongoDB Drop Collection #############################   9   ################################ 

# mycol.drop()


# Update Collection  #################################### 10 #######################################

myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}
mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)

#   Update Many
x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")

# Limit the Result #################################### 11 #######################################

myresult = mycol.find().limit(5)
#print the result:
for x in myresult:
  print(x)
