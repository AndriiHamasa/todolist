from django import template

register = template.Library()


@register.filter
def get_all_projects(queryset):
    print(type(queryset), queryset)
    print("FROM get_all_projects: ", ", ".join([tag.name for tag in queryset]))
    return ", ".join([tag.name for tag in queryset])
