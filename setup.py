from setuptools import setup, find_packages

setup(
	name="python-pin-payments",
	version="0.1.0",  # Increment version for each new release
	author="Viacheslav Lisovoi",
	author_email="viacheslav.lisovoi@onix-systems.com",
	description="Python library for interacting with Pin Payments API",
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	url="https://github.com/Onix-Systems/python-pin-payments",
	packages=find_packages(),
	package_dir={"": "pin_payments"},
	install_requires=[
		"requests==2.32.0",
		"python-dotenv==1.0.1",
	],
	classifiers=[
		"Programming Language :: Python :: 3.10",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.6",
)
