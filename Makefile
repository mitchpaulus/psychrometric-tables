TEX_FOLDER = tex/
PSY_FOLDER = psychrometrics/

$(TEX_FOLDER)main.pdf: $(TEX_FOLDER)main.tex $(TEX_FOLDER)tdb-rh.tex $(TEX_FOLDER)tdb-tdp.tex $(TEX_FOLDER)tdb-twb.tex
	cd $(TEX_FOLDER) && latexmk -lualatex main.tex

$(TEX_FOLDER)tdb-twb.tex :
	python3 $(PSY_FOLDER)tdb-twb.py $(TEX_FOLDER)tdb-twb.tex

$(TEX_FOLDER)tdb-rh.tex :
	python3 $(PSY_FOLDER)tdb-rh.py $(TEX_FOLDER)tdb-rh.tex

$(TEX_FOLDER)tdb-tdp.tex :
	python3 $(PSY_FOLDER)tdb-tdp.py $(TEX_FOLDER)tdb-tdp.tex

clean : 
	rm -f $(TEX_FOLDER)/main.aux
	rm -f $(TEX_FOLDER)/main.log
	rm -f $(TEX_FOLDER)/main.out
	rm -f $(TEX_FOLDER)/main.toc
	rm -f $(TEX_FOLDER)/main.pdf
	rm -f $(TEX_FOLDER)/main.fdb_latexmk
	rm -f $(TEX_FOLDER)/main.fls
	rm -f $(TEX_FOLDER)/tdb-rh.tex
	rm -f $(TEX_FOLDER)/tdb-twb.tex
	rm -f $(TEX_FOLDER)/tdb-tdp.tex
