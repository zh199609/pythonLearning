import os
import sys

print(eval('6*9'))

data = [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"},
]
print('类型：', type(data))

if __name__ == '__main__':
    print(os.path.basename(__file__).replace('py', 'yaml'))
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(os.path.dirname(os.path.abspath(__file__)))

    del_list = os.listdir('F:/web-ui/output/report_allure')
    if del_list:
        try:
            for f in del_list:
                file_path = os.path.join('F:/web-ui/output/report_allure', f)

                # 判断是不是文件
                if os.path.isfile(file_path):
                    print(f"{f}:是文件")
                    # if not file_path.endswith('.xml'):  # 不删除.xml文件
                    #     os.remove(file_path)
                else:
                    print(f'{f}:不是文件')
                    # os.path.isdir(file_path)
                    # shutil.rmtree(file_path)
        except Exception as e:
            print(e)

    print(sys.platform.lower())