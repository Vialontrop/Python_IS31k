import re
from collections import Counter

logs = """2026-04-01 ERROR Failed
2026-04-01 INFO OK
2026-04-02 ERROR Crash"""

errors = re.findall(r"(\d{4}-\d{2}-\d{2}) ERROR", logs)

print(errors)
print(Counter(errors))