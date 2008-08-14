%define oname DecoratorTools

Name:           python-decoratortools
Version:        1.7
Release:        %mkrel 1
Summary:        Use class and function decorators -- even in Python 2.3
Group:          Development/Python
License:        Python or ZPLv2.1
URL:            http://cheeseshop.python.org/pypi/DecoratorTools
Source0:        http://cheeseshop.python.org/packages/source/D/DecoratorTools/%{oname}-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

BuildRequires:  python-devel 
BuildRequires:  python-setuptools

%description
Want to use decorators, but still need to support Python 2.3? Wish you could
have class decorators, decorate arbitrary assignments, or match decorated
function signatures to their original functions? Then you need "DecoratorTools".

%prep
%setup -q -n %{oname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt
%{py_puresitedir}/*

