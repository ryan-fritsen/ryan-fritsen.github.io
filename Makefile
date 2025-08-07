# Makefile for static blog site

.PHONY: all render serve clean

all: render serve

# Run render.py to generate static HTML files
render:
	python render.py

# Start the Flask server to serve files from output/
serve:
	python serve.py

# Optional: remove output directory
clean:
	rm -rf output
