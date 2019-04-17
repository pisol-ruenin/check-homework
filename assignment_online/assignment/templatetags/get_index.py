from django import template

register = template.Library()

@register.filter
def get_at_index(list, index):
    return list[index].txt

@register.filter
def get_choice(list,index):
    return list[index].choice_no.no

@register.filter
def get_answer(list,index):
    if list is None:
        return 'X'
    return list[index].answer_choice

@register.filter
def get_pk(list,index):
    return list[index].pk