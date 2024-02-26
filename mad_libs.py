# The user will be prompted to input an adjective, noun, or verb (or
# other part of a sentence) and the results will output a mad lib for
# the user to read

adj_1 = str.lower(input('Enter an adjective: '))
noun_1 = str.lower(input('Enter a noun: '))
verb_1 = str.lower(input('Enter a verb: '))
noun_2 = str.lower(input('Enter a noun: '))

mad = f'The {adj_1} panda walked to the {noun_1} and then {verb_1}. A nearby {noun_2} was unaffected by these events.'
print(mad)