languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

if isinstance(languages, dict):
    for key, val in languages.items():
        print(key + " was created by " + val)
else:
    print("Dictonnary only")
