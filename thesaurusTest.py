from py_thesaurus import Thesaurus

tWord = "attack"

new_instance = Thesaurus(tWord)

# Get the synonyms according to part of speech
# Default part of speech is noun

print(new_instance.get_synonym())
print(new_instance.get_synonym(pos='verb'))
print(new_instance.get_synonym(pos='adj'))

print(new_instance.get_definition())