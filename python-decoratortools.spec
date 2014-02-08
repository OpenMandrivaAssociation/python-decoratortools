%define oname DecoratorTools

Name:           python-decoratortools
Version:        1.8
Release:        3
Summary:        Use class and function decorators -- even in Python 2.3
Group:          Development/Python
License:        Python or ZPLv2.1
URL:            http://cheeseshop.python.org/pypi/DecoratorTools
Source0:        http://cheeseshop.python.org/packages/source/D/DecoratorTools/%{oname}-%{version}.zip
BuildArch:      noarch

BuildRequires:  python-devel 
BuildRequires:  python-setuptools

%description
Want to use decorators, but still need to support Python 2.3? Wish you could
have class decorators, decorate arbitrary assignments, or match decorated
function signatures to their original functions?
Then you need "DecoratorTools".

%prep
%setup -q -n %{oname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}
 
%files
%defattr(-,root,root,-)
%doc README.txt
%{py_puresitedir}/*



%changelog
* Thu Nov 25 2010 Funda Wang <fwang@mandriva.org> 1.8-1mdv2011.0
+ Revision: 600932
- new version 1.8

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.7-3mdv2011.0
+ Revision: 442093
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.7-2mdv2009.1
+ Revision: 323563
- rebuild

* Thu Aug 14 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1.7-1mdv2009.0
+ Revision: 271700
- new version 1.7

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.6-4mdv2009.0
+ Revision: 259553
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.6-3mdv2009.0
+ Revision: 247402
- rebuild

* Wed Feb 20 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1.6-1mdv2008.1
+ Revision: 173277
- fix files
- fix group
- import python-decoratortools


