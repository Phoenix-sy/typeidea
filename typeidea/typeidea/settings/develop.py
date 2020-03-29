from .base import * #NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': '1234567890',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


INSTALLED_APPS += [
	'debug_toolbar',
	#'pympler',
	#'debug_toolbar_line_profiler',
	#'silk',
]


MIDDLEWARE += [
	'debug_toolbar.middleware.DebugToolbarMiddleware',
	#'silk.middleware.SilkyMiddleware',
]

DEBUG_TOOLBAR_CONFIG = {
	"JQUERY_URL": '//cdn.bootcss.com/jquery/2.2.4/jquery.min.js',

}
'''
DEBUG_TOOLBAR_PANELS = [
	#'djdt_flamegraph.FlamegraphPanel'
	#'pympler.panels.MemoryPanel',
	'debug_toolbar_line_profiler.panel.ProfilingPanel',
]
'''
INTERNAL_IPS = ['127.0.0.1']