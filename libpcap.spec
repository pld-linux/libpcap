Summary:	Libpcap provides promiscuous mode access to network interfaces
Summary(pl):	Libpcap pozwala na bezpo¶redni dostêp do interfejsów sieciowych
Name:		libpcap
Version:	0.4
Release:	19
Serial:		1
License:	GPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.ee.lbl.gov/%{name}-%{version}.tar.Z
Patch0:		ftp://ftp.inr.ac.ru/ip-routing/lbl-tools/libpcap-0.4-ss991029.dif.gz
Patch1:		libpcap-Makefile.patch
Patch2:		libpcap-shared.patch
Patch3:		libpcap-scanner.patch
Patch4:		libpcap-IFF_LOOPBACK.patch
BuildRequires:	flex
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libpcap is a system-independent interface for user-level packet capture.
Libpcap provides a portable framework for low-level network monitoring.
Applications include network statistics collection, security monitoring,
network debugging, etc. Libpcap has system-independent API that is used by
several applications, including tcpdump and arpwatch.

%package devel
Summary:	Header files and develpment documentation for libpcap
Summary(pl):	Pliki nag³ówkowe i dokumetacja do libpcap
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and develpment documentation for libpcap.

%description -l pl devel
Pliki nag³ówkowe i dokumetacja do libpcap.

%package static
Summary:	Static libpcap library
Summary(pl):	Biblioteka statyczna libpcap
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libpcap library.

%description -l pl static
Biblioteka statyczna libpcap.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
aclocal
autoconf
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

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	README CHANGES 

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES}.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man*/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
