# 导包
from api.login import LoginAPI
from api.course import CourseAPI
# import pytest
#断言是为了检查测试结果
# 创建测试类
class TestDelectCourse:
    # 初始化
    token = None

    # 前置处理
    # @pytest.fixture(autouse=True)
    def setup_class(self):
        # 实例化接口对象
        self.login_api = LoginAPI()
        self.delect_api = CourseAPI()

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
        TestDelectCourse.token = res_l.json().get("token")
        print(TestDelectCourse.token)
    # 后置处理
    def teardown_class(self):
        pass
    #课程删除成功
    def test01_delect_success(self):

        res_d = self.delect_api.delectcourse(course_id= 23056458704377207,token=TestDelectCourse.token)
        print(res_d.json())

        # 断言响应状态码
        assert 200 == res_d.status_code
        # 断言指定文字
        assert '成功' in res_d.text
        # 断言json返回数据code值
        assert 200 == res_d.json().get("code")

    # 课程删除失败（课程ID不存在）
    def test02_delect_fail(self):
        res_d = self.delect_api.delectcourse(course_id=110, token=TestDelectCourse.token)
        print(res_d.json())

        # 断言响应状态码
        assert 200 == res_d.status_code
        # 断言指定文字
        assert '失败' in res_d.text
        # 断言json返回数据code值
        assert 500 == res_d.json().get("code")
    # 课程删除失败（用户未登录）
    def test03_delect_fail(self):
        res_d = self.delect_api.delectcourse(course_id=23056458704377215, token="xxxx")
        print(res_d.json())

        # 断言响应状态码
        assert 200 == res_d.status_code
        # 断言指定文字
        assert '失败' in res_d.text
        # 断言json返回数据code值
        assert 401 == res_d.json().get("code")