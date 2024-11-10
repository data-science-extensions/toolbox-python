#* Variables
PYTHON := python3
PACKAGE_NAME := toolbox_python
PYTHONPATH := `pwd`
VERSION ?= v0.0.0
VERSION_CLEAN := $(shell echo $(VERSION) | awk '{gsub(/v/,"")}1')
VERSION_NO_PATCH := "$(shell echo $(VERSION) | cut --delimiter '.' --fields 1-2).*"


#* Environment
.PHONY: check-environment
update-build-essentials:
	sudo apt-get install build-essential
update-environment:
	sudo apt-get update --yes
	sudo apt-get upgrade --yes
install-git:
	sudo apt-get install git --yes


#* Python
.PHONY: prepare-python
install-python:
	sudo apt-get install python3-venv --yes
install-pip:
	sudo apt-get install python3-pip --yes
upgrade-pip:
	$(PYTHON) -m pip install --upgrade pip
install-python-and-pip: install-python install-pip upgrade-pip


#* Poetry
.PHONY: poetry-installs
install-poetry:
	$(PYTHON) -m pip install poetry
	poetry --version
install:
	poetry install --no-interaction --only main
install-dev:
	poetry install --no-interaction --with dev
install-docs:
	poetry install --no-interaction --with docs
install-test:
	poetry install --no-interaction --with test
install-dev-test:
	poetry install --no-interaction --with dev,test
install-all:
	poetry install --no-interaction --with dev,docs,test


#* Linting
.PHONY: linting
run-black:
	poetry run black --config pyproject.toml ./
run-isort:
	poetry run isort --settings-file pyproject.toml ./
run-safety:
	poetry check
lint: run-black run-isort run-safety


#* Checking
.PHONY: checking
check-black:
	poetry run black --diff --check --config pyproject.toml ./
check-mypy:
	poetry run mypy --install-types --config-file pyproject.toml src/$(PACKAGE_NAME)
check-isort:
	poetry run isort --settings-file pyproject.toml ./
check-codespell:
	poetry run codespell --toml pyproject.toml src/ *.py
check-safety:
	poetry check
check-pylint:
	poetry run pylint --rcfile=pyproject.toml src/$(PACKAGE_NAME)
check-pytest:
	poetry run pytest --config-file pyproject.toml
check-pycln:
	poetry run pycln --config="pyproject.toml" src/$(PACKAGE_NAME)
check-mkdocs:
	poetry run mkdocs build --site-dir="temp"
	if [ -d "temp" ]; then rm --recursive temp; fi
check: check-black check-mypy check-pycln check-isort check-codespell check-pylint check-mkdocs check-pytest


#* Testing

.PHONY: pytest
pytest:
	poetry run pytest --config-file pyproject.toml


#* Git
.PHONY: git-processes
git-add-credentials:
	git config --global user.name ${GITHUB_ACTOR}
	git config --global user.email "${GITHUB_ACTOR}@users.noreply.github.com"
	git config --global --list
	git config --local --list
	git remote -v
configure-git: git-add-credentials
git-refresh-current-branch:
	git remote update
	git fetch --verbose
	git fetch --verbose --tags
	git pull  --verbose
	git status --verbose
	git branch --list --verbose
	git tag --list --sort=-creatordate
git-switch-to-main-branch:
	git checkout -B main --track origin/main
git-switch-to-docs-branch:
	git checkout -B docs-site --track origin/docs-site
git-check-add-docs-remote:
	@if git remote -v | grep -q '^docs'; then \
		git remote remove docs; \
	fi
	echo ${DSE_ACCESS_TOKEN}
	git remote add docs https://${DSE_ACCESS_TOKEN}@github.com/data-science-extensions/website.git
git-test:
	echo ${DSE_ACCESS_TOKEN}
	echo $(DSE_ACCESS_TOKEN)
	git remote -v
	git remote add docs https://x-acccess-token:${DSE_ACCESS_TOKEN}@github.com/data-science-extensions/website.git
	git remote -v



#* Deploy Package
# See: https://github.com/monim67/poetry-bumpversion

.PHONY: bump-version
bump-version:
	poetry self add poetry-bumpversion
	poetry version $(VERSION_CLEAN)
	poetry version --short

.PHONY: update-git
update-git:
	git add .
	git commit --message="Bump to version \`$(VERSION)\` [skip ci]" --allow-empty
	git push --force --no-verify
	git status

.PHONY: poetry-build
poetry-build:
	poetry build

.PHONY: poetry-configure-credentials
poetry-configure:
	poetry config pypi-token.pypi ${PYPI_TOKEN}

.PHONY: poetry-publish
poetry-publish:
	poetry publish

.PHONY: build-package
build-package: poetry-build

.PHONY: deploy-package
deploy-package: poetry-configure poetry-publish



#* Docs
.PHONY: docs
docs-serve-static:
	poetry run mkdocs serve
docs-serve-versioned:
	poetry run mike serve --remote=docs --branch=docs-site
docs-build-static:
	poetry run mkdocs build --clean
docs-build-versioned:
	git config --global --list
	git config --local --list
	git remote -v
	echo ${DSE_ACCESS_TOKEN}
	poetry run mike --debug deploy --update-aliases --remote=docs --branch=docs-site --push $(VERSION) latest
update-git-docs:
	git add .
	git commit -m "Build docs [skip ci]"
	git push --force --no-verify --push-option ci.skip
docs-check-versions:
	poetry run mike --debug list --remote=docs --branch=docs-site
docs-delete-version:
	poetry run mike --debug delete --remote=docs --branch=docs-site $(VERSION)
docs-set-default:
	poetry run mike --debug set-default --remote=docs --branch=docs-site --push latest
build-static-docs: docs-build-static update-git-docs
build-versioned-docs: git-check-add-docs-remote docs-build-versioned docs-set-default
