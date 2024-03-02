from post import Post, TextPost, ImagePost, SalePost

class User(object):
	
	users = {}
	
	def __new__(cls, username, password):
		try:
			user: User = cls.users[username]
			assert user.password == password
			return user
		except KeyError:
			return super().__new__(cls)
		except Exception:
			return None
	
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.logged_in = True
		self.followers = []
		self.notifications = []
		User.users[username] = self

	def follow(self, user):
		if self.logged_in and self not in user.followers:
			user.followers.append(self)
			print(f"{self} started following {user}")

	def unfollow(self, user):
		if self.logged_in:
			try:
				user.followers.remove(self)
				print(f"{self} unfollowed {user}")
			except Exception:
				pass
	
	def update(self, post):
		pass
	
	def print_notifications(self):
		pass

	def publish_post(self, post_type: str, *content) -> Post:
		# factory
		posts = {
			"Text": TextPost, 
			"Image": ImagePost,
			"Sale": SalePost
		}
		return posts[post_type](*content)

	def __str__(self):
		return f"{self.username}"

