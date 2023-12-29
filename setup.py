import setuptools


with open("README.md", "r") as desc:
    long_description = desc.read()

setuptools.setup(
    name="tkhtmlview",
    version="0.0.1",
    author="Benit Mulindwa",
    keywords="flet html developement python",
    description="Embed HTML code on your flet app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Benitmulindwa/FletifyHTML",
    project_urls={
        "Documentation": "https://github.com/Benitmulindwa/FletifyHTML",
        "Source": "https://github.com/Benitmulindwa/FletifyHTML",
        "Tracker": "https://github.com/Benitmulindwa/FletifyHTML/issues",
    },
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8.*",
    install_requires=["flet>=0.11.0", "requests>=2.22.0", "bs4>=0.0.1"],
)
