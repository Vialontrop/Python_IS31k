import os
if os.path.exists('data.txt'):
    print(os.path.getsize('data.txt'))