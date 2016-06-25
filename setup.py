from setuptools import setup

setup(name='simind',
      version='0.0.1',
      description='Compute various incidence based or abundance based similarity indices between two numpy arrays.',
      url='https://bitbucket.org/benmaier/similarity-indices',
      author='Benjamin F. Maier',
      author_email='benjaminfrankmaier@gmail.com',
      license='MIT',
      packages=['simind'],
      install_requires=[
          'numpy',
      ],
      dependency_links=[
          ],
      zip_safe=False)
