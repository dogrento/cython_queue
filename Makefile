build:
	python setup.py build_ext --inplace

clean:
	rm -rf __pycache__
	rm -rf src/__pycache__
	rm -rf tests/__pycache__
	rm -f *.so
	rm -f *.c
	rm -rf build
	rm -f *.html
