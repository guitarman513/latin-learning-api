from typing import Tuple
from enum import Enum

from latin_api.models.grammar import Plurality, Case

DELETE_CHAR:str = '*'  # if a conjugation includes this, it means delete one character off of the stem before adding the next non-`DELETE_CHAR` character




class CaseTable:
    def __init__(self, nom_s:str, nom_p:str, voc_s:str, voc_p:str, acc_s:str, acc_p:str, gen_s:str, gen_p:str, dat_s:str, dat_p:str, abl_s:str, abl_p:str, stem:str) -> None:
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
            Case.nominative:  {Plurality.singular: adjust_conj(nom_s), Plurality.plural: adjust_conj(nom_p)},
            Case.vocative:    {Plurality.singular: adjust_conj(voc_s), Plurality.plural: adjust_conj(voc_p)},
            Case.accusative:  {Plurality.singular: adjust_conj(acc_s), Plurality.plural: adjust_conj(acc_p)},
            Case.genitive:    {Plurality.singular: adjust_conj(gen_s), Plurality.plural: adjust_conj(gen_p)},
            Case.dative:      {Plurality.singular: adjust_conj(dat_s), Plurality.plural: adjust_conj(dat_p)},
            Case.ablative:    {Plurality.singular: adjust_conj(abl_s), Plurality.plural: adjust_conj(abl_p)},
        }


class Noun:
    def __init__(
        self,
        english_root:str, 
        case_table:CaseTable
    ) -> None:
        if type(self) == Noun: raise ValueError("Need to subclass with the appropriate noun type.")
        self.english_root:str = english_root
        self.case_table:CaseTable = case_table
        self._check_case_table()
        
    def decline(self, case:Case, plurality:Plurality) -> str:
        return self.case_table.table[case][plurality]

    def _check_case_table(self):
        all_implemented_cases = self.case_table.table.keys()
        for case in Case:
            if case not in all_implemented_cases:
                raise AttributeError(f"Expected case not found in noun tables: {case}")
        


class RegularNoun(Noun):
    def __init__(
            self, 
            english_root:str, 
            latin_genitive_singular:str, # regular nouns can be declined if you know the genitive singular
            noun_declension_endings:Tuple[str,str, str,str, str,str, str,str, str,str, str,str, ] # 6 cases sing/plural
        ) -> None:
        
        if type(self) == RegularNoun: raise ValueError("Need to subclass with the appropriate noun type.")

        stem = latin_genitive_singular[:-2]  # puellae -> puell
        noun_table = CaseTable(*noun_declension_endings, stem)

        super().__init__(english_root, noun_table)


    
    

class NounFirstDeclensionRegular(RegularNoun):  # mensa, puella, agricola
    def __init__(self, english_root:str, latin_genitive_singular:str) -> None:
        if not latin_genitive_singular.endswith('ae'):
            raise ValueError("Genitive singular needs to end in -ae")
        noun_declension_endings = ( # sing, plural
            'a', 'ae',              # nom
            'a', 'ae',              # voc
            'am', 'as',             # acc
            'ae', 'arum',           # gen
            'ae', 'is',             # dat
            'a', 'is'               # abl
        )
        super().__init__(english_root, latin_genitive_singular, noun_declension_endings)
        

