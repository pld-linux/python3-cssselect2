#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	CSS selectors for Python ElementTree
Summary(pl.UTF-8):	Selektory CSS dla pythonowego ElementTree
Name:		python3-cssselect2
Version:	0.8.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/cssselect2/
Source0:	https://files.pythonhosted.org/packages/source/c/cssselect2/cssselect2-%{version}.tar.gz
# Source0-md5:	45b5f89f2934fbcb52490483367c3997
URL:		https://cssselect2.readthedocs.io/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.6
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-tinycss2
BuildRequires:	python3-webencodings
%endif
%if %{with doc}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-sphinx_rtd_theme
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cssselect2 is a straightforward implementation of CSS3 Selectors for
markup documents (HTML, XML, etc.) that can be read by
ElementTree-like parsers, including cElementTree, lxml, html5lib,
etc.

%description -l pl.UTF-8
cssselect2 to bezpośrednia implementacja selektorów CSS3 dla
dokumentów ze znacznikami (HTML, XML itp.), które można czytać
parserami w stylu ElementTree, w tym cElementTree, lxml, html5lib
itp.

%package apidocs
Summary:	API documentation for Python cssselect2 module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona cssselect2
Group:		Documentation

%description apidocs
API documentation for Python cssselect2 module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona cssselect2.

%prep
%setup -q -n cssselect2-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest -v
%endif

%if %{with doc}
cd docs
PYTHONPATH=$(pwd)/.. \
%{__python3} -m sphinx . build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/cssselect2
%{py3_sitescriptdir}/cssselect2-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/*
%endif
