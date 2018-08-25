from datetime import datetime

import time

v = 0
while True:
    print(datetime.now())
    v += 1
    time.sleep(v)
