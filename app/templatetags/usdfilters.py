from django import template

register = template.Library()


@register.filter(name='swapping')
def swap(value):
    return value.swapcase()


@register.filter()
def remove(value, arg):
    return value.replace(arg, '')


@register.filter()
def counting(value, arg):
    c = 0
    for i in range(len(value)):
        if arg == value[i:i+len(arg):]:
            c+=1
    return c


@register.filter(name='splitting')
def split(value):
    return value.split()


@register.filter()
def index(value, arg):
    for i in range(len(value)):
        if value[i]==arg:
            return i
  
      
@register.filter(name='dupliremove')        
def duplicate(value):
    ss = ''
    for i in value:
        if i not in ss:
            ss+=i
    return ss

@register.filter()
def countconst(value):
    v='AEIOUaeiou'
    c=0
    for i in value:
        if i not in v:
            c+=1
    return c


@register.filter()
def countvowel(value):
    v='AEIOUaeiou'
    c=0
    for i in value:
        if i in v:
            c+=1
    return c