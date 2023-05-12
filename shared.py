import threading

shared_memory = []

def write_to_shared_memory(value):
	global shared_memory
	shared_memory.append(value)

def read_from_shared_memory():
	global shared_memory
	return shared_memory

def write_thread():
	for i in range(5):
		write_to_shared_memory(i)

def read_thread():
	print(read_from_shared_memory())

threading.Thread(target = write_thread).start()
threading.Thread(target = read_thread).start()