from setuptools import setup, find_packages

with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()

with open("requirements.txt", "r") as file:
    DEPENDENCIES = file.readlines()

setup(
    name="mkdocs-pure",
    version="0.2",
    description="Pure theme for MkDocs",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    keywords="mkdocs pure theme",
    project_urls={
        "Source": "https://github.com/notoriginalnik/mkdocs-pure"
    },
    author='notoriginal',
    author_email='notoriginalnik@gmail.com',
    include_package_data=True,
    license="BSD",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    install_requires=DEPENDENCIES,
    packages=find_packages(),
    entry_points={
        'mkdocs.themes': [
            'pure = mkdocs_pure',
        ]
    },
	zip_safe=False
)