from ._anvil_designer import ArticleViewTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ArticleView(ArticleViewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    new_article = {}
    
    save_clicked = alert(
      content= ArticleEdit(item = new_article),
      title="Add Article",
      large=True,
      buttons=[("Save",True),("Cancel",False)]
    )

    if(save_clicked):
      anvil.server.call('add_article', new_article)