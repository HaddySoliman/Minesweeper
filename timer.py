import time

start=input ("Press enter to start playing!")
print("The timer has started")
start_time = time.time()
end=input ("Press enter to stop the timer")
end_time = time.time()
elapsed= end_time - start_time
elapsed= int(elapsed)
print ("You took ... ", elapsed, "seconds")
