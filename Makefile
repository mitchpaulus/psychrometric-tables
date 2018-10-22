tex/main.pdf : tex/main.tex tex/tdb-twb.tex tex/tdb-tdp.tex tex/tdb-rh.tex
	cd tex && latexmk -lualatex main.tex

tex/tdb-twb.tex : psychrometrics/tdb-twb.py psychrometrics/psychrometrics.py
	cd psychrometrics && python3 tdb-twb.py

tex/tdb-tdp.tex : psychrometrics/tdb-tdp.py psychrometrics/psychrometrics.py
	cd psychrometrics && python3 tdb-tdp.py

tex/tdb-rh.tex : psychrometrics/tdb-rh.py psychrometrics/psychrometrics.py
	cd psychrometrics && python3 tdb-rh.py

clean :
	rm -f tex/tdb-twb.tex
	rm -f tex/tdb-tdp.tex
	rm -f tex/tdb-rh.tex
	rm -f tex/main.pdf
	rm -f tex/main.fls
	rm -f tex/main.aux
	rm -f tex/main.out
	rm -f tex/main.fdb_latexmk
	rm -f tex/main.log
	rm -f tex/main.toc
