import thread

def Threadfun( i,j):
    while(True):
        i += 1
        print "x = " + str(i)

t = thread.start_new_thread(Threadfun, (1,1))
while True:
    pass