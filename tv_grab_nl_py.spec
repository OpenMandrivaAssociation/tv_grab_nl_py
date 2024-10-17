Summary:	XMLTV compatible grabber for Dutch TV
Name:		tv_grab_nl_py
Version:	r92
Release:	3
License:	GPL
Group:		Video
URL:		https://code.google.com/p/tvgrabnlpy/
Source0:	http://tvgrabnlpy.googlecode.com/files/%{name}-%{version}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
tv_grab_nl_py is a XMLTV-compatible grabber for Dutch television which uses
TVGids.nl as source.

%description -l nl
tv_grab_nl_py is een XMLTV-compatibele grabber voor Nederlandse televisie
die TVGids.nl als bron gebruikt.

%prep

%setup -q -c -T
cp %{SOURCE0} %{name}

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install %{name} %{buildroot}%{_bindir}/tv_grab_nl

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/tv_grab_nl


%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> r92-2mdv2010.0
+ Revision: 445567
- rebuild

* Sat Jan 03 2009 Stefan van der Eijk <stefan@mandriva.org> r92-1mdv2009.1
+ Revision: 323790
- r92

* Sun Oct 12 2008 Stefan van der Eijk <stefan@mandriva.org> r78-1mdv2009.1
+ Revision: 293050
- r78
- r78

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> r73-2mdv2009.0
+ Revision: 269442
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Stefan van der Eijk <stefan@mandriva.org> r73-1mdv2009.0
+ Revision: 202387
- r73

* Mon Mar 17 2008 Stefan van der Eijk <stefan@mandriva.org> r60-2mdv2008.1
+ Revision: 188254
- fix path of script

* Sun Mar 16 2008 Stefan van der Eijk <stefan@mandriva.org> r60-1mdv2008.1
+ Revision: 188181
- import tv_grab_nl_py


