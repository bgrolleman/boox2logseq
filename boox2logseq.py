#!/usr/bin/python
#
# Usage: cat <exported notes file> | python boox2logseq.py > logseqmarkdown.md
#
# This will take annotated notes and convert them to the following format for pasting into Logseq
#
# - <Annotation>
#   Page:: <Page nr>
#   Created:: <Create Date>
#   - #+BEGIN_QUOTE
#     <Quote>
#     #+END_QUOTE
import re
import sys

# Read input from STDIN
text = sys.stdin.read()

#pattern = r"^([0-9\- :]{16}).*: ([0-9]+)\n((?:[^\n-].*(?=\n|$))*)-{19}$"
pattern = r"^([0-9\- :]{16}).*: ([0-9]+)\n((?:[^-].*\n)*)-{19}$"
matches = re.finditer(pattern, text, re.MULTILINE)

# Process each match
for match_num, match in enumerate(matches, start=1):
    group3_content = match.group(3)

    if "【Annotation】" in group3_content:
        quote, annotation = group3_content.split("【Annotation】", 1)
        quote = re.sub(r"\n$","",quote)
        annotation = re.sub(r"\n$","",annotation)
        group3_without_newlines = match.group(3).replace("\n", " ")
        print("-", annotation)
        print("  Page:: ", match.group(2))
        print("  Created:: ", match.group(1))
        print("  - #+BEGIN_QUOTE")
        print("   ", quote)
        print("    #+END_QUOTE")

