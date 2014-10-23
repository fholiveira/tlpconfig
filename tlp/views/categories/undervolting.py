from ..binders import FreeTextParameterBinder
from tlp.models import TextParameter
from .category import CategoryView


class UndervoltingView(CategoryView):

    def __init__(self, loader, name, category):
        CategoryView.__init__(self, loader, name, category)
        self.value_binders.set_binder_by_type(TextParameter, FreeTextParameterBinder)
