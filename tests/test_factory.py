from redis import Redis

from pyapp_ext.redis import factory


class TestClientFactory:
    def test_session_factory(self):
        target = factory.RedisFactory("REDIS")
        actual = target.create()

        assert isinstance(actual, Redis)
