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
    # Konversi LiveObjectProxy menjadi dictionary biasa
    article_dict = dict(article_dict)
    
    # Perbarui kolom update_date
    article_dict['update_date'] = datetime.now()

    # Perbarui baris tabel
    article.update(**article_dict)

@anvil.server.callable
def delete_article(article):
    if app_tables.article.has_row(article):
        article.delete()
    else:
        raise Exception("Article does not exist or has already been deleted")
