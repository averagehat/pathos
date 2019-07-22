=============
Pathos Sheet
============= 

.. literalinclude:: ../pathos/pathos_sheet.py
   :start-after: '''
   :end-before: '''

The input samplsheet must be in TSV form with the input sample names in the first column and the control samples on the right column (if there are multiple control samples, each one should be seperated by a semi-colon.)

.. code-block:: bash

  191\t132;133
  192\t132;133
  193;194\t144
