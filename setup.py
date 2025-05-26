from setuptools import setup, find_packages

setup(
    name="sortmaster",
    version="0.1.0",
    author="Marcelo Rivera",
    author_email="ma.riveracontreras@duocuc.cl",
    description="Herramienta para organizar y gestionar archivos automáticamente.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/marceloriv/SortMaster",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=open("requirements.txt", encoding="utf-8").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    include_package_data=True,
)
