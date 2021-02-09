import setuptools
import os
import sys
username = os.getlogin()
os.mkdir('C:\//Users//'+username+'//Downloads//YTDownload')
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="YTDownload",
    version="0.0.1",
    author="TechGeeks",
    author_email="ytdown@tgeeks.cf",
    description="A Open-Source & Free YouTube Downloader",
     long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TechGeeks-Rajdeep/YTDownload",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'pytube',
      ],
    python_requires='>=3.6',
)