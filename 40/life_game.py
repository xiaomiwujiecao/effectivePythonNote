# encoding=utf-8
from collections import namedtuple

ALIVE = '*'

EMPTY = '-'

Query = namedtuple('Query',('y','x'))
print(Query)
def count_neighbors(y,x):
	n = yield Query(y+1,x+0)
	m = yield Query(y+1,x+1)
	neighbor_states = [n,ne,e_,se,s_,sw,w_nw]
	count = 0
	for state in neighbor_states:
		if state == ALIVE:
			count+=1
	return count

it = count_neighbors(10,5)
q1 = next(it)
print('First yield',q1)

q2  =it.send(ALIVE)
print('Second yield',q2)
q3 = it.send(ALIVE)

try:
	count = it.send(EMPTY)
except StopIteration as e:
	print('count',e.value)

Transaction= namedtuple('Transaction',('y','x','state'))


def game_logic(state,neighbors):
	if state==ALIVE:
		if neighbors <2:
			return EMPTY
		elif neighbors >3:
			return EMPTY
	else:
		if neighbors==3:
			return ALIVE
	return state


def step_cell(y,x):
	state = yield Query(y,x)
	neighbors = yield from count_neighbors(y,x)
	next_state = game_logic(state,neighbors)
	yield Transaction(y,x,next_state)

it = step_cell(10,5)
q0 = next(it)
print('Me',q0)
q1 = it.send(ALIVE)
print('Q1',q1)
t1 = it.send(EMPTY)
print('Outcome',t1)


TICK = object()

def simulate(height,width):
	while True:
		for y in range(height):
			for x in range(width) :
				yield from step_cell(y,x)
		yield TICK


class Grid(object):
	def __init__(self,height,width):
		self.height = height
		self.width = width
		self.row = []
		for _ in range(self.height):
			self.rows.append([EMPTY]+self.width)

	def __str__(self):
		pass

	def query(self,y,x):
		return self.rows[y%self.height][x%self.width]

	def assign(self,y,x,state):
		self.rows[y%self.height][x%self.width] = state



def live_a_generation(grid,sim):
	progeny = Grid(grid.height,grid.width)
	item = next(sim)
	while item is not TICK:
		if isinstance(item,Query):
			state = grid.query(item.y,item.x)
			item = sim.send(state)
		else:
			progeny.assign(item.y,item.x,item.state)
			item = next(sim)
	return progeny


grid = Grid(5,9)

grid.assign(0,3,ALIVE)

class ColumnPrinter(object):
	pass


columns = ColumnPrinter()
sim = simulate(grid.height,grid.width)
for i in range(5):
	columns.append(str(grid))
	grid = live_a_generation(grid,sim)


print(columns)

