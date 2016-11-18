import regex as mrab
import config


def scrub_content(content):
    """Removing unwanted sections of file

    This version only addresses the intro up to a hard-coded point.
    Future versions should:
     * look for a more generic delimiter
     * add "scrub" operations before returning.
    """

    scrubbed = mrab.sub(r'(?is)\A.*?limpopo\s*(?=praktiseer)', '', content)
    # TODO
    # scrubbed = some_other_operation(scrubbed)
    # scrubbed = some_other_operation(scrubbed)
    return scrubbed


def print_licensee(licensee):
    titles = config.section_titles
    for title in titles:
        print(title + ':', licensee[title])
    print('\n')
