from setuptools import setup

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'Mahfuz Islam Khan Jabed'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ["streamlit"]

setup(
    name=SRC_REPO,
    version='2.2.0',
    author=AUTHOR_NAME,
    author_email='mahfuzislam1410@gmail.com',
    description='A straightforward Python package designed for crafting uncomplicated web applications.',
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    package=[SRC_REPO],
    python_requires= '>=3.7',
    install_requires= LIST_OF_REQUIREMENTS,
)