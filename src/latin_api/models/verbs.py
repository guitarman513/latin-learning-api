from typing import Tuple, List, Dict, Optional, Union
from enum import Enum

from latin_api.models.grammar import Plurality, Person

DELETE_CHAR:str = '*'  # if a conjugation includes this, it means delete one character off of the stem before adding the next non-`DELETE_CHAR` character

class VerbTense(str, Enum):
    present = 'present'
    imperfect = 'imperfect'



class PrincipalParts:
    def __init__(self, one_present_fps:str, two_infinitive:Optional[str]=None, three_perfect_fps:Optional[str]=None, four_supine:Optional[str]=None, regular=True) -> None:
        if regular:
            self.one_present_1ps, self.two_infinitive, self.three_perfect_1ps, self.four_supine = self._get_principle_parts_from_1ps(one_present_fps)
        elif two_infinitive and three_perfect_fps and four_supine:
            self.one_present_1ps, self.two_infinitive, self.three_perfect_1ps, self.four_supine = (one_present_fps, two_infinitive, three_perfect_fps, four_supine)
        else:
            raise ValueError("must pass either a regular first person singular or all four principal parts.")
        self._validate_all_four_base_principal_parts()

    def _get_principle_parts_from_1ps(self, one_present_fps:str) -> Tuple[str, str, str, str]:
        #TODO: this will change once I learn more verbs I imagine...
        if not one_present_fps.endswith('o'):
            raise ValueError("-are verbs first person singular must end in an `o`.")
        two:str = one_present_fps[:-1] + 'are'
        three:str = one_present_fps[:-1] + 'avi'
        four:str = one_present_fps[:-1] + 'atum'
        return one_present_fps, two, three, four
    
    def _validate_all_four_base_principal_parts(self):
        proper_endings:bool = True
        proper_endings = proper_endings and self.one_present_1ps.endswith('o')
        proper_endings = proper_endings and self.two_infinitive.endswith('are')
        proper_endings = proper_endings and self.three_perfect_1ps.endswith('avi')
        proper_endings = proper_endings and self.four_supine.endswith('atum')
        if not proper_endings:
            raise ValueError("Check principal part endings!")


class ConjugationTable:
    def __init__(self, fs:str, fp:str, ss:str, sp:str, ts:str, tp:str, stem:str) -> None:
        def adjust_conj(suffix:str) -> str:
            delete_char_count = 0
            for char in suffix:
                if char == DELETE_CHAR:
                    delete_char_count += 1
            if delete_char_count:
                suffix = ''.join(suffix.split(DELETE_CHAR))
                new_stem = stem[:-delete_char_count]
            else:
                new_stem = stem
            return new_stem + suffix
        
        self.table = {
            Person.first:  {Plurality.singular: adjust_conj(fs), Plurality.plural: adjust_conj(fp)},
            Person.second: {Plurality.singular: adjust_conj(ss), Plurality.plural: adjust_conj(sp)},
            Person.third:  {Plurality.singular: adjust_conj(ts), Plurality.plural: adjust_conj(tp)},
        }


class Verb:
    def __init__(
        self,
        principal_parts:PrincipalParts, 
        english_root:str, 
        verb_tables:Dict[VerbTense,ConjugationTable]
    ) -> None:
        if type(self) == Verb: raise ValueError("Need to subclass with the appropriate verb type.")
        self.principal_parts:PrincipalParts = principal_parts
        self.english_root:str = english_root
        self.verb_tables:Dict[VerbTense,ConjugationTable] = verb_tables
        self._check_verb_tables()
        
    def conjugate(self, tense:VerbTense, person:Person, plurality:Plurality) -> str:
        return self.verb_tables[tense].table[person][plurality]

    def _check_verb_tables(self):
        all_implemented_tenses = self.verb_tables.keys()
        for tense in VerbTense:
            if tense not in all_implemented_tenses:
                raise AttributeError(f"Expected tense not found in verb tables: {tense}")
        


class RegularVerb(Verb):
    def __init__(
            self, 
            principal_parts_text:Union[Tuple[str],Tuple[str,str,str,str]], 
            english_root:str, 
            verb_table_endings:Dict[VerbTense,Tuple[str,str,str,str,str,str]]
        ) -> None:
        
        if type(self) == RegularVerb: raise ValueError("Need to subclass with the appropriate verb type.")

        if len(principal_parts_text) != 1 and len(principal_parts_text) != 4:
            raise ValueError("base_principal_parts must either be first person singular or all four principal parts.")
        if len(principal_parts_text) == 1:
            principal_parts:PrincipalParts = PrincipalParts(principal_parts_text[0])
        else:
            principal_parts:PrincipalParts = PrincipalParts(principal_parts_text[0], principal_parts_text[1], principal_parts_text[2], principal_parts_text[3], regular=True)

        stem = principal_parts.two_infinitive[:-2]  # amare -> ama
        verb_tables = {verb_tense:ConjugationTable(*table_endings, stem) for verb_tense,table_endings in verb_table_endings.items()}

        super().__init__(principal_parts, english_root, verb_tables)


    
    

class VerbFirstConjugationRegular(RegularVerb):  # -are verbs like amare, navigare, etc.
    def __init__(self, principal_parts_text:Union[Tuple[str],Tuple[str,str,str,str]], english_root: str) -> None:
        
        verb_table_endings:Dict[VerbTense,Tuple[str,str,str,str,str,str]] = dict()
        verb_table_endings[VerbTense.present] = (f'{DELETE_CHAR}o','mus','s','tis','t','nt')
        verb_table_endings[VerbTense.imperfect] = ('bam','bamus','bas','batis','bat','bant')
        
        super().__init__(principal_parts_text, english_root, verb_table_endings)
        

