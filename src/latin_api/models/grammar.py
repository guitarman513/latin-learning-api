from enum import Enum
from collections import namedtuple

class Plurality(str, Enum):
    singular = 'singular'
    plural = 'plural'

class Person(str, Enum):
    first = 'first'
    second = 'second'
    third = 'third'

class Case(str, Enum):          # mensa
    nominative = 'nominative'   # Table (subject)
    vocative = 'vocative'       # O table! (addressing)
    accusative = 'accusative'   # Table (object)
    genitive = 'genitive'       # Of a table
    dative = 'dative'           # To or for a table
    ablative = 'ablative'       # By, with, or from a table

_Conjunction = namedtuple('Conjunction',['english','latin'])
class Conjunction(Enum):
    AND = _Conjunction('and', 'et')
    BUT = _Conjunction('but', 'sed')
    NOT = _Conjunction('not', 'non')

pronouns = {
    Person.first:  {Plurality.singular: 'I', Plurality.plural: 'We'},
    Person.second: {Plurality.singular: 'You', Plurality.plural: "Y'all"},
    Person.third:  {Plurality.singular: 'He', Plurality.plural: "They"},    # TODO: random for the girl, the girls, etc
}