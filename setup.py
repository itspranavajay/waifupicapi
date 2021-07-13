from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="waifu-pic-api",
    version="0.4",
    description="Unofficial API Library for waifu-pic For Free",
    py_modules=["waifu-pic-api"],
    package_dir={'': 'src'},
    install_requires=["requests"],
    extras_require={
                      "dev":[
                          "pytest",
                      ],},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MoeZilla/waifu-pic-api",
    author="Moezilla",
    author_email="Pranavajay594@gmail.com"

)
