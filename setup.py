from setuptools import setup, find_packages

version = '2.0a3'

setup(name='plone.app.workflow',
      version=version,
      description="workflow and security settings for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Martin Aspeli',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.app.workflow',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages = ['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
            'Products.CMFCalendar',
            'Products.PloneTestCase',
        ]
      ),
      install_requires=[
        'setuptools',
        'kss.core',
        'plone.memoize',
        'plone.app.kss',
        'transaction',
        'zope.component',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.schema',
        'Plone',
        'Products.CMFCore',
        'Products.DCWorkflow',
        'Products.statusmessages',
        'Acquisition',
        'DateTime',
        'Zope2',
      ],
      )
