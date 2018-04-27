# encoding=utf-8
import copyreg
import pickle


class GameState(object):
	def __init__(self,level=0,lives=4,points=0,magic=5):
		self.level = level
		self.lives = lives
		self.points = points
		self.magic = magic

def pickle_game_state(game_state):
	kwargs = game_state.__dict__
	return unpickle_game_state,(kwargs,)

def unpickle_game_state(kwargs):
	return GameState(**kwargs)

copyreg.pickle(GameState,pickle_game_state)

state = GameState()
state.level += 1
state.lives -= 1
state_path = '/tmp/game_state.bin'


state = GameState()
state.points+=1000
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)

with open(state_path, 'rb') as f:
	state_after = pickle.load(f)
print(state_after.__dict__)

assert isinstance(state_after,GameState)
