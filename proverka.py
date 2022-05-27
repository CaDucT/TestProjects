from threading import Timer
run = True
def test():
	global run
	print("something")
	if run:
		Timer(1, test).start()

test()