from typing import List, Tuple, Dict, Union


# English, principal parts, isTransitive
ALL_ARE_VERBS: List[ Tuple[ str, Union[Tuple[str],Tuple[str,str,str,str]], bool  ] ] = [
    ('love', ('amo',), True),
    ('sail', ('navigo',), False),
    ('build', ('aedifico',), False),
    ('sing', ('canto',), False),
    ('hurry', ('festino',), False),
    ('expect', ('expecto',), True),
    ('work', ('laboro',), False),
    ('attack', ('oppungo',), True),
    ('prepare', ('paro',), False),
    ('fight', ('pugno',), True),
    ('ask', ('rogo',), True),
    ('watch', ('specto',), True),
    ('overcome', ('supero',), True),
    ('call', ('voco',), True),
]



    # 'love2': ('amo','amare','amavi','amatum'),