import config
import liquor_regex


def scrub_content(content):
    """Removing unwanted sections of file

    This version only addresses the intro up to a hard-coded point.
    Future versions should:
     * look for a more generic delimiter
     * add "scrub" operations before returning.
    """

    scrubbed = liquor_regex.intro_regex.sub('', content)
    # print(scrubbed[:200]) # check that intro was removed

    # TODO
    # scrubbed = some_other_operation(scrubbed)
    # scrubbed = some_other_operation(scrubbed)
    return scrubbed


def print_licensee(licensee):
    titles = config.section_titles
    for title in titles:
        print(title + ':', licensee[title])
    print('\n')
