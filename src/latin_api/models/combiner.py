from collections import namedtuple
from random import randint
from typing import Optional, Union

from latin_api.models.grammar import Plurality, Conjunction, pronouns
from latin_api.models.nouns import Noun, Case, NounFirstDeclensionRegular
from latin_api.models.verbs import Verb, VerbTense, Person, VerbFirstConjugationRegular
from latin_api.vocabulary.nouns_1d import ALL_1D_NOUNS
from latin_api.vocabulary.verbs_1c import ALL_ARE_VERBS

transitive_verbs_english_latinpps = [(eng,lat) for eng,lat,is_transitive in ALL_ARE_VERBS if is_transitive]
intransitive_verbs_english_latinpps = [(eng,lat) for eng,lat,is_transitive in ALL_ARE_VERBS if not is_transitive]


Phrase = namedtuple('Phrase',['english','latin'])

def random_verb(transitivity:Optional[bool]=None) -> Verb:
    if transitivity == None:
        all_are_verbs = [(eng,lat) for eng,lat,is_transitive in ALL_ARE_VERBS]
        i = randint(0,len(all_are_verbs)-1)
    elif transitivity == True:
        all_are_verbs = [(eng,lat) for eng,lat,is_transitive in ALL_ARE_VERBS if is_transitive]
        i = randint(0,len(all_are_verbs)-1)
    else:
        all_are_verbs = [(eng,lat) for eng,lat,is_transitive in ALL_ARE_VERBS if not is_transitive]
        i = randint(0,len(all_are_verbs)-1)
    return VerbFirstConjugationRegular(all_are_verbs[i][1], all_are_verbs[i][0])


def random_noun() -> Noun:
    i = randint(0,len(ALL_1D_NOUNS)-1)
    return NounFirstDeclensionRegular(ALL_1D_NOUNS[i][0], ALL_1D_NOUNS[i][1])

def get_pronoun(person:Person, plurality:Plurality) -> str:
    return pronouns[person][plurality]

def random_plurality() -> Plurality:
    i = bool(randint(0,1))
    if i:
        return Plurality.singular
    else:
        return Plurality.plural

def random_verb_tense() -> VerbTense:
    tenses = []
    for t in VerbTense:
        tenses.append(t)
    i = randint(0,len(tenses)-1)
    return tenses[i]

def random_conjunction(optional=True) -> Optional[Conjunction]:
    max_ = 2 if optional else 3
    i = randint(0,max_)
    if i == 0:
        return Conjunction.AND
    elif i == 1:
        return Conjunction.NOT
    elif i == 2:
        return Conjunction.BUT
    else:
        return None

def random_person() -> Person:
    i = randint(0,2)
    if i == 0:
        return Person.first
    elif i == 1:
        return Person.second
    else:
        return Person.third


def noun_verb_object(
    subject:Optional[Noun]=None, 
    transitive_verb:Optional[Verb]=None, 
    object:Optional[Noun]=None,
    subject_plurality:Optional[Plurality]=None, 
    verb_tense:Optional[VerbTense]=None, 
    object_plurality:Optional[Plurality]=None
    ) -> Phrase:
    
    subject = subject if subject else random_noun()
    transitive_verb = transitive_verb if transitive_verb else random_verb(transitivity=True)
    object = object if object else random_noun()

    subject_plurality = subject_plurality if subject_plurality else random_plurality()
    object_plurality = object_plurality if object_plurality else random_plurality()
    verb_tense = verb_tense if verb_tense else random_verb_tense()
    
    subject_english_suffix = 's' if subject_plurality == Plurality.plural else ''
    object_english_suffix = 's' if object_plurality == Plurality.plural else ''
    
    verb_phrase_english = ''
    if verb_tense == VerbTense.present:
        verb_phrase_english = f'{transitive_verb.english_root}s'
    elif verb_tense == VerbTense.imperfect:
        i = randint(0,1)
        verb_phrase_english = f'used to {transitive_verb.english_root}' if i else f'was {transitive_verb.english_root}ing'
    
    english = f'The {subject.english_root}{subject_english_suffix} {verb_phrase_english} the {object.english_root}{object_english_suffix}.'
    latin = f'{subject.decline(Case.nominative, subject_plurality)} {object.decline(Case.accusative, object_plurality)} {transitive_verb.conjugate(verb_tense, Person.third, subject_plurality)}'
    return Phrase(english=english, latin=latin)


#TODO: implement conjunction
def pronoun_verb_only(
    verb:Optional[Verb]=None, 
    subject_plurality:Optional[Plurality]=None, 
    subject_person:Optional[Person]=None,
    verb_tense:Optional[VerbTense]=None, 
    conjunction:Union[Optional[Conjunction],str] = 'NO',
    second_verb:Optional[Verb]=None, # need conjunction of and or but for this to be implemented
    ) -> Phrase:
    
    verb = verb if verb else random_verb()
    subject_plurality = subject_plurality if subject_plurality else random_plurality()
    verb_tense = verb_tense if verb_tense else random_verb_tense()
    subject_person = subject_person if subject_person else random_person()
    pronoun = get_pronoun(subject_person, subject_plurality)

    if conjunction == 'NO' or conjunction == None:
        conjunction = None
    else:
        conjunction = conjunction if conjunction else random_conjunction()

    if conjunction == Conjunction.AND or conjunction == Conjunction.BUT:
        second_verb = second_verb if second_verb else random_verb()

    verb_phrase_english = ''
    if verb_tense == VerbTense.present:
        if second_verb:
            verb_phrase_english = f'{verb.english_root}s {second_verb.english_root}s'
        else:
            verb_phrase_english = f'{verb.english_root}s'
    elif verb_tense == VerbTense.imperfect:
        i = randint(0,1)
        if second_verb:
            verb_phrase_english = f'used to {verb.english_root} and {second_verb.english_root}' if i else f'was {verb.english_root}ing and {second_verb.english_root}ing'
        else:
            verb_phrase_english = f'used to {verb.english_root}' if i else f'was {verb.english_root}ing'

    english = f'{pronoun} {verb_phrase_english}.'
    latin = f'{verb.conjugate(verb_tense, subject_person, subject_plurality)} et {second_verb.conjugate(verb_tense, subject_person, subject_plurality)}' if second_verb else f'{verb.conjugate(verb_tense, subject_person, subject_plurality)}'
    return Phrase(english=english, latin=latin)
