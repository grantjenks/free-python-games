Free Python Games Development
=============================

:doc:`Free Python Games <index>` development is lead by Grant Jenks
<contact@grantjenks.com>.

Collaborators Welcome
---------------------

#. Search issues or open a new issue to start a discussion around a bug.
#. Fork the `GitHub repository`_ and make your changes in a new branch.
#. Write a test which shows the bug was fixed.
#. Send a pull request and message the development lead until its merged and
   published.

.. _`GitHub repository`: https://github.com/grantjenks/free-python-games/

Requests for Contributions
--------------------------

#. Simplifications to existing games.
#. Refactoring to simplify games.
#. Improved documentation.
#. Additional games. Requirements for new games:

   #. Fun to play.
   #. Matching code style.
   #. Limited Python feature set.
   #. Short (less than 100 lines of code).

Get the Code
------------

:doc:`Free Python Games <index>` is actively developed in a `GitHub
repository`_.

You can either clone the public repository::

    $ git clone https://github.com/grantjenks/free-python-games.git

Download the `tarball <https://github.com/grantjenks/free-python-games/tarball/master>`_::

    $ curl -OL https://github.com/grantjenks/free-python-games/tarball/master

Or, download the `zipball <https://github.com/grantjenks/free-python-games/zipball/master>`_::

    $ curl -OL https://github.com/grantjenks/free-python-games/zipball/master

Installing Dependencies
-----------------------

Install development dependencies with `pip <http://www.pip-installer.org/>`_::

    $ pip install -r requirements.txt

All packages for running tests and building documentation will be installed.

Testing
-------

:doc:`Free Python Games <index>` currently tests against three versions of
Python:

* CPython 3.4
* CPython 3.5
* CPython 3.6

Testing uses `tox <https://pypi.python.org/pypi/tox>`_. If you don't want to
install all the development requirements, then, after downloading, you can
simply run::

    $ python setup.py test

The test argument to setup.py will download a minimal testing infrastructure
and run the tests.
