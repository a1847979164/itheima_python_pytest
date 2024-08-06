# 导包
from api.login import LoginAPI
from api.course import CourseAPI
#断言是为了检查测试结果

# 创建测试类
class TestAddCourse:
    # 初始化
    token = None

    # 前置处理
    def setup_class(self):
        # 实例化接口对象
        self.login_api = LoginAPI()
        self.addcourse_api = CourseAPI()
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
        TestAddCourse.token = res_l.json().get("token")
        print(TestAddCourse.token)
    # 后置处理
    def teardown_class(self):
        pass

    # 添加课程成功
    def test02_success(self):
        add_data = {
            "name": "测试开发提升课02",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课02"
        }
        res_c = self.addcourse_api.addcourse(token=TestAddCourse.token, test_data=add_data)
        print(res_c.json())
        # 断言响应状态码
        assert 200 == res_c.status_code
        # 断言指定文字
        assert '成功' in res_c.text
        # 断言json返回数据code值
        assert 200 == res_c.json().get("code")
    # 添加课程失败（未登录）
    def test03_fail(self):
        add_data = {
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课01"
        }
        res_c = self.addcourse_api.addcourse(token="xxx", test_data=add_data)
        print(res_c.json())
        # 断言响应状态码
        assert 200 == res_c.status_code
        # 断言指定文字
        assert '认证失败' in res_c.text
        # 断言json返回数据code值
        assert 401 == res_c.json().get("code")
