import itertools

phrase = "Глокая куздра штеко будланула бокра и курдячит бокрёнка".split()

results = []

for oder in itertools.permutations(phrase):
    variants_brakets = []

    for length_group in range(1, min(len(oder), 4) + 1):
        for group in itertools.combinations(oder, length_group):
            last_words = [word for word in oder if word not in group]
            variants_brakets.append("{" + " ".join(group) + " " + " ".join(last_words) + "}")

    results.extend(variants_brakets)

# Выводим уникальные результаты
print(set(results))
