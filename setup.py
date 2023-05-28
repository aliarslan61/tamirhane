from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tamirhane/__init__.py
from tamirhane import __version__ as version

setup(
	name="tamirhane",
	version=version,
	description="Tamirhane Yönetim Merkezi",
	author="Ali Arslan",
	author_email="arslan.ahmet93@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
