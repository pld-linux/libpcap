# TODO:
# - update pfring support (libpfring.spec, https://github.com/ntop/PF_RING)
# - DAG card support (--with-dag, proprietary, https://support.endace.com/)
# - SS7 card support (--with-septel, proprietary, requires Intel Septel API)
# - Myricom SNF support (--with-snf, proprietary, from https://www.ariacybersecurity.com/support/downloads/)
# - Riverbed TurboCap support (--with-turbocap, proprietary, from https://support.riverbed.com/ ?)
#
# Conditional build:
%bcond_with	dpdk		# DPDK support
%bcond_with	pfring		# http://www.ntop.org/PF_RING.html
%bcond_without	bluetooth	# disable bluetooth support
%bcond_without	ibverbs		# RDMA (InfiniBand) capture support

Summary:	Libpcap provides promiscuous mode access to network interfaces
Summary(es.UTF-8):	libpcap ofrece acceso a modo promiscuo en interfaces de red
Summary(pl.UTF-8):	Libpcap pozwala na bezpośredni dostęp do interfejsów sieciowych
Summary(pt_BR.UTF-8):	A libpcap fornece acesso ao modo promíscuo em interfaces de rede
Summary(ru.UTF-8):	Предоставляет доступ к сетевым интерфейсам в promiscuous-режиме
Summary(uk.UTF-8):	Надає доступ до мережевих інтерфейсів в promiscuous-режимі
Name:		libpcap
Version:	1.10.5
Release:	1
Epoch:		2
License:	BSD
Group:		Libraries
Source0:	https://www.tcpdump.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	0dc69ed81464e7a255715fa685daf134
Patch0:		%{name}-pf_ring.patch
URL:		https://www.tcpdump.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	bison
%{?with_bluetooth:BuildRequires:	bluez-libs-devel}
%{?with_dpdk:BuildRequires:	dpdk-devel >= 18.02.2}
BuildRequires:	dbus-devel
BuildRequires:	flex >= 2.5.31
%{?with_ibverbs:BuildRequires:	libibverbs-devel}
BuildRequires:	libnl-devel >= 3.2
%{?with_pfring:BuildRequires:	libpfring-devel}
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	pkgconfig >= 1:0.17
Obsoletes:	libpcap0 < 1.0
Obsoletes:	libpcap_mmap < 0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with dpdk}
# per_lcore__lcore_id per_lcore__rte_errno non-function symbols from DPDK
%define		skip_post_check_so	libpcap.so.*
%endif

%description
Libpcap is a system-independent interface for user-level packet
capture. Libpcap provides a portable framework for low-level network
monitoring. Applications include network statistics collection,
security monitoring, network debugging, etc. Libpcap has
system-independent API that is used by several applications, including
tcpdump and arpwatch.

%description -l es.UTF-8
libpcap es una interface independiente de sistema para captura de
paquetes en modo usuario. Ofrece un esquema portátil para el control
de la red en bajo nivel. Se utiliza para colecta de estadísticas de
red, Control de seguridad, depuración de la red, etc. Tiene una API
independiente de sistema que se usa por varias aplicaciones, entre
ellas tcpdump y arpwatch.

%description -l pl.UTF-8
libpcap to niezależny od systemu interfejs do przechwytywania pakietów
z poziomu użytkownika.

%description -l pt_BR.UTF-8
A libpcap é uma interface independente de sistema para captura de
pacotes em modo usuário. Fornece um esquema portátil para monitoração
da rede em baixo nível. É utilizada para coleta de estatísticas de
rede, monitoramento de segurança, depuração da rede, etc. Tem uma API
independente de sistema que é usada por várias aplicações, entre elas
tcpdump e arpwatch.

%description -l ru.UTF-8
Libpcap - это системнонезависимый интерфейс для захвата пакетов с
пользовательского уровня и низкоуровневого сетевого мониторинга.
Возможные применения включают сбор сетевой статистики, наблюдение за
безопасностью, отладка сети и т.д. Libpcap имеет системнонезависимый
API, используемый многими приложениями, включая tcpdump и arpwatch.

%description -l uk.UTF-8
Libpcap - це системнонезалежний інтерфейс для захвату пакетів з рівня
користувача та нізкорівневого моніторингу мережі. Можливі використання
включають збір статистики мережі, спостереження за безпекою, відладка
мережі і т.і. Libpcap має системнонезалежний API що використовується
багатьма програмами, такими ял tcpdump, arpwatch та trafshow.

