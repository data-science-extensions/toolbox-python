# Poetry
cd toolbox-python
pip install poetry
pip install --upgrade pip pipenv poetry
poetry --version
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true
poetry config --list
poetry init --no-interaction --name="toolbox-python" --description="Helper files/functions/classes for generic Python processes" --author="Admin <toolbox-python@data-science-extensions.com>" --python=">3.9,<4.0" --license="MIT"
poetry env use $(pyenv which python 3.13.0)
poetry add typeguard
poetry add $(cat requirements/root.txt)
poetry add --group="dev" $(cat requirements/dev.txt)
poetry add --group="docs" $(cat requirements/docs.txt)
poetry add --group="test" $(cat requirements/test.txt)
poetry lock
poetry install --no-interaction --with dev,docs,test
poetry shell
pre-commit install
pre-commit autoupdate

# UV
cd toolbox-python
curl -LsSf https://astral.sh/uv/install.sh | sh
uv self update
uv --version
uv python install=3.13 --link-mode=copy
uv init --python=3.13 --link-mode=copy --lib --name="toolbox-python" --description="Helper files/functions/classes for generic Python processes"
uv add --python=3.13 --link-mode=copy --no-cache typeguard
uv add --python=3.13 --link-mode=copy --no-cache --requirements=requirements/root.txt
uv add --python=3.13 --link-mode=copy --no-cache --requirements=requirements/dev.txt --group=dev
uv add --python=3.13 --link-mode=copy --no-cache --requirements=requirements/docs.txt --group=docs
uv add --python=3.13 --link-mode=copy --no-cache --requirements=requirements/test.txt --group=test
uv lock --python=3.13 --link-mode=copy --no-cache
uv sync --python=3.13 --link-mode=copy --no-cache --all-groups
uv run pre-commit install
uv run pre-commit autoupdate
