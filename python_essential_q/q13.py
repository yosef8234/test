# Question 13

# Place the following functions below in order of their efficiency. They all take in a list of numbers between 0 and 1. The list can be quite long. An example input list would be [random.random() for i in range(100000)]. How would you prove that your answer is correct?

def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i<0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]

# Answer
# Most to least efficient: f2, f1, f3. To prove that this is the case, you would want to profile your code. Python has a lovely profiling package that should do the trick.

import cProfile
import random
lIn = [random.random() for i in range(100000)]
cProfile.run('f1(lIn)')
cProfile.run('f2(lIn)')
cProfile.run('f3(lIn)')


# >>> cProfile.run('f1(lIn)')
#          4 function calls in 0.065 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.011    0.011    0.063    0.063 <stdin>:1(f1)
#         1    0.001    0.001    0.065    0.065 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.052    0.052    0.052    0.052 {sorted}


# >>> cProfile.run('f2(lIn)')
#          4 function calls in 0.032 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.011    0.011    0.031    0.031 <stdin>:1(f2)
#         1    0.001    0.001    0.032    0.032 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.020    0.020    0.020    0.020 {sorted}


# >>> cProfile.run('f3(lIn)')
#          4 function calls in 0.059 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.013    0.013    0.057    0.057 <stdin>:1(f3)
#         1    0.002    0.002    0.059    0.059 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.044    0.044    0.044    0.044 {sorted}

# Why do we care?

# Locating and avoiding bottlenecks is often pretty worthwhile. A lot of coding for efficiency comes down to common sense - in the example above it's obviously quicker to sort a list if it's a smaller list, so if you have the choice of filtering before a sort it's often a good idea. The less obvious stuff can still be located through use of the proper tools. It's good to know about these tools.