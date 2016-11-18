import regex as mrab


def scrub_content(content):
    """Removing intro of file"""

    remove_intro = mrab.sub(r'(?is)\A.*?limpopo\s*(?=praktiseer)', '', content)
    return remove_intro


def print_licensee(licensee):
    print('Title:', licensee['Title'])
    print('Licensee Details:',licensee['Licensee Details'])
    print('License Type', licensee['License Type'])
    print('Liquor Type', licensee['Liquor Type'])
    print('Full Address', licensee['Full Address'])
    print('Business Name', licensee['Business Name'])
    print('\n')


