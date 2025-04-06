#* Variables
PYTHON := python3
PACKAGE_NAME := toolbox_python
PYTHONPATH := `pwd`
VERSION ?= v0.0.0
VERSION_CLEAN := $(shell echo $(VERSION) | awk '{gsub(/v/,"")}1')
VERSION_NO_PATCH := "$(shell echo $(VERSION) | cut --delimiter '.' --fields 1-2).*"
UV_LINK_MODE := copy


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
poetry-install-poetry:
	$(PYTHON) -m pip install poetry
	poetry --version
poetry-install:
	poetry lock
	poetry install --no-interaction --only main
poetry-install-dev:
	poetry lock
	poetry install --no-interaction --with dev
poetry-install-docs:
	poetry lock
	poetry install --no-interaction --with docs
poetry-install-test:
	poetry lock
	poetry install --no-interaction --with test
poetry-install-dev-test:
	poetry lock
	poetry install --no-interaction --with dev,test
poetry-install-all:
	poetry lock
	poetry install --no-interaction --with dev,docs,test


#* UV
.PHONY: uv
install-uv:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv --version
uv-self-update:
	uv self update
	uv --version
uv-install-main:
	uv sync --no-cache --no-group=dev --no-group=docs --no-group=test
uv-install-dev:
	uv sync --no-cache --group=dev
uv-install-docs:
	uv sync --no-cache --group=docs
uv-install-test:
	uv sync --no-cache --group=test
uv-install-dev-test:
	uv sync --no-cache --group=dev --group=test
uv-install-all:
	uv sync --no-cache --all-groups
uv-sync-main: uv-install-main
uv-sync-dev: uv-install-dev
uv-sync-docs: uv-install-docs
uv-sync-test: uv-install-test
uv-sync-dev-test: uv-install-dev-test
uv-sync-all: uv-install-all
uv-sync: uv-install-all
uv-update: uv-install-all
install: uv-install-main
install-main: uv-install-main
install-dev: uv-install-dev
install-docs: uv-install-docs
install-test: uv-install-test
install-dev-test: uv-install-dev-test
install-all: uv-install-all


#* Linting
.PHONY: linting
run-black:
	uv run black --config pyproject.toml ./
run-isort:
	uv run isort --settings-file pyproject.toml ./
lint: run-black run-isort


#* Checking
.PHONY: checking
check-black:
	uv run black --diff --check --config pyproject.toml ./
check-mypy:
	uv run mypy --install-types --config-file pyproject.toml src/$(PACKAGE_NAME)
check-isort:
	uv run isort --settings-file pyproject.toml ./
check-codespell:
	uv run codespell --toml pyproject.toml src/ *.py
check-pylint:
	uv run pylint --rcfile=pyproject.toml src/$(PACKAGE_NAME)
check-pytest:
	uv run pytest --config-file pyproject.toml
check-pycln:
	uv run pycln --config="pyproject.toml" src/$(PACKAGE_NAME)
check-build:
	uv build --out-dir=dist
	if [ -d "dist" ]; then rm --recursive dist; fi
check-mkdocs:
	uv run mkdocs build --site-dir="temp"
	if [ -d "temp" ]; then rm --recursive temp; fi
check: check-black check-mypy check-pycln check-isort check-codespell check-pylint check-mkdocs check-build check-pytest


#* Testing
.PHONY: pytest
pytest:
	uv run pytest --config-file pyproject.toml
copy-coverage-report:
	cp --recursive --update "./cov-report/html/." "./docs/code/coverage/"
commit-coverage-report:
	git add .
	git commit --no-verify --message "Update coverage report [skip ci]"
	git push


#* Git
.PHONY: git-processes
git-add-credentials-old:
	git config --global user.name ${GITHUB_ACTOR}
	git config --global user.email "${GITHUB_ACTOR}@users.noreply.github.com"
git-add-credentials:
	git config --global user.name "github-actions[bot]"
	git config --global user.email "github-actions[bot]@users.noreply.github.com"
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


#* Deploy Package
# See: https://github.com/monim67/poetry-bumpversion
.PHONY: deployment
bump-version:
	poetry self add poetry-bumpversion
	poetry version $(VERSION_CLEAN)
	poetry version --short
update-git:
	git add .
	git commit --message="Bump to version \`$(VERSION)\` [skip ci]" --allow-empty
	git push --force --no-verify
	git status
poetry-build:
	poetry build
poetry-configure:
	poetry config pypi-token.pypi ${PYPI_TOKEN}
poetry-publish:
	poetry publish
build-package: poetry-build
deploy-package: poetry-configure poetry-publish


#* Docs
.PHONY: docs
docs-serve-static:
	uv run mkdocs serve
docs-serve-versioned:
	uv run mike serve --branch=docs-site
docs-build-static:
	uv run mkdocs build --clean
docs-build-versioned:
	git config --global --list
	git config --local --list
	git remote -v
	uv run mike --debug deploy --update-aliases --branch=docs-site --push $(VERSION) latest
update-git-docs:
	git add .
	git commit -m "Build docs [skip ci]"
	git push --force --no-verify --push-option ci.skip
docs-check-versions:
	uv run mike --debug list --branch=docs-site
docs-delete-version:
	uv run mike --debug delete --branch=docs-site $(VERSION)
docs-set-default:
	uv run mike --debug set-default --branch=docs-site --push latest
build-static-docs: docs-build-static update-git-docs
build-versioned-docs: docs-build-versioned docs-set-default
