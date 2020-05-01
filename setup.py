from setuptools import setup

setup(
   name='hdfc parser',
   version='1.0',
   description='HDFC Credit Card Statement converter to csv',
   author='santosh',
   author_email='santosh.siddarth123@gmail.com',
   packages=['hdfc-parser'],  #same as name
   install_requires=['tabula-py'], #external packages as dependencies
)