from Info import Submit
import  hashlib,json,base64,requests
submit=Submit()
submit.ecName=('政企分公司测试')
submit.apId='demo0'
submit.secretKey='123qwe'
submit.mobiles='13800138000'
submit.content='移动改变生活。'
submit.sign='DWItALe3A'
submit.addSerial=''
#字符串拼接
stringBuffer=submit.ecName+submit.apId+submit.secretKey+submit.mobiles+submit.content+submit.sign+submit.addSerial
assert isinstance(stringBuffer,str)
###MD5加密
result=hashlib.md5(stringBuffer.encode(encoding='utf-8')).hexdigest()
#加入mac字段的值
submit.mac=result
#转换成json格式
param=json.dumps(submit.__dict__).replace('_Submit__','')
#print(param)
#base64加密
r=base64.b64encode(param.encode(encoding='utf-8'))
#去除头尾
data_post=str(r,'utf-8')
# print(re)
'''POST方式发送数据'''
url= 'http://112.35.1.155:1992/sms/norsubmit'
# data_json = json.dumps({'key1':'value1','key2':'value2'})   #dumps：将python对象解码为json数据
response = requests.post(url,data_post)
#print(response)
print(response.text)
#print(response.content)
