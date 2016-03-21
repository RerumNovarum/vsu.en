CC=pandoc
CFLAGS=--latex-engine=xelatex -V mainfont='CMU Serif' -V geometry:margin=2cm -S

bst_aug.pdf: slides_order/*.markdown
	$(CC) $(CFLAGS) -t beamer -V theme:CambridgeUS -so bst_aug.pdf slides_order/*.markdown
