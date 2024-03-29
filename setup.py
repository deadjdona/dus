import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = [
    # Add your list of production dependencies here, eg:
    # 'requests == 2.*',
]

DEV_REQUIREMENTS = [
    'black >= 22,< 25',
    'build >= 0.7,< 1.1',
    'flake8 >= 4,< 8',
    'isort == 5.*',
    'mypy == 1.8.0',
    'pytest >= 7,< 9',
    'pytest-cov == 4.*',
    'twine >= 4,< 6',
]

setuptools.setup(
    name='PROJECT_NAME_URL',
    version='0.1.0',
    description='Your project description here',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/USERNAME/PROJECT_NAME_URL',
    author='USERNAME',
    license='MIT',
    packages=setuptools.find_packages(
        exclude=[
            'examples',
            'test',
        ]
    ),
    package_data={
        'PROJECT_NAME_URL': [
            'py.typed',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    entry_points={
        'console_scripts': [
            'PROJECT_NAME_URL=project_name.my_module:main',
        ]
    },
    python_requires='>=3.7, <4',
)
