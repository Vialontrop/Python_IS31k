# 18--19.py
class MyContext:
    def __enter__(self):
        print("Start")
    def __exit__(self, exc_type, exc, tb):
        print("End")

with MyContext():
    pass
