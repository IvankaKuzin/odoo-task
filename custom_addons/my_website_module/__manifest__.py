{ # noqa
    "name": "My Website Persons",
    "version": "1.0",
    "summary": "Manage persons information",
    "description": """
        Module for managing persons with their basic information.
    """,
    "category": "Website",
    "author": "Your Name",
    "depends": ["website"],
    "data": [
        "views/person_views.xml",
        "views/menu_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}