import json
import  pickle
data = {'k1':13,'k2':'a就哭闹'}
print(pickle.dumps(data)) #将数据通过特殊的形式转换为只有python语言认识的字符串

print(json.dumps(data,ensure_ascii=False))