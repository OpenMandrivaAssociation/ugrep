Summary:	Barebones version of grep/egrep
Name:		ugrep
Version:	1.7
Release:	%mkrel 8
License:	GPL
Group:		File tools
URL:		http://robur.slu.se/jensl/ugrep/
Source0:	%{name}.tar.bz2
Patch0:		%{name}-Makefile.patch
BuildRequires:	dietlibc-devel >= 0.32
Prefix:		%{_libdir}/embutils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf %{buildroot}

install -d %{buildroot}%{prefix}/bin
install -m755 %{name} %{buildroot}%{prefix}/bin/

# fix softlinks...
ln -snf %{name} %{buildroot}%{prefix}/bin/grep

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{prefix}/bin/%{name}
%{prefix}/bin/grep
