import pytest

from latin_api.vocabulary.nouns_1d import ALL_1D_NOUNS
from latin_api.models.nouns import NounFirstDeclensionRegular, Plurality, Case

@pytest.mark.parametrize(['english','latin'],ALL_1D_NOUNS)
def test_noun_list(english, latin):
    _ = NounFirstDeclensionRegular(english_root=english, latin_genitive_singular=latin)


def test_declension():
    girl = NounFirstDeclensionRegular('girl','puellae')
    assert girl.decline(Case.nominative, Plurality.singular) == 'puella'
    assert girl.decline(Case.nominative, Plurality.plural) == 'puellae'

    assert girl.decline(Case.vocative, Plurality.singular) == 'puella'
    assert girl.decline(Case.vocative, Plurality.plural) == 'puellae'

    assert girl.decline(Case.accusative, Plurality.singular) == 'puellam'
    assert girl.decline(Case.accusative, Plurality.plural) == 'puellas'

    assert girl.decline(Case.genitive, Plurality.singular) == 'puellae'
    assert girl.decline(Case.genitive, Plurality.plural) == 'puellarum'

    assert girl.decline(Case.dative, Plurality.singular) == 'puellae'
    assert girl.decline(Case.dative, Plurality.plural) == 'puellis'

    assert girl.decline(Case.ablative, Plurality.singular) == 'puella'
    assert girl.decline(Case.ablative, Plurality.plural) == 'puellis'


if __name__ == '__main__':
    pytest.main([__file__])