from django import template

register = template.Library()

@register.filter(name="Cut")
def Cut(value,arg):
    """
    This cuts out all values of 'arg' from string
    """
    return value.replace(arg,'')

# register.filter('Cut',Cut) #first arg is what u want to say it and second is function name
