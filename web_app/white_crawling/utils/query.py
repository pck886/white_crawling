# -*- coding: utf-8 -*-
# Author: chanlee(pck886@gmail.com)

from django.forms import model_to_dict


def item_to_model(item):
    model_class = getattr(item, 'django_model')
    if not model_class:
        raise TypeError("Item is not a `DjangoItem` or is misconfigured")

    return item.instance


def get_or_create(model):
    model_class = type(model)

    print("============= MODEL_CLASS %s" % model_class)
    print("============= MODEL %s" % model)
    print("============= MODEL %s" % model.title)

    created = False

    # Normally, we would use `get_or_create`. However, `get_or_create` would
    # match all properties of an object (i.e. create a new object
    # anytime it changed) rather than update an existing object.
    #
    # Instead, we do the two steps separately
    try:
        # We have no unique identifier at the moment; use the name for now.
        obj = model_class.objects.get(title=model.title)
    except model_class.DoesNotExist:
        created = True
        obj = model  # DjangoItem created a model for us.

    return obj, created


def update_model(destination, source, commit=True):
    pk = destination.pk

    source_dict = model_to_dict(source)
    for (key, value) in source_dict.items():
        print('============ KEY : %s' % key)
        print('============ VALUE : %s' % value)

        setattr(destination, key, value)

    setattr(destination, 'pk', pk)

    if commit:
        destination.save()

    return destination
