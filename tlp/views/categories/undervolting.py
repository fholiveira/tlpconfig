from tlp.views.binders import ParameterBinderSelector
from tlp.views.binders import FreeTextParameterBinder
from tlp.models import TextParameter
from .category import CategoryView


class UndervoltingView(CategoryView):
    def create_selector(self):
        selector = ParameterBinderSelector()
        selector.set_binder_by_type(TextParameter, FreeTextParameterBinder)
        return selector
