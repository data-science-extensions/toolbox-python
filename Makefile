#* Variables
PYTHON := python3
PACKAGE_NAME := toolbox_python
PYTHONPATH := `pwd`
VERSION ?= v0.0.0
VERSION_CLEAN := $(shell echo $(VERSION) | awk '{gsub(/v/,"")}1')
VERSION_NO_PATCH := "$(shell echo $(VERSION) | cut --delimiter '.' --fields 1-2).*"


#* Environment

.PHONY: install-build-essentials
update-build-essentials:
	sudo apt-get install build-essential

.PHONY: update-environment
update-environment:
	sudo apt-get update --yes
	sudo apt-get upgrade --yes

.PHONY: install-git
install-git:
	sudo apt-get install git --yes


#* Python

.PHONY: install-python
install-python:
	sudo apt-get install python3-venv --yes

.PHONY: install-pip
install-pip:
	sudo apt-get install python3-pip --yes

.PHONY: upgrade-pip
upgrade-pip:
	$(PYTHON) -m pip install --upgrade pip

.PHONY: install-python-and-pip
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
check: check-black check-mypy check-pycln check-isort check-codespell check-pylint check-pytest


#* Testing

.PHONY: pytest
pytest:
	poetry run pytest --config-file pyproject.toml


#* Git

.PHONY: configure-git
configure-git: git-add-credentials

.PHONY: git-add-credentials
git-add-credentials:
	git config --global user.name ${GITHUB_ACTOR}
	git config --global user.email "${GITHUB_ACTOR}@users.noreply.github.com"

.PHONY: git-refresh-current-branch
git-refresh-current-branch:
	git remote update
	git fetch --verbose
	git fetch --verbose --tags
	git pull  --verbose
	git status --verbose
	git branch --list --verbose
	git tag --list --sort=-creatordate

.PHONY: git-switch-to-main-branch
git-switch-to-main-branch:
	git checkout -B main --track origin/main

.PHONY: git-switch-to-docs-branch
git-switch-to-docs-branch:
	git checkout -B docs-site --track origin/docs-site


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
serve-docs-static:
	poetry run mkdocs serve
build-docs-static:
	poetry run mkdocs build
build-docs-mike:
	poetry run mike --debug deploy --alias-type=copy --update-aliases --push --branch=docs-site --deploy-prefix=web $(VERSION) latest
update-git-docs:
	git add .
	git commit -m "Build docs [skip ci]"
	git push --force --no-verify --push-option ci.skip
docs-check-versions:
	poetry run mike --debug list --branch=docs-site --deploy-prefix=web
docs-delete-version:
	poetry run mike --debug delete --branch=docs-site --deploy-prefix=web $(VERSION)
docs-set-default:
	poetry run mike --debug set-default --branch=docs-site --push --deploy-prefix=web latest
build-static-docs: build-docs-static update-git-docs
build-versioned-docs: build-docs-mike docs-set-default
