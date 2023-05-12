#import sleep() and perf_counter() functions from time module
from time import sleep , perf_counter

def task():
	print('Starting a task ---> ')
	sleep(1)
	print ('<---- task is DONE')

start_time = perf_counter()

task()
task()

end_time = perf_counter()
print(f'it took{end_time-start_time: 0.2f} second(s) to complete') 