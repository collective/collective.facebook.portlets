# -*- coding:utf-8 -*-

import os
from setuptools import setup, find_packages

version = '1.0b3.dev0'
description = "This package implements some Facebook Social Plugins as \
portlets for your Plone site."
long_description = open("README.txt").read() + "\n" + \
                   open(os.path.join("docs", "INSTALL.txt")).read() + "\n" + \
                   open(os.path.join("docs", "CREDITS.txt")).read() + "\n" + \
                   open(os.path.join("docs", "HISTORY.txt")).read()

setup(name='collective.facebook.portlets',
      version=version,
      description=description,
      long_description=long_description,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone portlet facebook',
      author='Franco Pellegrini',
      author_email='frapell@gmail.com',
      url='https://github.com/collective/collective.facebook.portlets',
      license='GPLv2',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.facebook'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'collective.facebook.accounts',
        'collective.prettydate>=1.1',
        'five.grok>=1.2',
        ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
