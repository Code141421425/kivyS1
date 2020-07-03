
from airtest.core.api import *

auto_setup(__file__)

# 始終允許
touch([796, 1771])

#等待遊戲警告，公司logo等
sleep(12)

# 點擊跳過
touch([940, 97])

#等待讀條