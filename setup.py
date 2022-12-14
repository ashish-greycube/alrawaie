from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in alrawaie/__init__.py
from alrawaie import __version__ as version

setup(
	name="alrawaie",
	version=version,
	description="Trial Balance customization app",
	author="Greycube Technologies",
	author_email="info@greycube.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
