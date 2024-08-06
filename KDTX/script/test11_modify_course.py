# 导包
from api.login import LoginAPI
from api.course import CourseAPI
# import pytest
#断言是为了检查测试结果
# 创建测试类
class TestModifyCourse:
    # 初始化
    token = None

    # 前置处理
    # @pytest.fixture(autouse=True)
    def setup_class(self):
        # 实例化接口对象
        self.login_api = LoginAPI()
        self.modify_api = CourseAPI()

        # 获取验证码
        res_v = self.login_api.get_verify_code()
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": res_v.json().get("uuid")
        }
        res_l = self.login_api.login(test_data=login_data)
        # 提取登录成功之后的token数据并保存在类的属性中
        TestModifyCourse.token = res_l.json().get("token")
        print(TestModifyCourse.token)
    # 后置处理
    def teardown_class(self):
        pass

    #修改课程成功
    def test01_modify_success(self):
        modify_data={
            "id":23056458704377239,
            "name":"接口测试001",
            "subject":"6",
            "price":998,
            "applicablePerson":"2",
            "info":"课程介绍001"
        }
        res_m =  self.modify_api.modifycourse(token=TestModifyCourse.token,modify_data=modify_data)
        print(res_m.json())
        # 断言响应状态码
        assert 200 == res_m.status_code
        # 断言指定文字
        assert '成功' in res_m.text
        # 断言json返回数据code值
        assert 200 == res_m.json().get("code")

    # 修改课程失败（用户未登录）
    def test02_modify_fail(self):
        modify_data={
            "id":23056458704377239,
            "name":"接口测试001",
            "subject":"6",
            "price":998,
            "applicablePerson":"2",
            "info":"课程介绍001"

        }
        res_m = self.modify_api.modifycourse(token="xxx",modify_data=modify_data)
        # 断言响应状态码
        assert 200 == res_m.status_code
        # 断言指定文字
        assert '失败' in res_m.text
        # 断言json返回数据code值
        assert 401 == res_m.json().get("code")