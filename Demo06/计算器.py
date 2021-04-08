import functools
import re


def minus_operator_handler(formula):
    '''处理一些特殊得减号算法'''
    minus_operator = re.split('-', formula)
    calc_list = re.findall('[0-9]', formula)
    if minus_operator[0] == '':  # 第一值肯定不是负号
        calc_list[0] = '-%s' % calc_list[0]
    res = functools.reduce(lambda x, y: float(x) - float(y), calc_list)
    print("\033[33;1m减号[%s]处理结果:\033[0m" % formula, res)
    return res


def remove_duplicates(formula):
    formula = formula.replace("++", "+")
    formula = formula.replace("+-", "-")
    formula = formula.replace("-+", "-")
    formula = formula.replace("--", "+")
    formula = formula.replace("- -", "+")
    return formula


def compute_mutiply_and_dividend(formula):
    '''算乘除，传进来的是字符串噢'''
    operators = re.findall("[*/]", formula)
    cals_list = re.split('[*/]', formula)
    res = None
    for index, i in enumerate(cals_list):
        if res:
            if operators[index - 1] == '*':
                res *= float(i)
            elif operators[index - 1] == '/':
                res /= float(i)
        else:
            res = float(i)
    print("\033[31;1m[%s]运算结果=\033[0m" % formula, res)
    return res
