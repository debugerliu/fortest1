import pytest


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
        # 本地新增
        # 别人远端新增


if __name__ == '__main__':
    #    pytest.main()
    pytest.main(["newtest.py", '--html=./zzreport.html'])
