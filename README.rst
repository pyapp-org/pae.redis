#############
pyApp - Redis
#############

*Let us handle the boring stuff!*

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
      :alt: Once you go Black...


Installation
============

Install using *pip*::

    pip install pae.redis

Install using *pipenv*::

    pipenv install pae.redis


Add `pae.redis` into the `EXT` list in your applications 
`default_settings.py`.

Add the `REDIS` block into your runtime settings file::

    REDIS = {
        "default": {
            "url": "redis://user:pass@host:port/1",
        },
    }


Usage
=====



API
===
