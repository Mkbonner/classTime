from setuptools import setup, find_packages

setup(
    name='jokes',
    version='1.0.0',
    url='https://github.com/Mkbonner/classTime.git',
    author='Matthew Bonner',
    author_email='fake_email@hotmail.com',
    description='Undecided',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'pandas >= 1.1'],
)
