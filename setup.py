from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in student_management/__init__.py
from student_management import __version__ as version

setup(
	name="student_management",
	version=version,
	description="Student Management System",
	author="student",
	author_email="student@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
