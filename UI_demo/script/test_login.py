import unittest

from UI_demo.page.LoginPage import LoginPage


class Caselogin163mail(unittest.TestCase):

    def test_login_main(self):
        login_page = LoginPage()
        username_element = login_page.find_element(By.NAME, 'email')
        print(username_element)

if __name__ == '__main__':
    unittest.main()
