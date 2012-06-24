Summary:	Libpcap provides promiscuous mode access to network interfaces.
Summary(pl):	Libpcap pozwala na bezpo�rednie odwo�anie do interfac�w sieciowych.
Name:		libpcap
Version:	0.4a6
Release:	5d
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Copyright:	GPL
Vendor:		PLD
Source0:	ftp://ftp.ee.lbl.gov/%{name}-%{version}+ipv6-1.tar.gz	
Patch0:		%{name}.patch
Patch1:		%{name}-Makefile.patch
Patch2:		%{name}.so_attach_filter.patch
BuildRoot:   	/tmp/%{name}-%{version}-root

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
./configure \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{include/pcap/net,lib,man/man3}

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	INCLDEST=/usr/include/pcap \

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*
gzip -9nf README CHANGES 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc    README.gz CHANGES.gz

/usr/include/pcap
/usr/lib/libpcap.a

%attr(644,root, man) /usr/man/man3/*

%changelog
* Tue Feb 16 1999 Artur Frysiak <wiget@usa.net>
  [0.4-5d]
- initial release for PLD
