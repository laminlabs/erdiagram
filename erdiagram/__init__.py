"""Make diagrams for SQLAlchemy.

Heavily based on the MIT-licensed https://github.com/fschulze/sqlalchemy_schemadisplay!

Import the package::

   import erdiagram

This is the complete API reference:

.. autosummary::
   :toctree: .

   create_schema_graph
   view
"""

__version__ = "0.1.0"

from ._sqlalchemy import create_schema_graph, create_uml_graph  # noqa
from ._utils import view
