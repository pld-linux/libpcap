Summary:	Libpcap provides promiscuous mode access to network interfaces
Summary(pl):	Libpcap pozwala na bezpo¶redni dostêp do interfejsów sieciowych
Name:		libpcap
Version:	0.4a6
Release:	6
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Copyright:	GPL
Source:		ftp://ftp.ee.lbl.gov/%{name}-%{version}+ipv6-1.tar.gz	
Patch0:		%{name}.patch
Patch1:		%{name}-Makefile.patch
Patch2:		%{name}.so_attach_filter.patch
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
%patch2 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{include/pcap/net,lib,man/man3}

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	INCLDEST=%{_includedir}/pcap \

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/*
gzip -9nf README CHANGES 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES}.gz

%{_includedir}/pcap
%{_libdir}/libpcap.a
%{_mandir}/man*/*

%changelog
* Sun Mar 14 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [0.4a6-6]
- removed man group from man pages
- fixed Summary(pl)
- minor changes

* Tue Feb 16 1999 Artur Frysiak <wiget@usa.net>
  [0.4a6-5d]
- initial release for PLD
