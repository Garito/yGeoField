from setuptools import setup, find_packages

def readme():
  with open("README.md") as f:
    return f.read()

setup(
  name = "yGeoField",
  version = "0.0.1",
  description = "Marshmallow field with geo capabilities",
  long_description = readme(),
  long_description_content_type='text/markdown',
  classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Plugins",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Topic :: Database"
  ],
  keywords = "data schema marshmallow geojson",
  url = "https://github.com/Garito/yGeoField",
  author = "Garito",
  author_email = "garito@gmail.com",
  license = "MIT",
  packages = find_packages(),
  python_requires=">=3.6",
  install_requires = [
    "marshmallow",
    "geojson"
  ],
  test_suite = "unittest"
)
