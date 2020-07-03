# Import S
import setuptools

# Installation Requirements
with open('requirements.txt') as fp:
    install_requires = fp.read()

# README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

# setup
setuptools.setup(
    name="canviewerPy", # Replace with your own username
    version="0.1.0",
    author="Tim Lucas Sabelmann",
    author_email="tsa@ecap-mobility.com",
    description="Program, that shows can messages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/ecap-mobility/canviewer_py.git",
    packages=setuptools.find_packages(include=['canviewer', 'canviewer.*']),
    package_data={
        'canviewer.gui.glade' : ['window.glade', 'ecap_logo.svg', 'icon.png']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=install_requires,
    py_modules=['main'],
    entry_points={
        'console_scripts' : [
            'canviewerPy = main:main'
        ]
    }
)