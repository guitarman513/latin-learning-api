from typing import Tuple, List
from enum import Enum


class Verb:
    class Type(str, Enum):
        are = 'are'

    def __init__(self) -> None:
        pass


class PrincipalParts:
    def __init__(self, base_principal_parts:Tuple[str], category:Verb.Type=Verb.Type.are) -> None:
        self.verb_category:Verb.Type = category
        if len(base_principal_parts) == 1:
            self.one_present_1ps, self.two_infinitive, self.three_perfect_1ps, self.four_supine = self._get_principle_parts_from_1ps(base_principal_parts)
        elif len(base_principal_parts) == 4:
            self.one_present_1ps, self.two_infinitive, self.three_perfect_1ps, self.four_supine = base_principal_parts
        else:
            raise ValueError("base_principal_parts must either be first person singular or all four principal parts.")
        self._validate_all_four_base_principal_parts()

    def _get_principle_parts_from_1ps(self, base_principal_parts:Tuple[str]) -> Tuple[str, str, str, str]:
        one:str = base_principal_parts[0]
        if not one.endswith('o'):
            raise ValueError("-are verbs first person singular must end in an `o`.")
        two:str = one[:-1] + 'are'
        three:str = one[:-1] + 'avi'
        four:str = one[:-1] + 'atum'
        return one, two, three, four
    
    def _validate_all_four_base_principal_parts(self):
        proper_endings:bool = True
        proper_endings = proper_endings and self.one_present_1ps.endswith('o')
        proper_endings = proper_endings and self.two_infinitive.endswith('are')
        proper_endings = proper_endings and self.three_perfect_1ps.endswith('avi')
        proper_endings = proper_endings and self.four_supine.endswith('atum')
        if not proper_endings:
            raise ValueError("Check principal part endings!")
