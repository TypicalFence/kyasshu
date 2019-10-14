.PHONY: test coverage lint clean

test:
	pipenv run test

coverage:
	pipenv run coverage

lint:
	pipenv run lint

clean:
	-pipenv --rm
	rm -f Pipfile.lock
