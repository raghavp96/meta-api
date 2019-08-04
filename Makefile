run:
	gunicorn  wsgi

clean:
	find . -name '__pycache__' -type d -exec rm -rf {} +