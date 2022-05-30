"""Make diagrams for biological entities.

Import the package::

   import biogram

This is the complete API reference:

.. autosummary::
   :toctree: .

   create_schema_graph
   view
"""

__version__ = "0.0.2"

from ._sqlalchemy import create_schema_graph, create_uml_graph  # noqa
from ._utils import view
