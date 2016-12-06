# Question 7

What is monkey patching and is it ever a good idea?

# Answer
# Monkey patching is changing the behaviour of a function or object after it has already been defined. For example:

import datetime
datetime.datetime.now = lambda: datetime.datetime(2012, 12, 12)

# Most of the time it's a pretty terrible idea - it is usually best if things act in a well-defined way. One reason to monkey patch would be in testing. The mock package is very useful to this end.