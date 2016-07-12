"""
    Implementation of the widget
"""


import zope.interface
import zope.component
import zope.schema.interfaces

from z3c.form.browser.multi import MultiWidget
from z3c.form import interfaces
from z3c.form.widget import FieldWidget
from z3c.form.converter import BaseDataConverter


from interfaces import IRawDictField


# ------------[ Main Widget ]-----------------------------------------------

class RawDictField(MultiWidget):
    """This grid should be applied to an schema.List item which has
    schema.Object and an interface"""

    zope.interface.implements(IRawDictField)

    display_table_css_class = "rawdictwidget-table-view"

    klass = "rawdictfield"
    key_type = 'dict'

    def setField(self, value):
        """
            The field information is passed to the widget after it is
            initialised.  Use this call to initialise the column
            definitions.
        """
        self._field = value

    def getField(self):
        return self._field

    field = property(getField, setField)


@zope.component.adapter(zope.schema.interfaces.IField, interfaces.IFormLayer)
@zope.interface.implementer(interfaces.IFieldWidget)
def RawDictFieldFactory(field, request):
    """IFieldWidget factory for DataGridField."""
    return FieldWidget(field, RawDictField(request))


class DictDataConverter(BaseDataConverter):
    """Convert between the context and the widget"""

    zope.component.adapts(zope.schema.interfaces.IList, IRawDictField)

    def toWidgetValue(self, value):
        """Simply pass the data through with no change"""
        return value

    def toFieldValue(self, value):
        return value
