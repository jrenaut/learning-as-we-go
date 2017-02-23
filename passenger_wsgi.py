#!/home/lawgadmin/awgpodcast.com/env/bin/python
import sys, os
INTERP = "/home/lawgadmin/awgpodcast.com/env/bin/python"
#INTERP is present twice so that the new python interpreter knows the actual executable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append('/home/lawgadmin/awgpodcast.com/learning-as-we-go/')  #You must add your project here

sys.path.insert(0,cwd+'/env/bin')
sys.path.insert(0,cwd+'/env/lib/python2.7/site-packages/django')
sys.path.insert(0,cwd+'/env/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "lawgo.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

