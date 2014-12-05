from django import template

register = template.Library()

def fontawesome(icon_name, size=""):
    """
    Generates fontawesome syntax for html.
    
    Usage:

    {% fontawesome "iconname" %}
    {% fontawesome "iconname" "size" %}
    
    size values are:
    lg
    2x
    3x
    4x
    5x
    
    http://fontawesome.io/examples/
    """
    if len(size) > 0:
        size = "fa-%s" % size
    return '<i class="fa fa-%s %s"></i>' % (icon_name, size)


register.simple_tag(fontawesome)
