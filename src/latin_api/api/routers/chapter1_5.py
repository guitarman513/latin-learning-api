from fastapi import APIRouter
from latin_api.models.combiner import pronoun_verb_only, noun_verb_object, Phrase

router = APIRouter(prefix="/1")

@router.post("/pronoun")
async def one():
    r:Phrase = pronoun_verb_only()
    return {'english':r.english, 'latin':r.latin}


@router.post("/noun_verb_obj")
async def two():
    r:Phrase = noun_verb_object()
    return {'english':r.english, 'latin':r.latin}
