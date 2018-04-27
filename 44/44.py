# encoding=utf-8
import pickle


class GameState(object):
	def __init__(self):
		self.level = 0
		self.lives = 4
		self.point = 0


state = GameState()
state.level += 1
state.lives -= 1
state_path = '/tmp/game_state.bin'

state = GameState()
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)

with open(state_path, 'rb') as f:
	state_after = pickle.load(f)
print(state_after.__dict__)

assert isinstance(state_after,GameState)
