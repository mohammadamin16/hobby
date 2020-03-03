from django import template
from films.imdbDB import search
register = template.Library()


# def add_linebreaks(text):
#     """add lines breaks< <br>, after some chars"""
#
#     return response
#
#
# register.filter('add_linebreaks', add_linebreaks())
