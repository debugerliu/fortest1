import pytest


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_three(self):
        x = "hello真的本地"
        # 我这里修改了
        assert hasattr(x, "check")
        # 本地修改了
        # 线上修改
        
    def lzy(self):
        pass

    def lxw(self):
        pass


if __name__ == '__main__':
    #    pytest.main()
    pytest.main(["newtest.py", '--html=./zzreport.html'])
