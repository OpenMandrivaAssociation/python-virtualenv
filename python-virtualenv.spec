%define	module	virtualenv
%define __noautoprov '.*setuptools.*'

Summary:	Virtual Python Environment builder
Name:		python-%{module}
Version:	20.1.0
Release:	1
Group:		Development/Python
License:	MIT
Url:		http://pypi.python.org/pypi/virtualenv
Source0:	https://files.pythonhosted.org/packages/06/8c/eb8a0ae49eba5be054ca32b3a1dca432baee1d83c4f125d276c6a5fd2d20/virtualenv-20.1.0.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-pkg-resources
Requires:	pkgconfig(python3)
Requires:	rpm-build

%description
virtualenv is a tool to create isolated Python environments.

%prep
%setup -qn %{module}-%{version}

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/virtualenv
%{py3_puresitedir}/virtualenv*
