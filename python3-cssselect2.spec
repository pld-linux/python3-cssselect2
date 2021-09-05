#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	CSS selectors for Python ElementTree
Name:		python3-cssselect2
Version:	0.4.1
Release:	1
License:	BSD
Source0:	https://files.pythonhosted.org/packages/source/c/cssselect2/cssselect2-%{version}.tar.gz
# Source0-md5:	6dfd5963c8a5d85f2634d1650b1ddfe1
Patch0:		disable-flake8-isort-pytest.patch
URL:		https://cssselect2.readthedocs.io/
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-pytest-runner
BuildRequires:	python3-setuptools >= 39.2.0
BuildRequires:	python3-tinycss2
BuildRequires:	python3-webencodings
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cssselect2 is a straightforward implementation of CSS3 Selectors for
markup documents (HTML, XML, etc.) that can be read by
ElementTree-like parsers, including cElementTree, lxml, html5lib_,
etc.

%prep
%setup -n cssselect2-%{version}
%patch0 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%if %{with tests}
%{__python3} -m pytest -v
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/cssselect2
%{py3_sitescriptdir}/cssselect2-%{version}-py*.egg-info
