import os

import config
from utils import scrub_content, print_licensee
from liquor_regex import low_hanging_regex, doubles_regex

licensees = []

for file_name in config.files:
    file_path = os.path.join(config.path_for_gazettes, file_name)

    with open(file_path, 'rt') as f:
        content = f.read()

    clean_content = scrub_content(content)
    low_hanging_fruit = low_hanging_regex.finditer(clean_content)

    for fruit in low_hanging_fruit:
        licensee = dict()
        for i, title in enumerate(config.section_titles, start=1):
            licensee[title] = fruit.group(i).strip()
        licensees.append(licensee)

    unpicked = low_hanging_regex.sub('', clean_content)
    doubles = doubles_regex.finditer(unpicked)
    for fruit in doubles:
        # Each fruit contains two licensees. Add them both.
        licensee = dict()
        for i, title in zip(list(range(1, 14, 2)), config.section_titles):
            licensee[title] = fruit.group(i).strip()
        licensees.append(licensee)

        # Each fruit contains two licensees. Add them both.
        licensee = dict()
        for i, title in zip(list(range(2, 15, 2)), config.section_titles):
            licensee[title] = fruit.group(i).strip()
        licensees.append(licensee)

    for licensee in licensees:
        print_licensee(licensee)

    unpicked = doubles_regex.sub('', unpicked)

    # TODO: do something with unpicked
