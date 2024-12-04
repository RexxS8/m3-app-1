from ._anvil_designer import ArticleViewTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ArticleEdit import ArticleEdit


class ArticleView(ArticleViewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def btn_edit_click(self, **event_args):
    # Membuat salinan untuk diedit di form
    copy_article = dict(self.item)

    # Formulir edit artikel
    save_clicked = alert(
        content=ArticleEdit(item=copy_article),
        title="Edit Article",
        large=True,
        buttons=[("Save", True), ("Cancel", False)]
    )
    if save_clicked:
      anvil.server.call('update_article', self.item, copy_article)
      self.refresh_data_bindings()  # Segarkan tampilan data

  def btn_delete_click(self, **event_args):
    delete_clicked = alert(
        title="Do you want to delete?",
        buttons=[("Delete", True), ("Cancel", False)]
    )
    if delete_clicked:
        try:
            anvil.server.call('delete_article', self.item)  # Pastikan self.item adalah LiveObjectProxy
            self.parent.raise_event('x-delete-article')  # Notifikasi penghapusan berhasil
        except Exception as e:
            alert(f"Failed to delete article: {e}")
