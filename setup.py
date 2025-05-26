from setuptools import setup, find_packages

setup(
    name='python-workspace',
    version='0.1.0',
    author='Tu Nombre',
    author_email='tu.email@example.com',
    description='Descripción del proyecto',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tu_usuario/python-workspace',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)