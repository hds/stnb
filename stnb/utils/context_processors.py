from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.sites.models import get_current_site

def ganalytics_js(request):
    """
    Adds google analytics to a page, using the tracking code specified in the
    settings variable GA_TRACKER.
    """
    
    try:
        ga_code = settings.GA_TRACKER
    except:
        ga_code = None

    if ga_code:
        ganalytics_js = """        <script type="text/javascript">
          var _gaq = _gaq || [];
          _gaq.push(['_setAccount', '%(ga_code)s'],
                    ['_setDomainName', '%(site)s'],
                    ['_trackPageview']);
          (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
          })();
        </script>""" % { 'ga_code': ga_code,
                         'site': get_current_site(request).domain, }
    else:
        ganalytics_js = ''

    return {'ganalytics_js': mark_safe(ganalytics_js)}

