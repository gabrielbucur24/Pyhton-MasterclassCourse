# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter(), monotonic() and process_time()
#
# Use the documentation for the get_clock_info() function
# to work out how to call it fo each of the clocks

import time

tm1 = time.get_clock_info('time')
mono1 = time.get_clock_info('monotonic')
pc1 = time.get_clock_info('perf_counter')
pt1 = time.get_clock_info('process_time')
print(tm1)
print(mono1)
print(pc1)
print(pt1)

tm = time.time()
mono = time.monotonic()
pc = time.perf_counter()
pt = time.process_time()

print('time() = ', tm, '; monotonic() = ', mono, '; perf_counter() = ', pc, '; process_time() = ', pt)

