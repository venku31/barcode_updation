from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in barcode_updation/__init__.py
from barcode_updation import __version__ as version

setup(
	name="barcode_updation",
	version=version,
	description="Barcode updation",
	author="venkatesh nayak",
	author_email="vn2019453@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
