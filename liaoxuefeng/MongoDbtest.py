import pymongo


#1.链接MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#2.指定数据库
mydb = myclient["mydba"]
'''
dblist = myclient.list_database_names()
if "runoobdb" in dblist:
    print("数据库已存在！")
'''
#3.指定集合
mycol = mydb["sites"]

#4.插入数据
#4.1单条
student={
    '_id':2,
    'name':'python',
    'age':200,
}
#result=mycol.insert(student)
#print(result)
#4.2多条
suudentany=[
    {'_id':3,'name':'java','age':300},
    {'_id':4,'name':'javascript','age':400},
    {'_id':5,'name':'c++','age':500}
]
#result = mycol.insert_many(suudentany)
#print(result)
#print(result.inserted_ids) #显示插入数据id列表

#5. 查询数据
result=mycol.find_one({'name':'python'}) #查询单条数据
print(type(result)) #返回字典类型
print(result)
#查询多条数据，需要迭代读取
resultall = mycol.find()
for i in resultall:
    print(i)