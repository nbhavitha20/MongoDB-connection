import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://test:test@testcluster0.z2wcc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.test

# create a db
dbb1 = client['testdb1']

# print all the collections in db
print(client.list_database_names())
collection = dbb1['collection']

# one record insertion
rec1 = {'name':'tiger'}
collection.insert_one(rec1)

#insert many records
record = [{'name':'123'},
          {'name':'dog'}
          ]
collection.insert_many(record)

record1 = [{'name':'123'},
          {'name':'dog',
           'type':'pet',
           'call':['ruby','cherry'],
           'misc':[{'food':['chicken','bone']},{'color':'brown'},[2,4,6,8]]
           }
          ]
rec = collection.insert_many(record1)

#fetch unique ids of records
idList = rec.inserted_ids
for ind, uniqueId in enumerate(idList):
    print (f"{ind},{uniqueId}")

#set limit to view results
no_rec = 2
nrec = collection.find().limit(no_rec)
for i in enumerate(nrec):
    print(f"{i}\n")

#find option
find_1_rec = collection.find_one()
print(find_1_rec)

findAll = collection.find()
print(findAll)

query = {'name':'dog'}
f1 = collection.find(query)
for data in f1:
    print(data)

f2=collection.find({'abc':{'$gt':'100'}})
for f in f2:
    print(f)

# update
present = {'abc':'456'}
collection.update_one(query,present)

#delete
col_delete = dbb1['test_del']

rec_del = [{'name':'123'},
           {'name':'234'},
           {'name':'456'}
]
col_delete.insert_many(rec_del)

# using let to store variable
col_delete.delete_one({ 'name': '123'})
