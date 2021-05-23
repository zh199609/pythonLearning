import os

base_dir = os.getcwd()

base_dir2 = os.path.abspath(__file__)
print(os.path.dirname(base_dir2))
print(base_dir)
