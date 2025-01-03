all:
	pdflatex slides.tex && evince slides.pdf

clean:
	rm -f *.aux *.toc *.log *.nav *.out *.snm *~ renum.tex

renum:
	cp slides.tex slides.tex.sov
	python3 renumber-slides.py && mv renum.tex slides.tex
