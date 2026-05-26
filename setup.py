from setuptools import setup, find_packages
setup(name='netbox-free-ip', version='1.0.0',
    description='NetBox plugin — wolne zakresy IP w prefiksie',
    packages=find_packages(), include_package_data=True,
    install_requires=[], python_requires='>=3.12')
