from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="DBRobustClust",
    version="0.0.2",
    author="Fabio Scielzo Ortiz",
    author_email="fabio.scielzoortiz@gmail.com",
    description="For more information, check out the official documentation of `DBRobustClust` at: https://fabioscielzoortiz.github.io/DBRobustClust-docu/intro.html", long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FabioScielzoOrtiz/DBRobustClust-package",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['polars','numpy<=1.26.4', 'PyDistances', 'pandas', 'scikit-learn-extra', 'setuptools', 'pyarrow', 'matplotlib', 'seaborn'],
    python_requires=">=3.7"
)