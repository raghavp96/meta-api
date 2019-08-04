run:
	gunicorn  wsgi

clean:
	rm -r $(find . -name '__pycache__')