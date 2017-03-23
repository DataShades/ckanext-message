import pylons
import ckan
import ckan.lib
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic as logic
import ckan.model as model
import ckan.controllers
from ckan.controllers.user import UserController 
import ckan.lib.helpers as h 
import ckan.lib.base as base
import logging 
from logging import getLogger
from ckan.common import _, c, g, request, response
from ckan.model import User, Package, PackageExtra
import urllib
import urllib2
from sqlalchemy import distinct
import os
import ckan.model.meta as meta
from sqlalchemy import distinct


log = logging.getLogger(__name__)

def user_list(context,data_dict):
    user = context['user']
    if user:
       return {'success':True}
    else:
       h.redirect_to('/user/login')

#def upassword():
var =  []



class MessagePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.IResourceController, inherit=True)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IAuthenticator, inherit=True)


    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'message')
    
    #IAuthenticator
    def login(self):
        pass
 
    def identify(self):
        log.debug(request.environ['CKAN_CURRENT_URL'].split('?'))
        if request.environ['CKAN_CURRENT_URL'].split('?')[0]=='/user/logged_in':
            if var:
               log.debug("var has value once logged in, clearing var")
               del var[:]
               return var
            else:
               #log.debug("var does not have value once logged in")
               pass
        if hasattr(toolkit.c.userobj,'password'):
            upassword=getattr(toolkit.c.userobj,'password')
            if var:
               log.debug('existing var')
               log.debug(var)
               if upassword == var[0]:
                  log.debug("same, pass")
                  #log.debug(upassword)    
                  pass
               else:
                  var[0]=upassword
                  log.debug("different, do stuff")
                  #log.debug(upassword)
                  #this toolkit redirect does not do what user expects)
                  toolkit.redirect_to(controller='user',action='logout',  __ckan_no_root=True, id=None)
                  #h.redirect_to('http://ckan.dev.edptest.info/user/logout')
                  #to do - this logs the user out, but does not redirect user to the "you have been logged out" page.
                  #return render('user/logout.html') 
            else: 
               log.debug("var is appended")
               var.append(upassword)
        else:
            pass
       

    def logout(self):
        pass
    
    #def abort(self, status_code, detail, headers, comment):
    #    pass

    
    
    # IAuthfunctions
    def get_auth_functions(self):
        return {'user_list':user_list}
     
    # IRoutes - redirect to our custom home page
    def before_map(self, m):
        m.redirect('/', 'http://dev.edptest.info/edphome/SearchResults.aspx')
        m.redirect('/dataset', 'http://dev.edptest.info/edphome/SearchResults.aspx')
        m.redirect('/user/register', 'http://dev.edptest.info')
        return m
  
    # IResource controller - dynamic urls for resources with Seed web map
    def before_show(self, resource_dict):
        pkg = model.Package.get(resource_dict['package_id'])
        #log.debug(pkg.extras)
        seedwebmap = 'SEED Web Map'
        if resource_dict['format'].lower()==seedwebmap.lower():
           resource_dict['url'] = 'http://geo.dev.edptest.info/EDP_Public_Viewer/Index.html?viewer=EDP_Public_Viewer&run=ViewMap&url='+pkg.extras['map_type']+":map_service_id="+pkg.extras['map_service_id'].replace("&","+")+";layer_id="+pkg.extras['layer_id'].replace("&","+")
           #log.debug(url)
        return resource_dict
        
