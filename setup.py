from setuptools import setup, find_packages

setup(
    name = 'pypokerengine',
    version = '1.0.2',
    author = 'Marc Ennaji',
    author_email = 'marc.ennaji@gmail.com',
    description = 'Poker engine for poker AI development in Python (forked and modified)',
    license = 'MIT',
    keywords = 'python poker emgine ai',
    url = 'https://github.com/Marcennaji/pypokerengine',
    packages = [pkg for pkg in find_packages() if pkg != "tests"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12",  
    ],
    )

