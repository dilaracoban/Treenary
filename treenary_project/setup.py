from setuptools import setup, find_packages

setup(
    name='treenary_project',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'treenary=main:main'
        ]
    },
    install_requires=[
        'argparse',
        'ete3'
    ],
    author='Your Name',
    description='Command-line tool for encoding phylogenetic tree nodes into Treenary strings.',
)
