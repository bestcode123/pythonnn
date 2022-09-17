rm dist/*.whl dist/*.gz
python3 -m pip uninstall pythonnn -y
python3 -m build
python3 -m twine upload --repository testpypi dist/*
pip install -i https://test.pypi.org/simple/ pythonnn
