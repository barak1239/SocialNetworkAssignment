from user import User
from post import Post
from singleton import Singleton

class SocialNetwork(object):
	### need to make as singelton
	__metaclass__ = Singleton
	
	def __init__(self, name: str):
			self.name = name
			self.posts: list[Post] = []
			print(f"The social network {self.name} was created!")
	
	def sign_up(self, username: str, password: str) -> User:
		if username not in User.users:
			return User(username, password)
	
	def log_in(self, username: str, password: str) -> User:
		try:
			user: User = User.users[username]
			assert user.password == password
			user.logged_in = True
		except Exception:
			pass
	
	def log_out(self, username: str):
		try:
			user: User = User.users[username]
			user.logged_in = False
		except Exception:
			pass
	
	def __str__(self) -> str:
		#TODO
		return ""

# class SocialNetwork:
#     _instance = None
#     users =  {}
#     networkName = ' '
#     def new(self, networkName):
#         pass
