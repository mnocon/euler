import doctest
import unittest
from solutions import Problem69 as challenge

current_challenge = challenge.ProblemSolution()
current_challenge.run_tests()
test_suite = doctest.DocTestSuite(challenge, extraglobs={'t': challenge.ProblemSolution()})
unittest.TextTestRunner().run(test_suite)
solution = current_challenge.execute()
print("Problem {} solution: {}".format(challenge.__name__, solution))
