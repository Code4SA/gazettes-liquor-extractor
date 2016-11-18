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

doubles_regex = mrab.compile(r'''(?mx)
(?(DEFINE)(?<bracketed_digit>\([1-5]\)))

# Name: Groups 2 & 3
(?>
  ^(\w+)[ ]+(.*?)(?=\s*[\r\n])
  \s*
)

# Applicant: Groups 4 & 5
(?>(?>(?>(?>(?>(?>(?>(?>(?>
\(1\)\s*
((?>(?!(?&bracketed_digit))[\d\D])*?)
\s*\(1\))\s*
((?>(?!(?&bracketed_digit))[\d\D])*?)

# License Category: Groups 6 & 7
\s*\(2\))\s*

((?>(?!(?&bracketed_digit))[\d\D])*?)
\s*\(2\))\s*
((?>(?!(?&bracketed_digit))[\d\D])*?)

# Liquor Type: Groups 8 & 9
\s*\(3\))\s*
((?>(?!(?&bracketed_digit))[\d\D])*?)
\s*\(3\))\s*
((?>(?!(?&bracketed_digit))[\d\D])*?)

# Business Details: Groups 8 & 9
\s*\(4\))\s*
((?>(?!(?&bracketed_digit))[\d\D])*?)
\s*\(4\))\s*
((?>(?!(?&bracketed_digit))[\d\D])*?)

# Authority: Groups 10 & 11
\s*\(5\))\s*
.*?
([\r\n]*?)
\s*\(5\))\s*
(.*?\s*$)''')
