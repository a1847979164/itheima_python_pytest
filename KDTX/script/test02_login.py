#登录成功


#导包
import requests

url ="http://kdtx-test.itheima.net/api/login"
header_data = {
    "Content-Type":"application/json"
}
login_data = {
    "username":"admin",
    "password":"HM_2023_test",
    "code":2,
    "uuid":"c5ba857faf6f411fb8fad8f5ef444951"
}
#发送请求
response =  requests.post(url=url,headers=header_data,json=login_data)

#查看响应
print(response.status_code)
print(response.json())