import os
from setuptools import setup
from cx_Freeze import setup , Executable
import os

home=os.path.expanduser('~')

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Bubble Crusher",
    version = "0.9.5",
    author = "Thibault Duponchelle",
    author_email = "thibault.duponchelle@gmail.com",
    description = ("A funny game "),
    license = "GPL",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['bubblecrusher'],
    package_dir={'bubblecrusher': 'bubblecrusher'},
    package_data={'bubblecrusher': ['data/pixs/*.*','data/pixs/font/*.*','data/pixs/logo/*.*']},
    #data_files=[(home + '/.bubblecrusher/', ['bubblecrusher/data/bubble.cfg'])],
    include_package_data = True,
    long_description=read('README.md'),
    install_requires = ['PyGTK', 'setuptools'],
    scripts = ['scripts/bubblecrusher'],
    classifiers=[
        "Development Status :: 3 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)