%package devel
Summary:	Header files and develpment documentation for libpcap
Summary(es.UTF-8):	Arquivos de cabeçalho e bibliotecas de desenvolvimento para libpcap
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumetacja do libpcap
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para a libpcap
Summary(ru.UTF-8):	Хедеры и библиотеки програмиста для libpcap
Summary(uk.UTF-8):	Хедери та бібліотеки програміста для libpcap
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libpcap0-devel < 1.0
Obsoletes:	libpcap_mmap-devel < 0.10

%description devel
Libpcap provides a portable framework for low-level network
monitoring. Libpcap can provide network statistics collection,
security monitoring and network debugging. Since almost every system
vendor provides a different interface for packet capture, the libpcap
authors created this system-independent API to ease in porting and to
alleviate the need for several system-dependent packet capture modules
in each application.

Install libpcap if you need to do low-level network traffic monitoring
on your network.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libpcap.

%description devel -l pt_BR.UTF-8
Tcpdump imprime os cabeçalhos dos pacotes em uma interface de rede.
Ele é muito prático para resolver problemas na rede e para operações
de segurança.

%description devel -l ru.UTF-8
Хедеры и библиотеки програмиста, необходимые для программирования с
libpcap.

%description devel -l uk.UTF-8
Хедери та бібліотеки програміста, необхідні для програмування з
libpcap.

%package static
Summary:	Static libpcap library
Summary(es.UTF-8):	Biblioteca estática usada no desenvolvimento de aplicativos com libpcap
Summary(pl.UTF-8):	Biblioteka statyczna libpcap
Summary(pt_BR.UTF-8):	Biblioteca estática de desenvolvimento
Summary(ru.UTF-8):	Статическая библиотека libpcap
Summary(uk.UTF-8):	Статична бібліотека libpcap
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	libpcap_mmap-static < 0.10

%description static
Libpcap provides a portable framework for low-level network
monitoring. Libpcap can provide network statistics collection,
security monitoring and network debugging. Since almost every system
vendor provides a different interface for packet capture, the libpcap
authors created this system-independent API to ease in porting and to
alleviate the need for several system-dependent packet capture modules
in each application.

This package contains the static library used for development.

%description static -l pt_BR.UTF-8
Tcpdump imprime os cabeçalhos dos pacotes em uma interface de rede.
Ele é muito prático para resolver problemas na rede e para operações
de segurança.

%description static -l pl.UTF-8
Biblioteka statyczna libpcap.

%description static -l ru.UTF-8
Статическая библиотека, необходимая для программирования с libpcap.

%description static -l uk.UTF-8
Статична бібліотека, необхідна для програмування з libpcap.

%prep
%setup -q
%{?with_pfring:%patch0 -p0}

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%configure \
	--with-dpdk%{!?with_dpdk:=no} \
	--with-pcap=linux \
	--enable-ipv6 \
	%{__enable bluetooth} \
	--enable-rdma%{!?with_ibverbs:=no}

%{__make} \
	%{?with_pfring:CCOPT="%{rpmcflags} -O0"}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# some packages want pcap-int.h (like kismet)...
# but sanitize somehow:
# don't depend on HAVE_{STRLCPY,SNPRINTF,VSNPRINTF} defines
sed -e '/#ifndef HAVE_STRLCPY/,/#endif/d;/#if !defined(HAVE_SNPRINTF)/,/#endif/d;/#if !defined(HAVE_VSNPRINTF)/,/#endif/d' \
	pcap-int.h > $RPM_BUILD_ROOT%{_includedir}/pcap-int.h

# to show the diff
diff -u pcap-int.h $RPM_BUILD_ROOT%{_includedir}/pcap-int.h || :

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE README.md
%attr(755,root,root) %{_libdir}/libpcap.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpcap.so.1
%{_mandir}/man5/pcap-savefile.5*
%{_mandir}/man7/pcap-*.7*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcap-config
%attr(755,root,root) %{_libdir}/libpcap.so
%{_includedir}/pcap
%{_includedir}/pcap*.h
%{_pkgconfigdir}/libpcap.pc
%{_mandir}/man1/pcap-config.1*
%{_mandir}/man3/pcap*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpcap.a
