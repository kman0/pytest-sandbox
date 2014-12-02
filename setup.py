__author__ = 'M'
from setuptools import setup
import codecs

# long_description = codecs.open("README.md", encoding='utf-8').read()

VERSION = '0.1'
PYPI_VERSION = '0.1'

setup(
    name='pytest-sandbox',
    description='Creates a sandbox temp directory and executes tests inside it',
    # long_description=long_description,
    version=VERSION,
    url='https://github.com/manojklm/pytest-sandbox/',
    download_url='https://github.com/manojklm/pytest-sandbox/tarball/%s' % PYPI_VERSION,
    license='MIT',
    author='mk',
    author_email='manojklm@gmail.com',
    entry_points={'pytest11': ['sandbox = pytest_sandbox']},
    py_modules=['pytest_sandbox'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['pytest>=2.6'],
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


