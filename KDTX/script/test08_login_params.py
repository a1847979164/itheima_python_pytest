# 导包
from api.login import LoginAPI
import pytest
import json
import config
#断言是为了检查测试结果
# # 测试数据（列表嵌套元组）
# test_data = [
#     ("admin", "HM_2023_test", 200, '成功', 200),
#     ("", "HM_2023_test", 200, '错误', 500),
#     ("admin123", "HM_2023_test", 200, '错误', 500),
# ]
#读取json文件(列表嵌套字典)
def build_data(json_file):
    #定义一个空列表
    test_data=[]
    #打开json文件
    with open(json_file,"r",encoding="utf-8") as f:
        #加载json文件数据
        json_data = json.load(f)
        #循环遍历测试数据
        for case_data in json_data:
            #转换数据格式[{},{}]==>[(),()]
            username = case_data.get("username")
            password = case_data.get("password")
            status = case_data.get("status")
            message = case_data.get("message")
            code = case_data.get("code")
            test_data.append((username,password,status,message,code))
    #返回处理之后的数据
    return test_data

# 创建测试类
class TestLoginAPI():
    # 初始化
    uuid = None

    # @pytest.fixture(autouse=True)
    # 前置处理
    def setup_class(self):
        # 实例化接口类
        self.login_api = LoginAPI()

    # 后置处理
    def teardown_class(self):
        pass

    # 登录成功
    @pytest.mark.parametrize("username,password,status,message,code",build_data(json_file=config.BASE_PATH+"/data/login.json"))
    def test01_success(self,username,password,status,message,code):
        # 获取验证码
        res_v = self.login_api.get_verify_code()
        print(res_v.status_code)
        # 提取uuid数据
        TestLoginAPI.uuid = res_v.json().get("uuid")
        # 登录成功
        login_data = {
            "username": username,
            "password": password,
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        res_l = self.login_api.login(test_data=login_data)
        # 断言响应状态码为200
        assert status == res_l.status_code
        # 断言响应数据包含‘成功’
        assert message in res_l.text
        # 断言响应json数据中code值
        assert code == res_l.json().get("code")
