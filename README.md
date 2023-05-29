<h1 align="center">Software solution to analyse companies' actions</h1>
<h3 align="center">Second Course Work. Analysis Group</h3>
<!-- <hr width="50%" align="center"> -->
<h6 align="center">Made by: Daria Anonymousova, Aleksandra Arkhipova, Ilya Suchkov</h6>
<h6 align="center">Supervised by: Anna Anonymousova</h6>
<br>
<div align="center">

![STATUS](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)
![BUILD](https://img.shields.io/badge/BUILD-PASSING-brightgreen?style=for-the-badge)
![LICENSE](https://img.shields.io/badge/LICENSE-MIT-brightgreen?style=for-the-badge)
</div>


## Table of Contents
* [Abstract](#abstract)
* [...](#)
* [Structure](#struct)
* [References](#references)
  * [Languages & libraries](#lanslibs)
  * [Works & articles](#worksarts)

## Abstract <a name="abstract"></a>

## Structure <a name="struct"></a>

### Folders
- `/data` - all the csv/tsv files
  - `/pickles` - folder to storage created merged DataFrames and access them anywhere
- `/docs` - all the pdf/docx files related to project's defence and submissions in the university
- `/src` - main folder for jupyter files with data analysis

### Files
- `config.py` - consists of csv/tsv files transferred to DataFrames to reduce `.copy()` and similar actions.
Local links such as: `/Users/name/Downloads/major_version_act.csv` are not taken into account! 
- `configlib.py` - includes custom "getter" functions to get DataFrames from `config.py`
- `README.md` - you are reading it right now

## References <a name="references"></a>

### Languages & libraries <a name="lanslibs"></a>

We resorted to using Jupyter Notebook and Python 3.9+ in the course work.
Having the distribution of usage around 90% and 10% respectively.
Using Jupyter Notebook as the main source of our project allowed us
to quickly annotate code and make it more comprehensible.

Used Python's libraries are listed below:

- [pandas](https://pandas.pydata.org/) - is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool
- [matplotlib](https://matplotlib.org/) - is a comprehensive library for creating static, animated, and interactive visualizations
- [beautifulsoap](https://beautiful-soup-4.readthedocs.io/en/latest) - library for pulling data out of HTML and XML files
- [scipy](https://scipy.org/) - provides algorithms for optimization, integration, interpolation, eigenvalue problems, algebraic equations, differential equations, statistics and many other classes of problems.
- [kmodes](https://pypi.org/project/kmodes/) - Python implementations of the k-modes and k-prototypes clustering algorithms. Relies on numpy for a lot of the heavy lifting. K-modes is used for clustering categorical variables.
- [missingno](https://github.com/ResidentMario/missingno) - provides a small toolset of flexible and easy-to-use missing data visualizations and utilities that allows you to get a quick visual summary of the completeness (or lack thereof) of your dataset

### Works & articles <a name="worksarts"></a>

We used many of sources that helped us to make work correct and more professional.