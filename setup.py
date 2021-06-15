import io
import setuptools as st
import sys

from setuptools.command.test import test as TestCommand

import freegames


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox

        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


with io.open('README.rst', encoding='UTF-8') as reader:
    readme = reader.read()


st.setup(
    name='freegames',
    version=freegames.__version__,
    description='Free Games',
    long_description=readme,
    author='Grant Jenks',
    author_email='contact@grantjenks.com',
    url='http://www.grantjenks.com/docs/freegames/',
    packages=['freegames'],
    include_package_data=True,
    tests_require=['tox'],
    cmdclass={'test': Tox},
    license='Apache 2.0',
    install_requires=[],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Games/Entertainment',
        'Topic :: Games/Entertainment :: Arcade',
        'Topic :: Games/Entertainment :: Board Games',
        'Topic :: Games/Entertainment :: Puzzle Games',
        'Topic :: Games/Entertainment :: Side-Scrolling/Arcade Games',
        'Topic :: Games/Entertainment :: Simulation',
        'Topic :: Games/Entertainment :: Turn Based Strategy',
    ),
)
