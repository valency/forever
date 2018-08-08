from os import path

from setuptools import setup, find_packages

with open(path.join(path.abspath(path.dirname(__file__)), 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='forever',
    version='0.8.8',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/valency/forever/',
    author='Deepera Co., Ltd.',
    author_email='yding@deepera.com',
    description='Forever: auto restart any script if it stops printing.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    keywords=['forever', 'logging', 'auto-restart'],
    install_requires=[]
)
