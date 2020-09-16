from typing import List, Tuple, Dict

import dash_bootstrap_components as dbc

"""
This file holds the component function for creating the navigation bar. In general, component functions should be dummy
and should not hold any state. Instead, state should be passed through appropriate arguments such that callbacks
can use the component function to update views.
"""


def __create_nav_link_style__(is_active: bool) -> Dict:
    """
    Create the appropriate style for the navigation link, highlighting the link if the route is active
    """
    style = {}
    if is_active:
        style["color"] = "lightblue"
    return style


def __create_nav_item__(entry: Tuple[str, str, bool]) -> dbc.NavItem:
    """
    Creates a navigation item for the navigation bar, each tuple is (Name, Path, IsActive)
    """
    is_active = entry[2] or False
    return dbc.NavItem(
        dbc.NavLink(
            entry[0],
            href=entry[1],
            active=is_active,
            style=__create_nav_link_style__(is_active)
        )
    )


def create_navbar(
        brand_name: str,
        brand_path: str,
        nav_links: List[Tuple[str, str, bool]]
) -> dbc.NavbarSimple:
    """
    Creates a Nav Bar components

    :param brand_path: A URL path for the brand link
    :param brand_name: Text to display as the brand name
    :param nav_links: a list of (Name, Path, IsActive) tuples
    :return: Nav Bar
    """
    return dbc.NavbarSimple(
        children=list(
            map(__create_nav_item__, nav_links)
        ),
        brand=brand_name,
        brand_href=brand_path,
        color="primary",
        dark=True,
    )
