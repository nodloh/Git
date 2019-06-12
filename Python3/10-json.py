#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import json
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
#def student2dict(stu):
#    return{
#            'name':stu.name,
#            'age': stu.age,
#            'score':stu.score
#            }


#JSON反序列化
def dict2student(d):
    return Student(d['name'],['age'],['score'])
s=Student('tom',24,98)
print(json.dumps(s,default=lambda obj:obj.__dict__))
print('反序列化')
json_str='{"score":88,"age":25,"name":"Tom"}'
print(json.loads(json_str,object_hook=dict2student))

#中文序列化
obj=dict(name='老李',age=20)
s=json.dumps(obj,ensure_ascii=False)
x=json.loads(s)
print(s)
print('x=',x)
