%define	module	virtualenv
%define __noautoprov '.*setuptools.*'

Summary:	Virtual Python Environment builder
Name:		python-%{module}
Version:	20.0.19
Release:	1
Group:		Development/Python
License:	MIT
Url:		http://pypi.python.org/pypi/virtualenv
Source0:	https://files.pythonhosted.org/packages/93/a4/4f2e546bd7e80a8340fab699be37b65752cb8f925a853365310b381af5f2/virtualenv-20.0.19.tar.gz
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
