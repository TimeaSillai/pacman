# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
#2.9

class CustomNode:
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost
    def getName(self):
   	return self.name
    def getCost(self):
   	return self.cost

class Node:
    def __init__(self,state,parent,action,path_cost):
        self.state=state
        self.parent=parent
        self.action=action
        self.path_cost=path_cost
    def getState(self):
  	return self.state
    def getParent(self):
   	return self.parent
    def getAction(self):
   	return self.action
    def getPath_Cost(self):
   	return self.path_cost
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def randomSearch(problem):
    current=problem.getStartState()
    solution=[]
    while(not(problem.isGoalState(current))):
	succ=problem.getSuccessors(current)
    	no_of_successors=len(succ)
        random_succ_index=int(random.random()*no_of_successors)  # type: int
    	next=succ[random_succ_index]
    	current=next[0]
   	solution.append(next[1])
    print "The solution is",solution
    return solution

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    2.5
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    2.6
    lista=problem.getSuccessors(problem.getStartState())
    for element in lista:
        print "state", element[0]
    print "action", element[1]
        print "cost", element[2]
    """

    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    2.7
    """from  game  import  Directions
    w = Directions.WEST
    return [w, w]
    2.8
    lista=problem.getSuccessors(problem.getStartState())
    return lista[0][1],lista[1][1] """
    #from util import Stack:
    #el1=Random_structure('el1',5)
    #el2=Random_structure('el2',5)
    """
    #2.9
    node1 = CustomNode("first", 3) # creates a new  object
    node2 = CustomNode("second", 10)
    print "Create a stack"
    my_stack = util.Stack () # creates a new  object  of the  class  Stack defined  in file  util.py
    print "Push the new node into the stack"
    my_stack.push(node1)
    my_stack.push(node2)
    print "Pop an element from the stack"
    extracted = my_stack.pop() # call a method  of the  object
    print "Extracted node is ", extracted.getName(), " ", extracted.getCost()
    util.raiseNotDefined()
    """
    from util import Stack
    frontiera=Stack()
    node1=Node(problem.getStartState(),[],[],0)
    #a=Node(problem.getStartState(),[],[],0)
    frontiera.push(node1)
    explored=set()
    while not(frontiera.isEmpty()):
        node2=frontiera.pop()
	#explored.add(node2.state)
        if problem.isGoalState(node2.state):
            return node2.action 
	if node2.state not in explored:
    		explored.add(node2.state)
    		for k in problem.getSuccessors(node2.state):
			if k[0] not in explored:
				child=Node(k[0],node2.getState(),node2.action+[k[1]],1)
    				frontiera.push(child)
    

    util.raiseNotDefined()
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    frontiera=Queue()
    node1=Node(problem.getStartState(),[],[],0)
    frontiera.push(node1)
    explored=[]
    if problem.isGoalState(node1.state):
    	return node1.action
    while not(frontiera.isEmpty()):
    	node2=frontiera.pop()
    	explored.append(node2.getState())
        if problem.isGoalState(node2.state):
    		return node2.action
    	for i in problem.getSuccessors(node2.state):
    		child=Node(i[0],node2.getState(),node2.action+[i[1]],1)
    		if child.state not in explored:
    			explored.append(child.getState())
    			frontiera.push(child)
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    frontiera = PriorityQueue()
    explored = []
    actions = []
    node1 = (problem.getStartState(), actions, 0)
    frontiera.push(node1,0)

    while not(frontiera.isEmpty()):
        node2 = frontiera.pop()
        if problem.isGoalState(node2[0]):
            return node2[1]
        if node2[0] not in explored:
            explored.append(node2[0])
            for succNode in problem.getSuccessors(node2[0]):
                actions = node2[1] + [succNode[1]]
                cost = node2[2] + succNode[2]
                frontiera.push((succNode[0], actions, cost), cost)
    util.raiseNotDefined()
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    frontiera = PriorityQueue()
    explored = []
    actions = []
    node1 = (problem.getStartState(), actions, 0)
    frontiera.push(node1,heuristic(problem.getStartState(), problem))

    while not(frontiera.isEmpty()):
        node2 = frontiera.pop()
        if problem.isGoalState(node2[0]):
            return node2[1]
        if node2[0] not in explored:
            explored.append(node2[0])
            for succNode in problem.getSuccessors(node2[0]):
                actions = node2[1] + [succNode[1]]
                cost = node2[2] + succNode[2]
                frontiera.push((succNode[0], actions, cost),cost+heuristic(succNode[0], problem))
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
rs=randomSearch
