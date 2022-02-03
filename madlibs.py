import random

adj = input("Adjective: ")
plural_noun = input("Plural noun: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")

madlib1 = f'Computer programming is so {adj}! It makes me feel like a million {plural_noun}!\
    I love to {verb1} everyday and staying hydrated is so important. So {verb2} like there is no tomorrow!'

madlib2 = f"Today I went to the beach and it was sooo {adj}! You wouldn't believe what I saw. I saw a hundred {plural_noun} flying overhead!\
    When I saw them I decided to {verb1}. Best decision I ever made because all of a sudden they began to {verb2}! What a day!"

madlib3 = f"When I think of {plural_noun}, I just want to {verb1}! They are truly {adj}. "

#madlib = [madlib1, madlib2, madlib3]

m = random.choice([madlib1, madlib2, madlib3])

print(m)