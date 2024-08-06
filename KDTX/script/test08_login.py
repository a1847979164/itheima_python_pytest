#导包
from api.login import LoginAPI
import pytest

#创建测试类
class TestLoginAPI:
    # 初始化
    uuid = None
    # @pytest.fixture(autouse=True)
    #前置处理
    def setup_class(self):
        #实例化接口类
        self.login_api = LoginAPI()

    #后置处理
    def teardown_class(self):
        pass

    #登录成功
    def test01_success(self):
        # 获取验证码
        res_v = self.login_api.get_verify_code()
        print(res_v.status_code)
        # 提取uuid数据
        TestLoginAPI.uuid = res_v.json().get("uuid")
        #登录成功
        login_data={
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        res_l = self.login_api.login(test_data=login_data)
        #断言响应状态码为200
        assert  200 == res_l.status_code
        #断言响应数据包含‘成功’
        assert  '成功' in res_l.text
        #断言响应json数据中code值
        assert  200 == res_l.json().get("code")
    #登录失败（用户名为空）
    def test02_failer(self):
        # 获取验证码
        res_v = self.login_api.get_verify_code()
        print(res_v.status_code)
        # 提取uuid数据
        TestLoginAPI.uuid = res_v.json().get("uuid")
        #登录失败（用户名为空）
        login_data={
            "username": "",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        res_l = self.login_api.login(test_data=login_data)
        # 断言响应状态码为200
        assert 200 == res_l.status_code
        # 断言响应数据包含‘成功’
        assert '错误' in res_l.text
        # 断言响应json数据中code值
        assert 500 == res_l.json().get("code")
    #登录失败（未注册用户）
    def test03_failer(self):
        # 获取验证码
        res_v = self.login_api.get_verify_code()
        print(res_v.status_code)
        # 提取uuid数据
        TestLoginAPI.uuid = res_v.json().get("uuid")
        #登录失败（未注册用户）
        login_data={
            "username": "admin123",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        res_l = self.login_api.login(test_data=login_data)
        # 断言响应状态码为200
        assert 200 == res_l.status_code
        # 断言响应数据包含‘成功’
        assert '错误' in res_l.text
        # 断言响应json数据中code值
        assert 500 == res_l.json().get("code")