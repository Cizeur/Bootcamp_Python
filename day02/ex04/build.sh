#!/bin/bash
rm -rf ai42
mkdir -p ai42
mkdir -p ai42/logging
cp log.py ./ai42/logging/
cp progressbar.py ./ai42/
touch ./ai42/__init__.py
touch ./ai42/logging/__init__.py
cat > setup.py << End
# import setup function from
# python distribution utilities

from setuptools import setup, find_packages

# Calling the setup function
setup(
    name='ai42',
    version='1.0.0',
    packages=find_packages(),
    author='Cesar',
    author_email='None of your business',
    url='https://github.com/Cizeur',
    description='basic lib',
    keywords='basic',
)

End
python setup.py sdist
rm setup.py
rm -rf setup.py
rm -rf ai42
