from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    LONG_DESCRIPTION=fh.read()

setup(name='pype',
      version='1.0',
      description='Python-integrated functional programming language - Provides easy-to-use pseudo-macros for common functional programming tasks such as maps, reduces, filters, conditionals, dictionary manipulations, and list manipulations..',
      long_description=LONG_DESCRIPTION,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Functional Programming :: Macros',
      ],
      keywords='functional map reduce filter lambda',
      url='https://github.com/bbbdragon/python-pype-lang',
      author='bbbdragon',
      author_email='bbbdragon@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'numpy',
      ],
      include_package_data=True,
      zip_safe=False)
