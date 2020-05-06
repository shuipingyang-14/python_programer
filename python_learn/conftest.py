# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 17:39
# @python  : python 3.7
# @Author  : 水萍
# @File    : conftest.py
# @Software: PyCharm

import pytest


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
	print("-----------------------------")
	# 获取钩子方法的调用结果
	out = yield
	print("用例执行结果", out)

	# 从钩子方法调用结果中获取测试报告
	report = out.get_result()

	print('测试报告：%s' % report)
	print('步骤：%s' % report.when)
	print('nodeid：%s' % report.nodeid)
	print('description:%s' % str(item.function.__doc__))
	print(('运行结果: %s' % report.outcome))


@pytest.fixture(scope="session", autouse=True)
def fix_a():
	print("setup 前置操作")
	yield
	print("teardown 后置操作")
	raise Exception("teardown失败")
