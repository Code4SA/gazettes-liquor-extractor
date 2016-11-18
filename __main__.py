import os

import config
from utils import scrub_content, print_licensee
from liquor_regex import simple_match_regex, doubles_regex

licensees = []

for file_name in config.files:
    file_path = os.path.join(config.path_for_gazettes, file_name)

    with open(file_path, 'rt') as f:
        content = f.read()

    scrubbed_content = scrub_content(content)

    simple_matches = simple_match_regex.finditer(scrubbed_content)

    for match in simple_matches:

        licensee = dict()
        for i, title in enumerate(config.section_titles, start=2):
            licensee[title] = match.group(i).strip()
        licensees.append(licensee)

    unpicked = simple_match_regex.sub('', scrubbed_content)
    doubles = doubles_regex.finditer(unpicked)
    for double in doubles:
        # Each double contains two licensees. Add them both.
        licensee = dict()
        for i, title in zip(list(range(2, 13, 2)), config.section_titles):
            licensee[title] = double.group(i).strip()
        licensees.append(licensee)

        licensee = dict()
        for i, title in zip(list(range(3, 14, 2)), config.section_titles):
            licensee[title] = double.group(i).strip()
        licensees.append(licensee)

    for licensee in licensees:
        print_licensee(licensee)

    unpicked = doubles_regex.sub('', unpicked)

    # TODO: do something with unpicked
