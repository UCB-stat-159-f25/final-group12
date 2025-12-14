.ONESHELL:
SHELL = /bin/bash

.PHONY : env all clean

env:
	conda env update -n nba -f environment.yml --prune

all: env
	conda run -n nba \
		jupyter nbconvert --to notebook --execute \
		--inplace \
		data_scraping.ipynb \
		feature_engineering.ipynb \
		eda.ipynb \
		modeling.ipynb \
		main.ipynb

.SILENT: clean
clean : 
	rm -f outputs/*
	rm -rf _build/*
