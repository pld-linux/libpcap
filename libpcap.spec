Summary:	Libpcap provides promiscuous mode access to network interfaces
Summary(pl):	Libpcap pozwala na bezpo¶redni dostêp do interfejsów sieciowych
Name:		libpcap
Version:	0.4
Release:	2
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Copyright:	GPL
Serial:		1
Source:		ftp://ftp.ee.lbl.gov/%{name}-%{version}.tar.Z
Patch0:		ftp://ftp.inr.ac.ru/ip-routing/lbl-tools/libpcap-0.4-ss990417.dif.gz
Patch1:		libpcap-Makefile.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Libpcap is a system-independent interface for user-level packet capture.
Libpcap provides a portable framework for low-level network monitoring.
Applications include network statistics collection, security monitoring,
network debugging, etc. Libpcap has system-independent API that is used
by several applications, including tcpdump and arpwatch.
 
%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/net \
	$RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man3}

make install install-man install-incl \
	DESTDIR=$RPM_BUILD_ROOT \
	INCLDEST=%{_includedir} \

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	README CHANGES 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES}.gz

%{_includedir}
%{_libdir}/libpcap.a
%{_mandir}/man*/*

%changelog
