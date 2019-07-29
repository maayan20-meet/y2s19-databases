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
	articles = session.query(Knowledge).all()

	res_list = list(articles)

	for i in articles:
		if i.arc_rate >= threshold:
			res_list.remove(i)
 
	return res_list

def query_article_by_primary_key(key):
	article = session.query(Knowledge).filter_by(arc_id=key).first()
	return article

def query_top_five():
	articles = session.query(Knowledge).all()
	res_list = list()

	articles.sort(key=extract_rating, reverse=True)

	for i in range(5):
		res_list.append(articles[i])

	return res_list


def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(arc_topic=topic).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def delete_article_by_rating(threshold):
	articles = query_by_low_rate(threshold)

	for i in articles:
		session.query(Knowledge).filter_by(arc_id=i.arc_id).delete()

	session.commit()


def edit_article_rating(new_rate, title):
	articles = session.query(Knowledge).filter_by(arc_title=title).all()
	for article in articles:
		article.arc_rate = new_rate
	session.commit()

def edit_by_avrege(new_rate, title):
	articles = session.query(Knowledge).filter_by(arc_title=title).all()
	for article in articles:
		article.arc_rate *= new_rate
		article.arc_rate /= 2
	session.commit()

def extract_rating(article):
	return article.arc_rate

# add_article("a", "a", 3)
# add_article("b", "b", 4)
# add_article("c", "c", 5)
# add_article("d", "d", 6)
# add_article("e", "e", 7)
# add_article("f", "f", 8)

print(query_all_articles())
