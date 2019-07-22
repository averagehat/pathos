===============
Installation
===============


With Docker:

.. code-block:: bash

  $ docker build -t pathos .
  $ docker run  <...>

Without:

.. code-block:: bash

    curl -sSL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh && \ 
    conda install -y python=3.6 && \
    git clone https://github.com/averagehat/pathos && \
    cd install && bash assume-conda-install.sh /usr/local/bin/ 
