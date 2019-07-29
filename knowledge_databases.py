from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, title, rating):
	arc_obj = Knowledge(
		arc_topic=topic,
		arc_title=title,
		arc_rate=rating)
	session.add(arc_obj)
	session.commit()

def query_all_articles():
	print(session.query(Knowledge).all())

def query_article_by_topic(topic):
	article = session.query(Knowledge).filter_by(
		arc_topic=topic).first()
	return article

def query_by_low_rate(threshold):
	articles = session.query(Knowledge).filter_by(
		arc_rate<threshold).all()
	return articles

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(arc_topic=topic).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def edit_article_rating(new_rate, title):
	articles = session.query(Knowledge).filter_by(arc_title=title).all()
	for article in articles:
		article.arc_rate = new_rate
	session.commit()

add_article("123", "abc", 9)
add_article("123", "abc", 9)
add_article("123", "abc", 9)
add_article("123", "abc", 9)
edit_article_rating(8, "abc")
print(query_all_articles())
