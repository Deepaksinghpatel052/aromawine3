import random
import string
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_id_generator(instance):
    order_new_id= random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(Product_id= order_new_id).exists()
    if qs_exists:
        return unique_id_generator(instance)
    return order_new_id


def slug_generator_for_product(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Product_name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Product_slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{rendstr}".format(Product_slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_product(instance,new_slug=new_slug)
    return slug