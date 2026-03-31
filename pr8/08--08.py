class Logger:
    def log(self, data):
        print(f"Log: {data}")


class ListLogger(Logger):
    def log(self, data):
        print(f"List log: {data}")


class DictLogger(Logger):
    def log(self, data):
        print(f"Dict log: {data}")


loggers = [Logger(), ListLogger(), DictLogger()]
loggers[0].log("test")
loggers[1].log([1, 2, 3])
loggers[2].log({"a": 1})
