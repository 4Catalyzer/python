from setuptools import setup


setup(
    name='flake8-config-4catalyzer',
    version='0.1.0',
    url='https://github.com/4Catalyzer/python/blob/packages/flake8-config-4catalyzer',
    author="Alex Rothberg",
    author_email='arothberg@4catalyzer.com',
    license='MIT',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    keywords='flake8',
    install_requires=('flake8', 'flake8-import-order', 'flake8-bugbear'),
)
