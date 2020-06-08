from ColorQuantizer import ColorQuantize
import time


start = time.time()
ColorQuantize.Cluster('test.png', 4)
end = time.time()
print(end - start)