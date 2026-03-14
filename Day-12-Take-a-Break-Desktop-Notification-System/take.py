import time
from plyer import notification

if __name__ == '__main__':
  while True:
    notification.notify(
      title = "*** Take Rest ***",
      message="Time to stretch your body and relax your eyes!",
      timeout = 5)
      
    time.sleep(10)


