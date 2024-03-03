import matplotlib.pyplot as plt 
import matplotlib.image as img 

class Post(object):
	### post is an event for the observer
	### total of three events (1) posting new post (2) liking post (3) comment on post
	### the observer is the user
	def __init__(self, owner):
		self.owner = owner
		self.like_num = 0
		self.comments: list[tuple[str, str]] = []
		self.notify("new", self.owner, self.owner.followers)

	def like(self, user):
		self.like_num += 1
		print(f"notification to {self.owner.username}: {user.username} liked your post")
		self.notify("like", user, [self.owner])

	def comment(self, user, comment: str):
		self.comments.append((user.username, comment))
		print(f"notification to {self.owner.username}: {user.username} commented on your post: {comment}")
		self.notify("comment", user, [self.owner])

	def notify(self, type0: str, sender, recivers: list):
		for reciver in recivers:
			if reciver != sender:
				reciver.notification(type0, sender)

class TextPost(Post):
	### only contains text 
	### need to print content
	def __init__(self, user, content: str):
		super().__init__(user)
		self.content = content
		print(f"{self.owner.username} published a post:\n{self.content}\n")
	
	def __str__(self) -> str:
		return f"{self.owner.username} published a post:\n{self.content}\n"


class ImagePost(Post):
	### contains string with path to the image
	### add show function using matplotlib.plt
	def __init__(self, user, path: str):
		super().__init__(user)
		self.path = path
		print(self)
	
	def display(self):
		try:
			print("Shows picture")
			image = img.imread(self.path)
			plt.imshow(image)
		except Exception:
			pass
	
	def __str__(self):
		return f"{self.owner.username} posted a picture\n"

class SalePost(Post):
	### contains info about the product
	### saler can update post info need password
	### saler can make discount to the product need password
	### need to print if the poduct was soled or not
	def __init__(self, user, item, price, location):
		super().__init__(user)
		self.item = item
		self.price = price
		self.location = location
		self.status = "For sale"
		print(self)

	def discount(self, precent, password):
		if password == self.owner.password:
			self.price -= self.price * (precent / 100)
			print(f"Discount on {self.owner.username} product! the new price is: {self.price:.1f}")
	
	def sold(self, password: str):
		if password == self.owner.password:
			print(f"{self.owner.username}'s product is sold")
			self.status = "Sold"

	def __str__(self):
		return f"{self.owner.username} posted a product for sale:\n{self.status}! {self.item}, price: {self.price:.1f}, pickup from: {self.location}\n"