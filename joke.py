import praw
import os

class Joke():
	"""
		using the reddit wrapper to pull a joke
		members
		ci: client id
		cs: client secret
		ua: user agent

		these are pulled from enviornment variables
		so remeber to set them.
	"""
	client_id = None 
	client_secret = None 
	user_agent = None
	reddit = None

	def __init__(self):

		"""
			load the auth information from the
			enviornment.
			Try to build a reddit instance based
			on that information
		"""
		self.ci =(os.environ['R_CI'])
		self.cs =(os.environ['R_CS'])
		self.ua =(os.environ['R_UA'])
		self._get_reddit_instance()

	def _get_reddit_instance(self):
		self.reddit = praw.Reddit(client_id=self.ci,
							 client_secret=self.cs,
                     		 user_agent=self.ua
                     )
	def GetJokePair(self):
		"""
			if the reddit object is not None
			then we return a joke pair
		"""
		try:
			result = {"joke":"","punch_line":""}
			while(result["punch_line"] is None or result["punch_line"] == ""):
				sub = self.reddit.subreddit('DMDadJokes').random()
				result = {"joke":sub.title,
					  	  "punch_line":sub.selftext}
			return result
		except:
			raise Exception("unable to generate Joke")