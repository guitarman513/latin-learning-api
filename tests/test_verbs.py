import pytest

from latin_api.vocabulary.verbs_1c import ALL_ARE_VERBS
from latin_api.models.verbs import PrincipalParts

all_are_verbs_latin = [val for val in  ALL_ARE_VERBS.values()]

@pytest.mark.parametrize('are_verb',all_are_verbs_latin)
def test_are_verb_principal_parts(are_verb):
    _ = PrincipalParts(are_verb)

improper_are_verb_inputs = {
    'bad_love': ('am',),
    'bad_love2': ('amo','amare','amavi','amatu'),
    'bad_love3': ('amo','amare','amavi',),
    'bad_love4': ('amo','amare'),
}

improper_are_verb_inputs = [val for val in  improper_are_verb_inputs.values()]

@pytest.mark.parametrize('bad_input',improper_are_verb_inputs)
def test_exception_are_input(bad_input):
    with pytest.raises(ValueError):
        _ = PrincipalParts(bad_input)