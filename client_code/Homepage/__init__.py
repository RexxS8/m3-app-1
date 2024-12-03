from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ArtcileEdit import ArtcileEdit

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_artcile_btn_click(self, **event_args):

    new_arcticle = {}
    
    save_clicked = alert(
      content= ArtcileEdit(item = new_arcticle),
      title="Add Article",
      large=True,
      buttons=[("Save",True),("Cancel",False)]
    )

    if(save_clicked):
      print(new_arcticle)
