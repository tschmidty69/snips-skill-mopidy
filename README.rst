Mopidy skill for Snips
=====================

|Build Status| |PyPI| |MIT License|


Installation
------------

Snips Skills Manager
^^^^^^^^^^^^^^^^^^^^

It is recommended that you use this skill with the `Snips Skills Manager <https://github.com/snipsco/snipsskills>`_. Simply add the following section to your `Snipsfile <https://github.com/snipsco/snipsskills/wiki/The-Snipsfile>`_:

.. code-block:: yaml

    skills:
      - url: github.com/snipsco/snips-skills-Mopidy
        param:
          mopidy_host: YOUR_IP # defaults to localhost

Usage
-----

The skill allows you to control `Mopidy <http://musicpartners.Mopidy.com/docs?q=node/442>`_ server. You can use it as follows:

