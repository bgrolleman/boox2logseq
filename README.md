This is a very simple script, it allows me to export all my annotations from NeoReader and then quickly convert it to a reference page in Logseq that I can then link to in my notes.

1. This will only convert notes with annotations, since it will use the annotation as the title. This is personal preference because I only want to export notes where I had a thought.
2. I'm still testing this, but bug fixes will happen as I go through books making notes


Usage:
You will need to have python installed for this to work, I'm using STDIN and STDOUT 

cat <exported notes file> | python boox2logseq.py > <resulting file for logseq>
cat asystemforwriting.txt | python boox2logseq.py > asystemforwriting.md
