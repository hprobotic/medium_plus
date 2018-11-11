start:
	uwsgi --http 127.0.0.1:5000 --module medium_plus.wsgi:app