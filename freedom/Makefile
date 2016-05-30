all: freedom.pdf

freedom.pdf: freedom.md pictures
	pandoc --latex-engine=xelatex -F pandoc-crossref -F pandoc-citeproc --biblatex -t beamer -V mainfont='CMU Serif' -V geometry:margin=2cm -S freedom.md -o freedom.pdf

pictures: graphs

graphs: pic/star.c.png pic/star.d.png

pic/star.%.png: pic/star.%.dot
	dot -Tpng -o pic/star.$*.png pic/star.$*.dot
