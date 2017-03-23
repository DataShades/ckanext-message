import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class MessagePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'message')
     
    # IRoutes - redirect to our custom home page
    def before_map(self, m):
        m.redirect('/', 'http://dev.edptest.info/edphome/SearchResults.aspx')
        m.redirect('/dataset', 'http://dev.edptest.info/edphome/SearchResults.aspx')
        return m
