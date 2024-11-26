import time
from collections import deque
# first we have the grid size : n
# third we get the distination point
def main():	
	global grid 
	global paths
	global movements
	paths = []
	q = deque()
	starting_cords = (24,15	,0,"")
	ending_cords = (46,102)
	grid = 150

	#starting_cords = (0,3,0,"")
	#ending_cords = (4,3)
	#grid = 7

#	starting_cords = (5,1,0,"")
#	ending_cords = (0,5)
	movements  = [UL,UR,R,LR,LL,L]

	grid = grid - 1
	q += [starting_cords]
	step = 1



	play(q , ending_cords , set() )
#	(play(q , ending_cords,movements, 0 , set() ))
#	(play(q , ending_cords,movements, 0 , set() ))
#	(play(q , ending_cords,movements, 0 , set() ))
#	(play(q , ending_cords,movements, 0 , set() ))
#	print(f"list of paths = {paths}")
			


def compare(m1 , m2):
	if m1 == m2 :
			return 0
	if m1 == "UL":
		return m1
	if m2 == "UL":
		return m2
	
	if m1 == "UR":
		return m1
	if m2 == "UR":
		return m2
	
	if m1 == "R":
		return m1
	if m2 == "R":
		return m2
	
	if m1 == "LR":
		return m1
	if m2 == "LR":
		return m2

	if m1 == "LL":
		return m1
	if m2 == "LL":
		return m2

	if m1 == "L":
		return m1
	if m2 == "L":
		return m2

def compareMoves(paths):
	if len(paths) == 2:
		for i in range(len(paths[0])):
			rs_one_move = compare(paths[0][i], paths[1][i]) 

			if rs_one_move == 0 :
				continue
			else :
				if rs_one_move == paths[0][i]:
					return paths[0]
				else :
					return paths[1]
	return compareMoves(paths[1:])


def destination(res_i , res_j ):
	if res_i < 0 or res_j < 0:
		return ()	
	elif res_i > grid or res_j > grid:
		return ()
	else:
		return (res_i, res_j)

def UL(i,j):
	res_i = i-2	
	res_j = j-1
	return destination(res_i, res_j) 
def UR(i,j):
	res_i = i-2
	res_j = j+1
	return destination(res_i, res_j) 
def R(i,j):
	res_i = i 
	res_j = j+2
	return destination(res_i, res_j) 
def LR(i,j):
	res_i = i+2
	res_j = j+1
	return destination(res_i, res_j) 
def LL(i,j):
	res_i = i+2
	res_j = j-1
	return destination(res_i, res_j) 
def L(i,j):
	res_i = i
	res_j = j-2
	return destination(res_i, res_j) 
# fourth we start moving in the grid with the movements : 
paths = []	
def play(q, ending_cords, explored_paths = set() ):
	if len(q) == 0:
		print("Impossible")
		return 
	starting_cords = q.popleft()
	if starting_cords[0:2] in explored_paths:
		return play(q,ending_cords, explored_paths)
	
	if starting_cords[0:2] == ending_cords:	
		return steps

	else :
		explored_paths.add(starting_cords[0:2])
		npaths = 0
		recorded_paths = []
		for move in movements:
			cord = move(starting_cords[0],starting_cords[1]) 
			if cord == ():
				continue
			cord = move(starting_cords[0],starting_cords[1]) + (starting_cords[2]+1 , starting_cords[3]+move.__name__+" ")
			if cord[0:2] == ending_cords :
				npaths = cord[2]
				recorded_paths.append(cord[3].strip())
				continue
			else :
				if not cord[0:2] in explored_paths:
					q+=[cord]
		if len(recorded_paths) >= 2:
			e = [ i.split(" ") for i in recorded_paths ]
			res = ' '.join(compareMoves(e)).strip()
			print(npaths)
			print(res)
			return
		if len(recorded_paths) == 1:
			print(npaths)
			print(recorded_paths[0])
			return


		return play(q, ending_cords, explored_paths )

if __name__ == "__main__":
	main()




