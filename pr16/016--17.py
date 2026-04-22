import re
log = "2026-04-01 ERROR Failed"
m = re.match(r"(\d{4}-\d{2}-\d{2}) (INFO|ERROR) (.+)", log)
print(m.groups())