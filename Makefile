init:
	pip install -r requirements.txt

test:
	pip install -r tests/requirements.txt
	nosetests tests