from pyramid.config import Configurator


def main(global_config, **settings):

    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.add_static_view(name='static', path='untitled:static')
    config.scan()
    return config.make_wsgi_app()
