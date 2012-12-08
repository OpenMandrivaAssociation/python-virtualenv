%define module	virtualenv
%define name	python-%{module}
%define version	1.7.2

Name:		%{name}
Version:	%{version}
Release:	1
Summary:	Virtual Python Environment builder
Group:		Development/Python
License:	MIT
URL:		http://pypi.python.org/pypi/virtualenv
Source0:	http://pypi.python.org/packages/source/v/virtualenv/%{module}-%{version}.tar.gz
Source1:	virtualenv
Patch0:		multiarch-1.7.2.patch
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRoot:	%{_tmppath}/%{name}-%{version}
Requires:	python-devel

%description
virtualenv is a tool to create isolated Python environments.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0 -b .multiarch

%build
PYTHONDONTWRITEBYTECODE= %{__python} setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot}
%__mv %{buildroot}%{_bindir}/virtualenv %{buildroot}%{_bindir}/virtualenv.sh 
%__install -m 755 %SOURCE1 %{buildroot}%{_bindir}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc docs/*.txt
%_bindir/virtualenv*
%py_sitedir/virtualenv*


%changelog
* Fri Jun 22 2012 Lev Givon <lev@mandriva.org> 1.7.2-1
+ Revision: 806716
- Update to 1.7.2.

* Sun Feb 19 2012 Lev Givon <lev@mandriva.org> 1.7.1.2-1
+ Revision: 777345
- Update to 1.7.1.2.

* Fri Feb 17 2012 Lev Givon <lev@mandriva.org> 1.7.1-1
+ Revision: 776139
- Update to 1.7.1.

* Wed Nov 30 2011 Lev Givon <lev@mandriva.org> 1.7-1
+ Revision: 735727
- Update to 1.7.

* Thu Jul 28 2011 Lev Givon <lev@mandriva.org> 1.6.4-2
+ Revision: 692103
- Need python-devel to run virtualenv.

* Thu Jul 21 2011 Lev Givon <lev@mandriva.org> 1.6.4-1
+ Revision: 690872
- Update to 1.6.4.

* Sun Jul 17 2011 Lev Givon <lev@mandriva.org> 1.6.3-1
+ Revision: 690164
- Update to 1.6.3.

* Sun May 01 2011 Lev Givon <lev@mandriva.org> 1.6.1-1
+ Revision: 661110
- Update to 1.6.1.

* Fri Apr 22 2011 Lev Givon <lev@mandriva.org> 1.6-1
+ Revision: 656688
- Update to 1.6.
- Bump release to rebuild.

* Sun Mar 13 2011 Lev Givon <lev@mandriva.org> 1.5.2-4
+ Revision: 644104
- Update to 1.5.2.

* Sun Jan 23 2011 Lev Givon <lev@mandriva.org> 1.5.1-4
+ Revision: 632441
- Manually unset PYTHONDONTWRITEBYTECODE in /usr/bin/virtualenv (#42808).

* Thu Nov 04 2010 Funda Wang <fwang@mandriva.org> 1.5.1-2mdv2011.0
+ Revision: 593098
- rebuild for py 2.7

* Mon Sep 20 2010 Lev Givon <lev@mandriva.org> 1.5.1-1mdv2011.0
+ Revision: 579917
- Update to 1.5.1.

* Tue Sep 14 2010 Lev Givon <lev@mandriva.org> 1.5-4mdv2011.0
+ Revision: 578355
- Rebuild with updated tarball to address virtualenv issue 62.

* Tue Sep 14 2010 Lev Givon <lev@mandriva.org> 1.5-3mdv2011.0
+ Revision: 578348
- Update to 1.5.

* Mon Sep 06 2010 Lev Givon <lev@mandriva.org> 1.4.9-3mdv2011.0
+ Revision: 576208
- Restore multiarch patch silently removed in r515961.

* Tue Jul 13 2010 Lev Givon <lev@mandriva.org> 1.4.9-2mdv2011.0
+ Revision: 551389
- Fix file list.
- Update to 1.4.9.

  + Sandro Cazzaniga <kharec@mandriva.org>
    - update to 1.4.5

* Thu Apr 23 2009 Lev Givon <lev@mandriva.org> 1.3.3-1mdv2010.0
+ Revision: 368776
- Update to 1.3.3.
  Patch to not choke on multiarch.

* Tue Dec 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.2-1mdv2009.1
+ Revision: 321436
- new version
- don't use auto-generated file list
- don't change upstream compression

* Tue Nov 04 2008 Lev Givon <lev@mandriva.org> 1.3-1mdv2009.1
+ Revision: 299869
- Update to 1.3.

* Fri Jun 13 2008 Jérôme Soyer <saispo@mandriva.org> 1.1-1mdv2009.0
+ Revision: 218912
- Remove bindir
- import python-virtualenv

