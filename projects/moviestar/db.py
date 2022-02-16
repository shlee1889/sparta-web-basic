from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# # 저장 - 예시
# doc = {'name':'bobby','age':21}
# db.articles.insert_one(doc)

# # 한 개 찾기 - 예시
# user = db.articles.find_one({'name':'bobby'})

# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# same_ages = list(db.articles.find({'age':21},{'_id':False}))

# # 바꾸기 - 예시
# db.articles.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
# db.articles.delete_many({})