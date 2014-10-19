import time, sys
total = 10
for i in range(total):
    sys.stdout.write('%d / %d\r' % (i, total))
    sys.stdout.flush()
    time.sleep(0.5)
print('Done     ')