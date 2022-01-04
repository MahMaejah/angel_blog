from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in angel_blog/__init__.py
from angel_blog import __version__ as version

setup(
	name="angel_blog",
	version=version,
	description="Blog for Angel",
	author="Chipo Hameja",
	author_email="chipohameja@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
