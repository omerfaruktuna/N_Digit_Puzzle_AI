
from depthlimitedsearch import *
from n_digit_puzzle import Node_Graph

global vstd
vstd = []

def IterativeDeepiningSearch(start_state, dim):
  state = start_state
  for i in range(1,1000):
    result = DepthLimitedSearch(state,i,i,0,dim)
    if result != "cutoff":
     return result
