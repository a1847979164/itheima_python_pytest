#导包
import pytest
import config
from api.login import LoginAPI
from api.course import  CourseAPI
from api.contract import ConTractAPI

#创建测试类
class TestContractBusiness:
    # @pytest.fixture(autouse=True)
    #初始化
    token = None
    filename=None

    #前置处理
    def setup_class(self):
        # 实例化接口对象
        self.login_api = LoginAPI()
        self.addcourse_api = CourseAPI()
        self.uploadcontract_api = ConTractAPI()
        self.addcontract_api=ConTractAPI()

    #后置处理
    def teardown_class(self):
        pass

    #1.登录成功
    def test01_login_success(self):

        #获取验证码
        res_v = self.login_api.get_verify_code()
        print(res_v.status_code)
        print(res_v.json())
        #打印uuid数据
        print(res_v.json().get("uuid"))
        #登录
        # header_data={
        #     "Content-Type":"application/json"
        # }
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": res_v.json().get("uuid")
        }
        res_l = self.login_api.login(test_data=login_data)
        print(res_l.status_code)
        print(res_l.json())

        #提取登录成功之后的token数据并保存在类的属性中
        TestContractBusiness.token = res_l.json().get("token")

    # 2.添加课程成功
    def test02_addcourse_success(self):
        test_data = {
            "name": "测试开发提升课02",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info":"测试开发提升课02"
        }
        res_c= self.addcourse_api.addcourse(token = TestContractBusiness.token,test_data=test_data)
        print(res_c.json())

    # 3.合同上传成功
    def test03_upload_contract(self):
        # 读取pdf文件数据
        file = "/data/test.pdf"
        f = open(config.BASE_PATH+file, "rb")
        res_c=self.uploadcontract_api.upload_contract(token=TestContractBusiness.token,file=f)
        # 提取合同上传成功之后的fileName数据并保存在类的属性中
        TestContractBusiness.filename= res_c.json().get("fileName")
        print(res_c.json())
        print(TestContractBusiness.filename)

    # 4.新增合同成功
    def test04_add_contract(self):
        test_data={
            "name":"测试888",
            "phone":"136123456789",
            "contractNo":"HT20240106",
            "subject":"6",
            "courseId":"99",
            "channel":"0",
            "activityId":77,
            "fileName":TestContractBusiness.filename
        }
        res_ac= self.addcontract_api.addcontract(token=TestContractBusiness.token,test_data=test_data)
        print(res_ac.json())