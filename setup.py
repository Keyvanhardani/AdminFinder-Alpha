from setuptools import setup

setup(
    name='adminfinder',
    version='1.0.3',
    description='A tool for finding admin panels and login pages',
    long_description='A tool for finding admin panels and login pages. It uses a list of paths and a list of common admin panels and login pages to perform the search.',
    url='https://github.com/username/adminfinder-alpha',
    author='Keyvan Hardani',
    author_email='dev@keyvvan.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='admin panel login page finder',
    packages=['adminfinder'],
    entry_points={
        'console_scripts': [
            'adminfinder=adminfinder.app:main'
        ]
    },
    install_requires=[
        'requests'
    ],
)