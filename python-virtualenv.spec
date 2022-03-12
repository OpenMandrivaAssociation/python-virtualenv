%define module virtualenv
%define __noautoprov '.*setuptools.*'

Summary:	Virtual Python Environment builder
Name:		python-%{module}
Version:	20.13.1
Release:	2
Group:		Development/Python
License:	MIT
Url:		http://pypi.python.org/pypi/virtualenv
Source0:	https://files.pythonhosted.org/packages/9f/85/a968cda343234cd22265ddea1cb7801e25eb1536081099d7016ca7e105c1/virtualenv-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
BuildRequires:	pkgconfig(python)
BuildRequires:	python-pkg-resources
Requires:	pkgconfig(python3)
Requires:	rpm-build

%description
virtualenv is a tool to create isolated Python environments.

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/virtualenv
%{py_puresitedir}/virtualenv*
