from pyapp.conf import settings

# Ensure settings are configured
settings.configure(["pyapp_ext.redis.default_settings", "tests.settings"])
