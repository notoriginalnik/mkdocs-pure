from setuptools import setup, find_packages

VERSION = '0.2'


setup(
    name="mkdocs-pure",
    version=VERSION,
    url='https://github.com/mkdocs/mkdocs-basic-theme',
    license='BSD',
    description='Pure theme for MkDocs',
    author='notoriginal',
    author_email='notoriginalnik@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'pure = mkdocs_pure',
        ]
    },
    zip_safe=False
)
