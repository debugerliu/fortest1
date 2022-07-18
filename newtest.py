import pytest


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
        print('lxw修改的')
        print('别人修改的2')
        print('lxw修改2')


if __name__ == '__main__':
    #    pytest.main()
    pytest.main(["newtest.py", '--html=./zzreport.html'])
