# -*- coding: utf-8 -*-
"""jupyter_notebook_config.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pIa3o-Pfw5Z3go7tLBzZ63_E_ldlffmR
"""

c = get_config()  # get the config object
c.IPKernelApp.pylab = 'inline'  # in-line figure when using Matplotlib
c.NotebookApp.ip = '*'  
c.NotebookApp.open_browser = False  # do not open a browser window by default when using notebooks
c.NotebookApp.token = '' # No token. Always use jupyter over ssh tunnel
c.NotebookApp.notebook_dir = '/notebooks'
c.NotebookApp.allow_root = True # Allow to run Jupyter from root user inside Docker container