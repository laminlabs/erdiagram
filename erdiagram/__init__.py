"""Make diagrams for SQLAlchemy.

The underlying code is heavily based on the MIT-licensed https://github.com/fschulze/sqlalchemy_schemadisplay and contains its copyright notice!

Import the package::

   import erdiagram

This is the complete API reference:

.. autosummary::
   :toctree: .

   create_schema_graph
   view
"""

__version__ = "0.1.3"

from ._sqlalchemy import create_schema_graph, create_uml_graph  # noqa
from ._utils import view
