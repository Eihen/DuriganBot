init:
	pip install -r requirements.txt

init-tests:
	pip install -r tests/requirements.txt

test:
	nosetests tests --with-coverage --cover-package=duriganbot

