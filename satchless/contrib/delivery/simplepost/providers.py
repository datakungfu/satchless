from django.utils.translation import ugettext as _
from satchless.delivery import DeliveryProvider

from . import forms
from . import models

class PostDeliveryProvider(DeliveryProvider):
    def enum_types(self, customer=None, delivery_group=None):
        return ([(t.typ, t.name) for t in models.PostShippingType.objects.all()])

    def get_form(self, delivery_group, typ):
        return forms.PostShippingVariantForm

    def get_variant(self, delivery_group, typ, form):
        typ = models.PostShippingType.objects.get(typ=typ)
        form.save(commit=False)
        variant = form.instance
        variant.name = typ.name
        variant.price = typ.price
        variant.save()
        return variant
