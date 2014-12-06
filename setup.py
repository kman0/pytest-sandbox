__author__ = 'M'
from setuptools import setup
import codecs

VERSION = '0.2'
PYPI_VERSION = '0.2'
DESCRIPTION = (
    "Creates a sandbox temp directory and executes tests inside it"
)
setup(
    name='pytest-sandbox',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    version=VERSION,
    url='https://github.com/manojklm/pytest-sandbox/',
    download_url='https://github.com/manojklm/pytest-sandbox/tarball/%s' % PYPI_VERSION,
    keywords=['pytest', 'sandbox', 'tempdir', 'tests', 'plugin'],
    license='MIT',
    author='mk',
    author_email='manojklm+gh@gmail.com',
    entry_points={'pytest11': ['sandbox = pytest_sandbox']},
    py_modules=['pytest_sandbox'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['pytest>=2.6', 'path.py>=7.0'],
    classifiers=[
        'Environment :: Plugins',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)


