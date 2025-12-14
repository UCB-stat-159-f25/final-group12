.ONESHELL:
SHELL = /bin/bash

.PHONY : env html clean

env:
	conda env update -n nba -f environment.yml --prune

html :
	myst build --html

.SILENT: clean
clean : 
	rm -f outputs/*
	rm -rf _build/*
