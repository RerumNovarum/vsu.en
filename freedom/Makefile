freedom.pdf: freedom.md pictures
	pandoc --latex-engine=xelatex -F pandoc-crossref -F pandoc-citeproc --biblatex -t beamer -V mainfont='CMU Serif' -V geometry:margin=2cm -S freedom.md -o freedom.pdf

pictures: graphs

graphs: gr-star.c gr-star.d

gr-%: pic/%.dot
	dot -Tpng -o pic/$*.png pic/$*.dot
