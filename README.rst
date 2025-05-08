===================
My Website Persons
===================

The **My Website Module** is a custom Odoo add-on that extends the functionality of the website module. It introduces new features and enhancements to improve website management and user experience.

Key Features
========
- **Feature 1**: Created a model for persons to the website module with list and form views.
.. image:: model.png
.. image:: views.png
- **Feature 2**: Implemented a controller to handle the display of persons on the website.
.. image:: persons_list.png
- **Feature 3**: Developed a template to create a new person.
.. image:: add_person.png

Dependencies
========
This module depends on the Website module in Odoo.

Data Files Included:
========
- **Security Settings**:
    - `security/ir.model.access.csv` defines access controls for managing records.
- **Views**:
    - `views/person_views.xml` for managing persons in the backend.
    - `views/menu_views.xml` for adding menu items for navigation.
    - `views/website_templates.xml` for website-related UI templates.
- **Technical Details**:
    - `__init__.py` file indicates that the module contains both models and controllers.
        - Models: Define the data structure and logic for persons.
        - Controllers: Handle the website's routing and functionality.