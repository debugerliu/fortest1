import pytest


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
        print('hello')


if __name__ == '__main__':
    #    pytest.main()
    pytest.main(["newtest.py", '--html=./zzreport.html'])

   
