#!/usr/bin/env python3

import setuptools  # type: ignore

META = dict(
    name="onweb",
    version="0.6.0",
    description="Check the status of some website.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fmind/onweb",
    author="Médéric Hurier (fmind)",
    author_email="fmind@fmind.me",
    license="LGPL-3.0",
    packages=["onweb"],
    keywords="check status website",
    classifiers=["Development Status :: 4 - Beta"],
    entry_points={"console_scripts": ["onweb=onweb.__main__:main"]},
    python_requires=">=3.7",
    install_requires=["aiohttp"],
)

if __name__ == "__main__":
    setuptools.setup(**META)
