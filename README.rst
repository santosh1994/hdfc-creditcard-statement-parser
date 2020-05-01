===============================================
HDFC Credit Card statement PDF to CSV Converter
===============================================

Core feature:
  * Parse credit card statement
  * Export transactions into csv
  * Generate rewards for 10X smartbuy partners


Prerequisites
~~~~~~~~~~~~~
Install dependencies through pip

.. code-block:: bash

    pip install -r requirements.txt
    pip install -e . 


Usage
~~~~~
.. code-block:: bash

    python parser.py --statement-path <path to statements>

    --statement-path STATEMENT_PATH
                            path to statements pdf file or directory
    --show-diners-rewards SHOW_DINERS_REWARDS
                            show diners 10x rewards