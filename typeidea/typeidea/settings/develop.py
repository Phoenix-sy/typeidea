from .base import * #NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


INSTALLED_APPS += [
	#'debug_toolbar',
	#'pympler',
	#'debug_toolbar_line_profiler',
	'silk',
]


MIDDLEWARE += [
	#'debug_toolbar.middleware.DebugToolbarMiddleware',
	'silk.middleware.SilkyMiddleware',
]

DEBUG_TOOLBAR_CONFIG = {
	"JQUERY_URL": '//cdn.bootcss.com/jquery/2.2.4/jquery.min.js',

}

DEBUG_TOOLBAR_PANELS = [
	#'djdt_flamegraph.FlamegraphPanel'
	#'pympler.panels.MemoryPanel',
	'debug_toolbar_line_profiler.panel.ProfilingPanel',
]

INTERNAL_IPS = ['127.0.0.1']