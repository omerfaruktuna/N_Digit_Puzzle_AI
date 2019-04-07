
from breadthfirstsearch import *
from depthfirstsearch import *
from uniformcostsearch import *
from depthlimitedsearch import *
from depthfirstsearch_Recursion import *
from iterativedeepiningsearch import *
from n_digit_puzzle import Node_Graph
from time import time

problem = []

question_file = open('question.txt', 'r')

content = [line.strip() for line in question_file.readlines()]

question_file.close()

puzzle_dimension = int(content[0])


print("Initial problem based on input is: ")

for i in range(1,puzzle_dimension+1):
  print(content[i])

for i in range(1,puzzle_dimension+1):
  puzzle_row = content[i]
  for j in range(puzzle_dimension):
    puzzle_numbers = puzzle_row.split(" ")
    problem.append(int(puzzle_numbers[j]))

main_loop = True

while main_loop:

  print("\n")
  print("Which algorithm do you chose?")
  print ("1 - Breadth First Search")
  print ("2 - Depth First Search")
  print ("3 - Uniform Cost Search")
  print ("4 - Depth Limited Search")
  print ("5 - Iterative Deepining Search")
  print ("6 - Depth First Search (With Recursion)")
  print("Or press 0 to exit")
  answer = int(input())

  if answer == 1:
    print("Running Breadth First Search Algorithm...")
    tic=time()
    answer=BreadthFirstSearch(problem,puzzle_dimension)
    tac=time()
    toe = tac - tic
    print('Solution path:')
    print(answer)
    print('Time spent for solving the puzzle is {:.5f} sec.'.format(toe))

  elif answer == 2:

    print("Running Depth First Search Algorithm...")
    tic=time()
    answer=DepthFirstSearch(problem,puzzle_dimension)
    tac=time()
    toe = tac - tic
    print('Solution path:')
    print(answer)
    print('Time spent for solving the puzzle is {:.5f} sec.'.format(toe))

  elif answer == 3:

    print("Running Uniform Cost Search Algorithm...")
    tic=time()
    answer=UniformCostSearch(problem,puzzle_dimension)
    tac=time()
    toe = tac - tic
    print('Solution path:')
    print(answer)
    print('Time spent for solving the puzzle is {:.5f} sec.'.format(toe))

  elif answer == 4:

    depth_parameter = int(input("Please enter desired depth: "))

    print("Depth Limited Search Algorithm...")
    tic=time()
    answer=DepthLimitedSearch(problem,depth_parameter,depth_parameter,0,puzzle_dimension)
    tac=time()
    toe = tac - tic
    print('Solution path:')
    print(answer)
    print('Time spent for solving the puzzle is {:.5f} sec.'.format(toe))

  elif answer == 5:

    print("Iterative Deepining First Search Algorithm")
    tic=time()
    answer=IterativeDeepiningSearch(problem,puzzle_dimension)
    tac=time()
    toe = tac - tic
    print('Solution path:')
    print(answer)
    print('Time spent for solving the puzzle is {:.5f} sec.'.format(toe))

  elif answer == 6:

    print("Running Depth First Search Algorithm With Recursion...")
    tic=time()
    answer=DepthFirstSearch_Recursion(problem,0,puzzle_dimension)
    print(answer)
    tac=time()
    toe = tac - tic
    print('Solution path:')
    print('Time spent for solving the puzzle is {:.5f} sec.'.format(toe))

  elif answer == 0:
    print("Goodbye")
    main_loop = False
  else:
    print("Unknown choice. Please type your choice again!")
