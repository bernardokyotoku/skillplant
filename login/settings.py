FACEBOOK_APP_ID = '163593707021590'
FACEBOOK_API_KEY = 'f57618bd76404bb67db38d53f7e84d63'
FACEBOOK_API_SECRET = '4f0436b35427ff75764247ff76f5ef2a'
FACEBOOK_REDIRECT_URI = 'http://app.bernardo.kyotoku.org/login'

AUTHENTICATION_BACKENDS = (
    'login.backends.FacebookBackend',
)
