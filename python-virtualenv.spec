%define module	virtualenv
%define name	python-%{module}
%define version	1.4.9

Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
Summary:	Virtual Python Environment builder
Group:		Development/Python
License:	MIT
URL:		http://pypi.python.org/pypi/virtualenv
Source0:	http://pypi.python.org/packages/source/v/virtualenv/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRoot:	%{_tmppath}/%{name}-%{version}
%py_requires -d

%description
virtualenv is a tool to create isolated Python environments.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
%__rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc docs/*.txt
%{_bindir}/*
%{py_sitedir}/*.py
%{py_sitedir}/*.pyc
%{py_sitedir}/*.egg-info
%{py_sitedir}/virtualenv_support/__init__.py
%{py_sitedir}/virtualenv_support/__init__.pyc
%{py_sitedir}/virtualenv_support/distribute-0.6.8.tar.gz
%{py_sitedir}/virtualenv_support/pip-0.7.2.tar.gz
%{py_sitedir}/virtualenv_support/setuptools-0.6c11-py2.6.egg
