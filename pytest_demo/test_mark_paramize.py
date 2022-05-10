import sys

import pytest

# 参数化，前面两个变量，后面是数据
@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+4",6),("9*3",20)])
def test_eval(test_input,expected):
    assert eval(test_input) == expected

#参数组合
@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[6,8,12])
def test_foo(x,y):
    print(f"测试数据组合x:{x},y:{y}")

#方法名作为参数
test_user_data = ['Tom','Jerry']
@pytest.fixture(scope="module")
def login_r(request):
    user = request.param
    print(f"\n 打开首页准备登录，登录用户：{user}")
    return user

@pytest.mark.xfail
# @pytest.mark.skip("此测试用例不执行登录 ")
# @pytest.mark.skipif(sys.platform == "darwin",reason="不在macos上执行")
@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值: {a}")
    assert a != ""
    raise NameError

if __name__ == '__main__':
    pytest.main()
