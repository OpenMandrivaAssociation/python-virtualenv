%define module	virtualenv
%define name	python-%{module}
%define version	1.4.9

Name:		%{name}
Version:	%{version}
Release:	%mkrel 2
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
PYTHONDONTWRITEBYTECODE= %{__python} setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root,-)
%doc docs/*.txt
