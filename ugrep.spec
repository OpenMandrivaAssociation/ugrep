Summary:	Barebones version of grep/egrep
Name:		ugrep
Version:	1.7
Release:	9
License:	GPL
Group:		File tools
URL:		https://robur.slu.se/jensl/ugrep/
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


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.7-8mdv2010.0
+ Revision: 434498
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.7-7mdv2009.0
+ Revision: 269446
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 10 2008 Oden Eriksson <oeriksson@mandriva.com> 1.7-6mdv2009.0
+ Revision: 217548
- rebuilt against dietlibc-devel-0.32

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.7-5mdv2008.1
+ Revision: 140924
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.7-5mdv2008.0
+ Revision: 69934
- use %%mkrel


* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 1.7-4mdk
- rebuild

* Sun May 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.7-3mdk
- build release

* Mon Apr 07 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.7-2mdk
- argh!!! fix buildrequires

* Sat Apr 05 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.7-1mdk
- initial cooker contribs

