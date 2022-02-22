"""
MIT License

Copyright (c) 2022 Polsulpicien

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from setuptools import setup, find_packages

with open("README.md") as readme:
    long_description = readme.read()
    
setup(
    name='ObserverAPI',
    version='1.1.0',
    license='MIT',
    author="Polsulpicien",
    description="Observer API Wrapper in Python",
    long_description=long_description,
    keywords='ObserverAPI',
    long_description_content_type="text/markdown",
    url="https://github.com/Polsulpicien/ObserverAPI",
    project_urls={
        "Documentation": "https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md",
        "Issue tracker": "https://github.com/Polsulpicien/ObserverAPI/issues",
        "Support": "https://discord.com/invite/xm9QX3Q",
      },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
