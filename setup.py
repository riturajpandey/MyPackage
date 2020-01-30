from setuptools import setup
with open ("README.md","r") as fh :
    long_description = fh.read()

setup(
    name='MyPackage',
    version='1.1',
    packages=['Test'],
    url='https://github.com/riturajpandey/MyPackage/',
    license='GNU GENERAL PUBLIC',
    author='Ashwini Bokade',
    author_email='ashwini_bokade@yahoo.com',
    description='Test Package',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI APPROVED :: GNU General Public License v3"
        "Operating System :: OS Independent",
        "long_description=long_description",
        "long_description_content_type=text/markdown"
    ]
)
