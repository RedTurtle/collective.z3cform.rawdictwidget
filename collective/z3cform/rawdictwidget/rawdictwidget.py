"""
    Implementation of the widget
"""


import zope.interface
import zope.component
import zope.schema.interfaces
from z3c.form.widget import Widget
from z3c.form import interfaces
from z3c.form.widget import FieldWidget
from z3c.form.converter import BaseDataConverter
from zope.schema.interfaces import IDict
from interfaces import IRawDictWidget
import ast

# ------------[ Main Widget ]-----------------------------------------------


class RawDictField(Widget):
    """Is general widget that is extended"""

    zope.interface.implements(IRawDictWidget)

    display_table_css_class = "rawdictwidget-table-view"

    klass = "rawdictfield"
    viewonly = True

    def extract(self):
        # import pdb;pdb.set_trace()
        val = self.request.get(self.name, getattr(self.context, self.field.getName()))
        return ast.literal_eval(str(val))

    def update(self):
        """
        """
        # import pdb;pdb.set_trace()
        self.value = self.extract()


@zope.component.adapter(IDict)
@zope.interface.implementer(interfaces.IFieldWidget)
def RawDictWidgetFactory(field, request):
    """IFieldWidget factory for DataGridField."""
    widget = FieldWidget(field, RawDictField(request))
    # widget.template = Z3ViewPageTemplateFile("templates/rawdictwidget_input.pt")
    return widget


class DictDataConverter(BaseDataConverter):
    """Convert between the context and the widget"""

    zope.component.adapts(IDict, IRawDictWidget)

    def toWidgetValue(self, value):
        """Simply pass the data through with no change"""
        return value

    def toFieldValue(self, value):
        return value
