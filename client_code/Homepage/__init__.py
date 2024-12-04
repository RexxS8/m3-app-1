from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ArticleEdit import ArticleEdit

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    anvil.users.login_with_form()
    self.repeating_panel.set_event_handler('x-delete-article', self.delete_article)
    self.refresh_articles()

  def add_article_btn_click(self, **event_args):

    new_article = {}
    
    save_clicked = alert(
      content= ArticleEdit(item = new_article),
      title="Add Article",
      large=True,
      buttons=[("Save",True),("Cancel",False)]
    )

    if(save_clicked):
      anvil.server.call('add_article', new_article)
      self.refresh_articles()
      
  def refresh_articles(self):
    self.repeating_panel.items = anvil.server.call('get_article')

  def delete_article(self,article, **event_args):
    self.refresh_articles()