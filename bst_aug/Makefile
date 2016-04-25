CC=pandoc
SLIDES=\
slides/title.markdown \
slides/contact.markdown \
slides/github.markdown \
slides/foreword.markdown \
slides/motivation.markdown \
slides/cumulative.markdown \
slides/rsq.markdown \
slides/rmq.markdown \
slides/rmq_solution.markdown \
slides/lazy_propagation.markdown \
slides/online_problem.markdown \
slides/arbitrary_key.markdown \
slides/monoid.markdown \
slides/augmentation.markdown \
slides/aug-implementation.markdown \
slides/examples.markdown \
slides/references.markdown \
slides/contact.markdown

CFLAGS=--latex-engine=xelatex -V mainfont='CMU Serif' -V fontsize:10pt -V geometry:margin=2cm -S

bst_aug.pdf: $(SLIDES)
	$(CC) $(CFLAGS) -t beamer -V theme:CambridgeUS -so bst_aug.pdf $(SLIDES)
