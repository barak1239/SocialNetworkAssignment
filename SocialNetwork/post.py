from user import User

class Post(object):
	### need like, comment
	### print info about the post
	def __init__(self, owner: User, *content):
		self.owner = owner
		self.content = content
		self.like_num = 0
		self.comments: list[tuple[str, str]] = []
		self.notify()

	def like(self, user: User):
		self.like_num += 1
		self.owner.get_like(user)

	def comment(self, user: User, comment: str):
		pass

	def notify(self, notification_type: str):
		for observer in self.owner.followers:
			observer.update(self, notification_type)

class TextPost(Post):
	### only contains text 
	### need to print content
	def __init__(self, user: User, content: str):
		super().__init__(user, content)

class ImagePost(Post):
	### contains string with path to the image
	### add show function using matplotlib.plt
	def show(self):
		pass

class SalePost(Post):
	### contains info about the product
	### saler can update post info need password
	### saler can make discount to the product need password
	### need to print if the poduct was soled or not
	def __init__(self, user: User, content: str):
		super().__init__(user, content)

	def discount(self, precent, password):
		pass
	
	def sold(password: str):
		pass