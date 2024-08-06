#导包
import requests
import config
#创建对应的接口类
class CourseAPI:
    #初始化
    def __init__(self):
        #指定url基本信息
        # self.url_add_course="http://kdtx-test.itheima.net/api/clues/course"
        # self.url_select_course="http://kdtx-test.itheima.net/api/clues/course/list"
        self.url_add_course = config.BASE_URL+"/api/clues/course"
        self.url_select_course = config.BASE_URL+"/api/clues/course/list"
    #课程添加
    def addcourse(self,token,test_data):
        return  requests.post(url=self.url_add_course,headers= {"Authorization":token},json=test_data)
    #课程查询
    def selectcourse(self,test_data,token):
        return requests.get(url=self.url_select_course+f"/{test_data}",headers={"Authorization":token})
    #课程修改
    def modifycourse(self,token,modify_data):
        return requests.put(url=self.url_add_course,headers={"Authorization":token},json=modify_data)
    #课程删除
    def delectcourse(self,course_id,token):
        return  requests.delete(url=self.url_add_course+f"/{course_id}",headers={"Authorization":token})