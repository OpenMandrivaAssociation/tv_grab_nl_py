Summary:	XMLTV compatible grabber for Dutch TV
Name:		tv_grab_nl_py
Version:	r73
Release:	%mkrel 1
License:	GPL
Group:		Video
URL:		http://code.google.com/p/tvgrabnlpy/
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
