import pytest

from latin_api.models.combiner import random_noun, random_verb, random_conjunction, random_person, random_plurality, random_verb_tense, noun_verb_object, pronoun_verb_only


def test_pronoun(num_loops = 10000):
    for _ in range(num_loops):
        r = pronoun_verb_only(
            verb=random_verb(),
            subject_plurality=random_plurality(),
            subject_person=random_person(),
            verb_tense=random_verb_tense(),
            conjunction='NO',
            second_verb=None
        )
        print(r)

def test_sov(num_loops = 10000):
    for _ in range(num_loops):
        r = noun_verb_object()
        print(r)



if __name__ == '__main__':
    pytest.main([__file__])