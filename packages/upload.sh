rm dist/*.whl dist/*.gz
python3 -m pip uninstall pythonnn -y
python3 -m build
python3 -m twine upload --repository testpypi dist/* -u __token__ -p pypi-AgENdGVzdC5weXBpLm9yZwIkNjJkMzBlODEtNDBlZS00MGQyLTllMjEtZjBiNjM5ZjZmMzZjAAIqWzMsIjExZWVmMzQ2LTVkZTAtNDcyMS05MWNkLThiMzBhMWZhNDEyZSJdAAAGIHeGhagAXzw08a56Pa97dYeJ1ZU4Vyepic_4GJSfzYvo

