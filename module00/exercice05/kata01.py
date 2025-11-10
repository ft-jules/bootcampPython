#!/usr/bin/env python3

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for language, createur in kata.items():
    print(f"{language} was created by {createur}")