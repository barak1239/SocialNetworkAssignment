from .post import Post, TextPost, ImagePost, SalePost

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
		self.posts = []
		User.users[username] = self

	def follow(self, user):
		if self.logged_in and self not in user.followers:
			user.followers.append(self)
			print(f"{self.username} started following {user.username}")

	def unfollow(self, user):
		if self.logged_in:
			try:
				user.followers.remove(self)
				print(f"{self.username} unfollowed {user.username}")
			except Exception:
				pass
	
	def notification(self, type0, sender):
		if type0 == "new":
			notification = f"{sender.username} has a new post"
		elif type0 == "like":
			notification = f"{sender.username} liked your post"
		elif type0 == "comment":
			notification = f"{sender.username} commented on your post"
		self.notifications.append(notification)
	
	def print_notifications(self):
		print(f"{self.username}'s notifications:")
		for notification in self.notifications:
			print(notification)

	def publish_post(self, post_type: str, *content) -> Post:
		# factory
		posts = {
			"Text": TextPost, 
			"Image": ImagePost,
			"Sale": SalePost
		}
		post = posts[post_type](self, *content)
		self.posts.append(post)
		return post

	def __str__(self):
		return f"User name: {self.username}, Number of posts: {len(self.posts)}, Number of followers: {len(self.followers)}\n"

