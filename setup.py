# Licensed under a 3-clause BSD style license - see LICENSE.rst
from setuptools import setup
from acis_taco import __version__
try:
    from testr.setup_helper import cmdclass
except ImportError:
    cmdclass = {}

setup(name='acis_taco',
      author='Tom Aldcroft',
      description='ACIS Earth Solid Angle package',
      author_email='aldcroft@head.cfa.harvard.edu',
      url='http://cxc.cfa.harvard.edu/mta/ASPECT/tool_doc/taco/',
      version=__version__,
      zip_safe=False,
      packages=['acis_taco'],
      cmdclass=cmdclass,
      )


