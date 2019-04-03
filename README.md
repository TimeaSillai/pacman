# pacman
search.py:
• Test solution on more layouts:
python pacman . py -l tinyMaze -p SearchAgent -a fn = dfs
python pacman . py -l mediumMaze -p SearchAgent -a fn = dfs
python pacman . py -l bigMaze -z .5 -p SearchAgent -a fn = dfs

• Similar to DFS, test the code on mediumMaze and bigMaze by using the option −a fn =
bfs
python pacman . py -l mediumMaze -p SearchAgent -a fn = bfs

In search.py, is the implemented uniform-cost graph search algorithm in
uniformCostSearch function
Test it with mediumM aze and bigM aze
python pacman . py -l mediumMaze -p SearchAgent -a fn = ucs

For A*:
python pacman . py -l bigMaze -z .5 -p SearchAgent -a fn = astar ,
heuristic = manhattanHeuristic

Pacman needs to find the shortest path to visit all the corners,
regardless there is food dot there or not. Go to CornersProblem in searchAgents.py and
propose a representation of the state of this search problem. It might help to look at the existing implementation for P ositionSearchP roblem. The representation should include only the
information necessary to reach the goal. Read carefully the comments inside the class CornersProblem.
• Test your implementation with BFS - remember that BFS finds the optimal solution in
number of steps (not necessarilly in cost). The cost for each action is the same for this
problem.
 python pacman . py -l tinyCorners -p SearchAgent -a fn = bfs , prob =
CornersProblem
 python pacman . py -l mediumCorners -p SearchAgent -a fn = bfs , prob =
CornersProblem
Implement a consistent heuristic for CornersProblem. Go to the
function cornersHeuristic in searchAgent.py.
• Test it with
1 $python pacman . py -l mediumCorners -p SearchAgent -a fn =
aStarSearch , prob = CornersProblem , heuristic = cornersHeuristic
 or
 $python pacman . py -l mediumCorners -p AStarCornersAgent -z 0.5
