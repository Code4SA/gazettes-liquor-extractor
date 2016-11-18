import regex as mrab


intro_regex = mrab.compile(r'''(?xsm)
(?(DEFINE)(?<bracketed_digit>\([1-5]\)))
(?>\A.*?BYLAE)
(?>(?!(?&bracketed_digit)).)*\(1\)
(?>(?!(?&bracketed_digit)).)*\(2\)
(?>(?!(?&bracketed_digit)).)*\(3\)
(?>(?!(?&bracketed_digit)).)*\(4\)
(?>(?!(?&bracketed_digit)).)*\(5\)
.*?
^$\s*
''')


simple_match_regex = mrab.compile(r"""(?xm)
(?(DEFINE)(?<bracketed_digit>\([1-5]\)))

# Name Line (sometimes empty)
(?>(?P<Name>.*)\n)

# (1) Applicant
\(1\)\s*
(?P<Applicant>(?>(?!(?&bracketed_digit))[\d\D])*)(?=\(2\))

# (2) License Category
\(2\)\s*
(?P<LicenseCat>(?>(?!(?&bracketed_digit))[\d\D])*)(?=\(3\))

# (3) Liquor Type
\(3\)\s*
(?P<LiquorType>(?>(?!(?&bracketed_digit))[\d\D])*)(?=\(4\))

# (4) Business Details
\(4\)\s*
(?P<Business>(?>(?!(?&bracketed_digit))[\d\D])*)(?=\(5\))

# (5) Authority: just grab the first line
\(5\)\s*(?P<Authority>.*)

""")

doubles_regex = mrab.compile(r'''(?smx)
^(\w+)[ ]+(.*?)(?=\s*[\r\n])
\s*
(\(1\)(?:(?!\(2).)*?(?=\s*\(1))
\s*
(\(1\)(?:(?!\(3).)*?(?=\s*\(2))
\s*
(\(2\)(?:(?!\(3).)*?(?=\s*\(2))
\s*
(\(2\)(?:(?!\(4).)*?(?=\s*\(3))
\s*
(\(3\)(?:(?!\(4).)*?(?=\s*\(3))
\s*
(\(3\)(?:(?!\(5).)*?(?=\s*\(4))
\s*
(\(4\)(?:(?!\(5).)*?(?=\s*\(4))
\s*
(\(4\)(?:(?!\(4).)*?(?=\s*\(5))
\s*
(\(5\)(?:(?!\(4).)*?(?=\s*\(5))
\s*
(\(5\)(?:(?!\(4).)*?(?=\s*[\r\n]+^$))''')
