from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
#    py_modules = ['rss_reader', 'app'],

setup(
    name = 'rss-reader',
    version = '1.5',
    author = 'Olga VarivonchiK',
    author_email = '_alex@tut.by',
    license = 'BSD_setup.py',
    description = 'RSS parser',
    long_description='RSS parser using Python v3.9',    
    #packages=find_packages(include=['src','src.*']),
    packages=find_packages(),    
    #package_dir={'': 'src'},
    package_data={
        '': ['*.ttf'],
    },
    install_requires=[requirements],    
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': [
                'rss_reader=rssreader.rss_reader:main',
        ],
    },
)