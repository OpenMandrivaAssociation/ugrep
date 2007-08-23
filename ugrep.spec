%define name	ugrep
%define version 1.7
%define release %mkrel 5

Summary:	Barebones version of grep/egrep
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		File tools
URL:		http://robur.slu.se/jensl/ugrep/
Source0:	%{name}.tar.bz2
Patch0:		%{name}-Makefile.patch
BuildRequires:	dietlibc-devel >= 0.20-1mdk
Prefix:		%{_libdir}/embutils
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
%{name} will only do basic regexp string matching.

%prep

%setup -q -n %{name}
%patch0 -p0

# fix version
echo "#define VERSION \"Version: %{version}\"" > version.h

%build

make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{prefix}/bin
install -m755 %{name} %{buildroot}%{prefix}/bin/

# fix softlinks...
ln -snf %{name} %{buildroot}%{prefix}/bin/grep

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{prefix}/bin/%{name}
%{prefix}/bin/grep

