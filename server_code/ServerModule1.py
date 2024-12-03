import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#


@anvil.server.callable
def add_article(article_dic):
  app_tables.article.add_row(create_date= datetime.now(), **article_dic)

@anvil.server.callable
def get_article():
  return app_tables.article.search(tables.order_by("create_date", ascending=False))

@anvil.server.callable
def update_article(article, article_dict):
  if(app_tables.article.has_row(article)):
    article_dict['update_date'] = datetime.now()
    article.update(**article_dict)