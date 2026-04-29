import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dynfc", 
    version="0.0.4a1",
    author="Lucas G. S. França, Dafnis Batalle",
    author_email="lucas.franca@kcl.ac.uk, dafnis.batalle@kcl.ac.uk",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://code-neuro.github.io/dynfc/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
        "scikit-learn",
        "pytest",
    ]
)
