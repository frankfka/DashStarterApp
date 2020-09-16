from views.home_page.layout import layout as home_page_layout
from views.graphs_page.layout import layout as graph_page_layout
import views.routes as routes

"""
This file exposes a `pages` dictionary, which maps a particular route to the appropriate layout. Putting this variable
in the `__init__` file allows us to import the dictionary directly from the `views` module.
"""
pages = {
    routes.HOME_ROUTE: home_page_layout,
    routes.GRAPHS_PAGE_ROUTE: graph_page_layout,
}
