from selenium.webdriver.common.by import By


def find(by=By.ID, value=None):
    print(by)
    print(value)


location = By.ID, "axxx"
locationA = (By.ID, "xxdsf")
for i in locationA:
    print(i)
find(*location)

try:
    a = 1 / 1
except Exception as ex:
    print(ex)
else:
    print("一切正常")
finally:
    print('finally')
