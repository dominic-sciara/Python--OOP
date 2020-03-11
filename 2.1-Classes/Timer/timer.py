import time

class Timer(object):
    def __init__(self):
        self._start = None

    conversion = {'seconds' : 1, 'minutes' : 60, 'hours' : 3600}
        
    
    def start(self):
        if self._start is None:
            self._start = time.time()
        else:
            print 'Timer already started!'

    def end(self, config = 'seconds'):
        if self._start is not None:
            print ((time.time() - self._start) / self.conversion[config]), config
            self._start = None
        else:
            print 'Timer is has not been started!'
    
def main():
    t = Timer()
    t.start()
    # Lots of code here
    t.end('hours')

if __name__ == "__main__":
    main()