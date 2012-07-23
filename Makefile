all: demo1.png demo2.png
%.png: %.py
	python $*.py > $*.dot
	neato -T png -o $*.png $*.dot
clean:
	rm *.dot *.png
