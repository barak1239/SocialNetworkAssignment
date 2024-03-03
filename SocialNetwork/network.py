from .user import User
from .singleton import Singleton

class SocialNetwork(object):
	### need to make as singelton
	__metaclass__ = Singleton
	
	def __init__(self, name: str):
			self.name = name
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
		string = f"{self.name} social network:\n"
		for user in User.users:
			user = User.users[user]
			string += f"{user}"
		return string

