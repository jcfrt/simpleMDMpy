from setuptools import setup, find_packages

setup(
    name='simpleMDMpy',
    version='3,0,7',
    url='https://github.com/macadmins/simpleMDMpy',
    author='SteveKueng',
    author_email='steve.kueng@srgssr.ch',
    description='python lib for simpleMDM API',
    packages=find_packages(),
    install_requires=['requests'],
)
