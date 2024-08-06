import requests
import config
class ConTractAPI:
    # 初始化
    def __init__(self):
        # 指定url基本信息
        # self.url_contract = "http://kdtx-test.itheima.net/api/common/upload"
        # self.url_addcontract="http://kdtx-test.itheima.net/api/contract"
        self.url_contract = config.BASE_URL+"/api/common/upload"
        self.url_addcontract = config.BASE_URL+"/api/contract"

    # 合同上传业务
    def upload_contract(self,token,file):
        return requests.post(url=self.url_contract,headers={"Authorization":token},files={"file":file})

    # 新增合同业务
    def addcontract(self, token, test_data):
        return requests.post(url=self.url_addcontract, headers={"Authorization": token}, json=test_data)