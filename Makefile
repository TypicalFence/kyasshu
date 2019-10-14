.PHONY: help init lint test coverage
locks = core/Pipfile.lock redis/Pipfile.lock

help: ## Display this help text
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

%/Pipfile.lock: %/Pipfile
	cd $* && pipenv install -d

init: $(locks) ## Initialize all projects with pipenv

lint: $(locks) ## Lint all packages
	-$(MAKE) -C core lint
	$(MAKE) -C redis lint

test: $(locks) ## Test all packages
	-$(MAKE) -C core test
	$(MAKE) -C redis test

coverage: $(locks) ## Print the test coverage of all packages
	-$(MAKE) -C core coverage
	$(MAKE) -C redis coverage

clean:
	-$(MAKE) -C core clean
	$(MAKE) -C redis clean 
