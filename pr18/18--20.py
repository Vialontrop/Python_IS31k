# 18--20.py
class SafeFile:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        try:
            self.file = open(self.filename)
            return self.file
        except Exception as e:
            print("Error:", e)
    def __exit__(self, exc_type, exc, tb):
        print("File closed")
        try:
            self.file.close()
        except:
            pass

with SafeFile("input.txt") as f:
    if f:
        print(f.read())
