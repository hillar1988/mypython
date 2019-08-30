from Info import Submit
import hashlib
import json
import base64
import requests

def Post():
    #list = ['15168557200', '15867557512', '18267432205', '15990572628']
    list = ['15168557200']
    t = ','.join(list)
    submit = Submit()
    submit.ecName = "宁波奉化农村商业银行股份有限公司"
    submit.apId = "http"
    #submit.secretKey = "fhxyls62"
    #submit.mobiles = "15168557200,15867557512,18267432205,15990572628"
    submit.mobiles = t
    submit.content = "测试"
    submit.sign = "WbsLve34q"
    submit.addSerial = ""
    # 字符串拼接
    stringBuffer = submit.ecName + submit.apId + "fhxyls62" + \
        submit.mobiles + submit.content + submit.sign + submit.addSerial
    #print(stringBuffer)
    assert isinstance(stringBuffer, str)
    # MD5加密
    #result=hashlib.md5(stringBuffer.encode())
    result = hashlib.md5(stringBuffer.encode(encoding='utf-8')).hexdigest()
    # 加入mac字段的值
    submit.mac = result
    # 转换成json格式
    param = json.dumps(submit.__dict__).replace('_Submit__', '')
    # base64加密
    r = base64.b64encode(param.encode(encoding='utf-8'))
    # 去除头尾
    data_post = str(r, 'utf-8')
    '''POST方式发送数据'''
    # url = 'http://112.35.1.155:1992/sms/norsubmit'
    # response = requests.post(url, data_post)
    ##测试
    url="http://154.24.35.201:9080/index.aspx"
    s={"errorCode":"DELIVRD","mobile":"15168557200","msgGroup":"0826112130001000330441","receiveDate":"20190826112100","reportStatus":"CM:0000","submitDate":"20190826112100"}
    ss= json.dumps(s)
    print(ss)
    response = requests.post(url, ss)
    ##测试

    #print(response)
    print(response.text)
    #print(response.content)

if __name__ == '__main__':
 for i in range(1,10001):
    Post()





