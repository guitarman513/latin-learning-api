import pytest

from latin_api.vocabulary.verbs_1c import ALL_ARE_VERBS
from latin_api.models.verbs import VerbFirstConjugationRegular, VerbTense, Person, Plurality

verbs_and_principal_parts = [(eng, pps) for eng, pps, is_transitive in ALL_ARE_VERBS]

@pytest.mark.parametrize(['english_stem','are_verb_parts'],verbs_and_principal_parts)
def test_are_verb_principal_parts(english_stem, are_verb_parts):
    _ = VerbFirstConjugationRegular(are_verb_parts, english_stem)

improper_are_verb_inputs = {
    'bad_love': ('am',),
    # 'bad_love2': ('amo','amare','amavi','amatu'),
    'bad_love3': ('amo','amare','amavi',),
    'bad_love4': ('amo','amare'),
}


@pytest.mark.parametrize(['english_stem','bad_input'],improper_are_verb_inputs.items())
def test_exception_are_input(english_stem, bad_input):
    with pytest.raises(ValueError):
        _ = VerbFirstConjugationRegular(bad_input, english_stem)



def test_conjugation():
    love = VerbFirstConjugationRegular(('amo',),'love')
    assert love.conjugate(VerbTense.present,Person.first, Plurality.singular) == 'amo'
    assert love.conjugate(VerbTense.present,Person.first, Plurality.plural) == 'amamus'
    assert love.conjugate(VerbTense.present,Person.second, Plurality.singular) == 'amas'
    assert love.conjugate(VerbTense.present,Person.second, Plurality.plural) == 'amatis'
    assert love.conjugate(VerbTense.present,Person.third, Plurality.singular) == 'amat'
    assert love.conjugate(VerbTense.present,Person.third, Plurality.plural) == 'amant'
    
    assert love.conjugate(VerbTense.imperfect,Person.first, Plurality.singular) == 'amabam'
    assert love.conjugate(VerbTense.imperfect,Person.first, Plurality.plural) == 'amabamus'
    assert love.conjugate(VerbTense.imperfect,Person.second, Plurality.singular) == 'amabas'
    assert love.conjugate(VerbTense.imperfect,Person.second, Plurality.plural) == 'amabatis'
    assert love.conjugate(VerbTense.imperfect,Person.third, Plurality.singular) == 'amabat'
    assert love.conjugate(VerbTense.imperfect,Person.third, Plurality.plural) == 'amabant'

    love = VerbFirstConjugationRegular(('amo','amare','amavi','amatum'),'love')
    assert love.conjugate(VerbTense.present,Person.first, Plurality.singular) == 'amo'
    assert love.conjugate(VerbTense.present,Person.first, Plurality.plural) == 'amamus'
    assert love.conjugate(VerbTense.present,Person.second, Plurality.singular) == 'amas'
    assert love.conjugate(VerbTense.present,Person.second, Plurality.plural) == 'amatis'
    assert love.conjugate(VerbTense.present,Person.third, Plurality.singular) == 'amat'
    assert love.conjugate(VerbTense.present,Person.third, Plurality.plural) == 'amant'

    assert love.conjugate(VerbTense.imperfect,Person.first, Plurality.singular) == 'amabam'
    assert love.conjugate(VerbTense.imperfect,Person.first, Plurality.plural) == 'amabamus'
    assert love.conjugate(VerbTense.imperfect,Person.second, Plurality.singular) == 'amabas'
    assert love.conjugate(VerbTense.imperfect,Person.second, Plurality.plural) == 'amabatis'
    assert love.conjugate(VerbTense.imperfect,Person.third, Plurality.singular) == 'amabat'
    assert love.conjugate(VerbTense.imperfect,Person.third, Plurality.plural) == 'amabant'

if __name__ == '__main__':
    pytest.main([__file__])