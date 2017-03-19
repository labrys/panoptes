# coding=utf-8

from client.tvdb.sessions.auth.v2 import TVDBAuth, TVDBUserAuth


def test_auth(api_key):
    auth = TVDBAuth(api_key='')


def test_user_auth():
    user_auth = TVDBUserAuth('knossos', '7B874EB7880EF522', 'DE1EAEFAD0F4587D')
