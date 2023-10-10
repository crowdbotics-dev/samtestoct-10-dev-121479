"""
WSGI config for samtestoct_10_dev_121479 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "samtestoct_10_dev_121479.settings"
)

application = get_wsgi_application()
