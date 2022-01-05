from setuptools import find_packages, setup

setup(
    name='netbox-slm',
    version='0.9',
    description='Software Lifecycle Management Netbox Plugin',
    url='https://github.com/ICTU/netbox_slm',
    author='Hedde van der Heide',
    license='Apache 2.0',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
