from setuptools import setup, find_packages

setup(
    name="crosschexcloudapi",  # package name
    version="0.1.0",
    description="Anviz CrossChex Cloud API Python integration library",
    author="Sreethul Krishna",
    author_email="sreethulkrishna24@gmail.com",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "requests>=2.28.0",
    ],
    url="https://github.com/KSreethul/crosschexcloudapi",
    license="LGPL-3.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Hardware :: Hardware Drivers",
    ],
)
