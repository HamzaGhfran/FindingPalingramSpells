"""Code to compute run time of program or function"""
import time
import cProfile
import palingramwords
cProfile.run('palingramwords.palingram()')    


"""We can also compute time like this"""
start_time = time.time()
palingramwords.palingram()
end_time = time.time()