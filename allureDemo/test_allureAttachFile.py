import allure
import pytest

"""
@allure.step() 装饰器：可以设置测试步骤，让测试用例的执行过程更加详细
allure.attach() 函数：可以设置需要显示在allure报告的附件，包含了多种类型，可以通过allure.attachment_type查看支持的类型


@allure.description()
@allure.title()

语法格式，有三种
@allure.description(str）
在测试用例函数声明下方添加 """ """
@allure.description_html(str）：相当于传一个HTML代码组成的字符串，类似 allure.attach() 中传HTML
方式一方式二的效果和作用是一致的， 哪个方便哪个来
"""


@pytest.fixture
def attach_file_in_module_scope_with_finalizer(request):
    allure.attach('在fixture前置操作里面添加一个附件txt', 'fixture前置附件', allure.attachment_type.TEXT)

    def finalizer_module_scope_fixture():
        allure.attach('在fixture后置操作里面添加一个附件txt', 'fixture后置附件',
                      allure.attachment_type.TEXT)

    request.addfinalizer(finalizer_module_scope_fixture)


@allure.description("""
这是一个@allure.description装饰器
没有特别的用处
""")
def test_with_attacments_in_fixture_and_finalizer(attach_file_in_module_scope_with_finalizer):
    pass





def test_multiple_attachments():
    allure.attach('<head></head><body> 一个HTML页面 </body>', 'Attach with HTML type', allure.attachment_type.HTML)
    allure.attach.file('./reports.html', attachment_type=allure.attachment_type.HTML)
