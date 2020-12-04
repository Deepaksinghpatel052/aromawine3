import random
import string
from django.utils.text import slugify

def random_string_generator(size=5, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_id_generator_for_CouponCode(instance):
    order_new_id= random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(CouponCode= order_new_id).exists()
    if qs_exists:
        return unique_id_generator_for_CouponCode(instance)
    return order_new_id



def slug_generator_for_eventType(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Type)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_eventType(instance,new_slug=new_slug)
    return slug


def slug_generator_for_event(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Event_name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_event(instance,new_slug=new_slug)
    return slug


def unique_id_generator(instance):
    order_new_id= random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(Product_id= order_new_id).exists()
    if qs_exists:
        return unique_id_generator(instance)
    return order_new_id



def unique_id_generator_for_order(instance):
    order_new_id= random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(order_id= order_new_id).exists()
    if qs_exists:
        return unique_id_generator(instance)
    return order_new_id

def slug_generator_for_color(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Color_name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_color(instance,new_slug=new_slug)
    return slug



def slug_generator_for_AwRegion(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Region_Name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_AwRegion(instance,new_slug=new_slug)
    return slug


def slug_generator_for_AwCmsPaage(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_AwVarietals(instance,new_slug=new_slug)
    return slug


def slug_generator_for_AwVarietals(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Varietals_Name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_AwVarietals(instance,new_slug=new_slug)
    return slug



def slug_generator_for_AwVintages(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Vintages_Year)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_AwVintages(instance,new_slug=new_slug)
    return slug

def slug_generator_for_AwCountry(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Country_Name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_AwCountry(instance,new_slug=new_slug)
    return slug



def slug_generator_for_AwGrape(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Grape_Name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_AwGrape(instance,new_slug=new_slug)
    return slug


def slug_generator_for_AwClassification(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Classification_Name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_AwClassification(instance,new_slug=new_slug)
    return slug

def slug_generator_for_AwTesting(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_AwTesting(instance,new_slug=new_slug)
    return slug

def slug_generator_for_AAwDinner(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Dinner_Name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_AAwDinner(instance,new_slug=new_slug)
    return slug


def slug_generator_for_AwProducers(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Winnery_Name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_AwProducers(instance,new_slug=new_slug)
    return slug

def slug_generator_for_AwSize(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Bottle_Size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_AwSize(instance,new_slug=new_slug)
    return slug

def slug_generator_for_AwAppellation(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Appellation_Name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Slug=slug).exists()
    if qs_exists:
        new_slug = "{Slug}-{rendstr}".format(Slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_AwAppellation(instance,new_slug=new_slug)
    return slug


def slug_generator_for_product(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.Product_name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(Product_slug=slug).exists()
    if qs_exists:
        new_slug = "{Product_slug}-{rendstr}".format(Product_slug=slug,rendstr=random_string_generator(size=4))
        return slug_generator_for_product(instance,new_slug=new_slug)
    return slug