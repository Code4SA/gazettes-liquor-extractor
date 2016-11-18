import config
from utils import scrub_content, print_licensee
from liquor_regex import low_hanging_regex, doubles_regex

licensees = []

for file_path in config.files:

    with open(file_path, 'rt') as f:
        content = f.read()

    clean_content = scrub_content(content)
    low_hanging_fruit = low_hanging_regex.finditer(clean_content)

    for fruit in low_hanging_fruit:
        licensee = {
            'Title': fruit.group(1).strip(),
            'Licensee Details': fruit.group(2).strip(),
            'License Type': fruit.group(3).strip(),
            'Liquor Type': fruit.group(4).strip(),
            'Full Address': fruit.group(5).strip(),
            'Business Name': fruit.group(6).strip(),
        }
        licensees.append(licensee)

    unpicked = low_hanging_regex.sub('', clean_content)
    doubles = doubles_regex.finditer(unpicked)
    for fruit in doubles:
        licensee_one = {
            'Title': fruit.group(1).strip(),
            'Licensee Details': fruit.group(3).strip(),
            'License Type': fruit.group(5).strip(),
            'Liquor Type': fruit.group(7).strip(),
            'Full Address': fruit.group(9).strip(),
            'Business Name': fruit.group(11).strip(),
        }
        licensee_two = {
            'Title': fruit.group(2).strip(),
            'Licensee Details': fruit.group(4).strip(),
            'License Type': fruit.group(6).strip(),
            'Liquor Type': fruit.group(8).strip(),
            'Full Address': fruit.group(10).strip(),
            'Business Name': fruit.group(12).strip(),
        }

        licensees.append(licensee_one)
        licensees.append(licensee_two)

    for licensee in licensees:
        print_licensee(licensee)

    yet_unpicked = doubles_regex.sub('', unpicked)
