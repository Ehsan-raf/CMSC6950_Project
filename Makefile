Report.pdf: Report.tex Task1.png Task2.png
	latexmk -pdf

Task1.png:	Task1.py
	python3 Task1.py

Task2.png: Task2.py
	python3 Task2.py


clean:
	rm *.csv
	rm *.png

.PHONY : clean

deepclean:
	rm *.png
	latexmk -c
	rm *.pdf
	rm *.csv
	rm Report.log
	rm Report.out
	rm Report.bbl

.PHONY : deepclean
