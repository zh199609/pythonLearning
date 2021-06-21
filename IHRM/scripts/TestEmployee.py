import unittest

from IHRM import app
from IHRM.api.employee import EmployeeAPI


class TestEmployee(unittest.TestCase):
    employee_id = None

    def setUp(self):
        self.employee_api = EmployeeAPI()

    def tearDown(self):
        pass

    def test_add_employee(self):
        add_employee_data = {
            "username": "052301",  # 用户名唯一
            "mobile": "13212070501",  # 手机号唯一
            "timeOfEntry": "2021-07-09",
            "formOfEmployment": 1,
            "workNumber": "070501",  # 员工ID唯一性
            "departmentName": "销售",
            "departmentId": "1266699057968001024",
            "correctionTime": "2020-07-30T16:00:00.000Z"
        }
        response = self.employee_api.add(app.headers_data, add_employee_data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        TestEmployee.employee_id = response.json().get("data").get("id")