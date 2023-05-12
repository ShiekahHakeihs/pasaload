#Multi-threaded
from threading import Thread
from time import sleep, perf_counter
#import the thread class from the threading module


#create a new thread by instantianting and instance of the thread class

#new_thread = Thread(target = fn,args = args_tuple)
'''
	Thread() accepts 2 parameters
	- target - specifies a function(fn) to run the new thread
	- args - specifies arguments of the function
	The arguments is tuple
'''

def task():
	print('Starting a task ---> ')
	sleep(1)
	print ('<---- task is DONE')

start_time = perf_counter()

#create two threads
t1 = Thread(target=task)
t2 = Thread(target=task)

#start the thread

t1.start()
t2.start()

#wait for the threads to complete - join() by this function, the main thread will wait for the second thread to complete before it terminated

t1.join()
t2.join()
end_time = perf_counter()
print(f'it took{end_time-start_time: 0.2f} second(s) to complete') 

my_tuple = (1,2,"three", 4.0)

print(my_tuple[2])
#iterate
for item in my_tuple:
	print(item)