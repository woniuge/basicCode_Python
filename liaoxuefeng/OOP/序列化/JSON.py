


#Python内置的json模块提供了非常完善的Python对象
# 到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
import json
d = dict(name = 'Bob',age = 20,score = 88)
print(json.dumps(d))

#要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字
# 符串并反序列化：
json_str = '{"age":20,"score":87,"name":"Bob"}'
print(json.loads(json_str))

