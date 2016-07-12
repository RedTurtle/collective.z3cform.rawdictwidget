# collective.z3cform.rawdictwidget

# To add in z3c schema
```python
from plone.autoform import directives
from collective.z3cform.rawdictwidget import RawDictWidgetFactory

class IExampleDexterityContent(model.Schema, IImageScaleTraversable):
    directives.widget('example_field', RawDictWidgetFactory)
    example_field = schema.Dict(
        title=_(u'Example field'),
        readonly=True,  # to make the field readonly, and possible to set using some event based code or method. that is normally the use case
        required=False)
```