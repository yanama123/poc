import setuptools
import re
import os



with open('requirements.txt', 'r') as f:
    install_reqs = [
        s for s in [
            line.strip(' \n') for line in f
        ] if not s.startswith('#') and s != ''
    ]

# Fields marked as "Optional" may be commented out.
setuptools.setup(
    name="test_runer",  # Required
    version=1.0,  # Required
    author="anji",  # Optional
    description="Run test cases",  # Required
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    include_package_data=True,  # Optional
    install_requires=install_reqs)

