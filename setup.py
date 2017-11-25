from setuptools import setup, find_packages
from kayla import __version__, __author__, __email__, __url__

setup(
    name='kayla-project',
    # packages=['kayla', 'kayla.exception', 'kayla.hash', 'kayla.signature', 'kayla.utils'],
    packages=find_packages(where='.', exclude=[
        'sample_code',
        'tests',
    ]),
    version=__version__,
    description='Utility package',
    author=__author__,
    author_email=__email__,
    url=__url__,
    keywords=['kayla', 'utility', 'helpers', 'library'],
)
