from setuptools import setup, find_packages

print(find_packages())

setup(
    name='spano',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['flask', 'python-magic', 'Flask-HashFS', 'Flask-IndieAuth'],
)
