Mopidy skill for Snips
=====================

|Build Status| |PyPI| |MIT License|


Installation
------------

The skill is on `PyPI <https://pypi.python.org/pypi/snipsMopidy>`_, so you can just install it with `pip <http://www.pip-installer.org>`_:

.. code-block:: console

    $ pip install snipsMopidy

Snips Skills Manager
^^^^^^^^^^^^^^^^^^^^

It is recommended that you use this skill with the `Snips Skills Manager <https://github.com/snipsco/snipsskills>`_. Simply add the following section to your `Snipsfile <https://github.com/snipsco/snipsskills/wiki/The-Snipsfile>`_:

.. code-block:: yaml

    skills:
      - pip: https://github.com/snipsco/snips-skills-Mopidy
        package_name: snipsMopidy
        class_name: SnipsMopidy

Usage
-----

The skill allows you to control `Mopidy <http://musicpartners.Mopidy.com/docs?q=node/442>`_ speakers. You can use it as follows:

.. code-block:: python

    from snipsMopidy.snipsMopidy import SnipsMopidy

    Mopidy = SnipsMopidy(SPOTIFY_REFRESH_TOKEN)
    Mopidy.play_artist("John Coltrane")

The ``SPOTIFY_REFRESH_TOKEN`` is used for playing music from Spotify. You can obtain it from the `Snips Spotify Login <https://snips-spotify-login.herokuapp.com>`_ page.

Copyright
---------

This skill is provided by `Snips <https://www.snips.ai>`_ as Open Source software. See `LICENSE.txt <https://github.com/snipsco/snips-skill-hue/blob/master/LICENSE.txt>`_ for more
information.

.. |Build Status| image:: https://travis-ci.org/snipsco/snips-skill-Mopidy.svg
   :target: https://travis-ci.org/snipsco/snips-skill-Mopidy
   :alt: Build Status
.. |PyPI| image:: https://img.shields.io/pypi/v/snipsMopidy.svg
   :target: https://pypi.python.org/pypi/snipsMopidy
   :alt: PyPI
.. |MIT License| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/snipsco/snips-skill-hue/master/LICENSE.txt
   :alt: MIT License
