from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	__tablename__ = 'knowledge'
	arc_id = Column(Integer, primary_key=True)
	arc_topic = Column(String)
	arc_title = Column(String)
	arc_rate = Column(Float)

	def __repr__(self):
		if 1:#self.arc_rate > 7:
			return ("If you want to learn about {}, you should look at the Wikipedia article called {}. We gave this article a rating of {} out of 10! The ID of this instance is {}").format(
						self.arc_topic,
						self.arc_title,
						self.arc_rate,
						self.arc_id)

		else:
			return "Unfortunately, this article does not have a better rating. Maybe, this is an article that should be replaced soon!"