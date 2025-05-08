{ # noqa
    "name": "My Website Persons",
    "version": "1.0",
    "summary": "Manage persons information",
    "description": """
        Module for managing persons with their basic information.
    """,
    "category": "Website",
    "author": "IvannaKuzin",
    "depends": ["website"],
    "data": [
        "security/ir.model.access.csv",
        "views/person_views.xml",
        "views/menu_views.xml",
        "views/website_templates.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}