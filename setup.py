from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="multigro",
    version="0.0.1",
    author="Hüsamettin Deniz Özeren",
    author_email="denizozeren614@gmail.com",
    description="MultiGRO: Automated methods for GROMACS simulations.",
    url="https://github.com/hozeren/multigro",
    project_urls={
        "Bug Tracker": "https://github.com/hozeren/multigro/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'argv',
        'pandas',
        'nltk',
        'sh',
        'getopt',
        'scipy'
    ],
    packages=find_packages(include=['multigro', 'multigro.*']),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'multigro = multigro.main:main'],
            },
    tests_require=['pytest'],
    setup_requires=['pytest-runner', 'flake8'],
    test_suite='multigro.tests',
)