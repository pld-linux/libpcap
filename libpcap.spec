Summary:	Libpcap provides promiscuous mode access to network interfaces
Summary(es):	libpcap ofrece acceso a modo promiscuo en interfaces de red
Summary(pl):	Libpcap pozwala na bezpo¶redni dostêp do interfejsów sieciowych
Summary(pt_BR):	A libpcap fornece acesso ao modo promíscuo em interfaces de rede
Name:		libpcap
Version:	0.7.1
Release:	1
Epoch:		2
License:	GPL
Group:		Libraries
Source0:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libpcap0

%description
Libpcap is a system-independent interface for user-level packet
capture. Libpcap provides a portable framework for low-level network
monitoring. Applications include network statistics collection,
security monitoring, network debugging, etc. Libpcap has
system-independent API that is used by several applications, including
tcpdump and arpwatch.

%description -l es
libpcap es una interface independiente de sistema para captura de
paquetes en modo usuario. Ofrece un esquema portátil para el control
de la red en bajo nivel. Se utiliza para colecta de estadísticas de
red, Control de seguridad, depuración de la red, etc. Tiene una API
independiente de sistema que se usa por varias aplicaciones, entre
ellas tcpdump y arpwatch.

%description -l pl
libpcap to niezale¿ny od systemu interfejs do przechwytywania pakietów
z poziomu u¿ytkownika.

%description -l pt_BR
A libpcap é uma interface independente de sistema para captura de
pacotes em modo usuário. Fornece um esquema portátil para monitoração
da rede em baixo nível. É utilizada para coleta de estatísticas de
rede, monitoramento de segurança, depuração da rede, etc. Tem uma API
independente de sistema que é usada por várias aplicações, entre elas
tcpdump e arpwatch.

%package devel
Summary:	Header files and develpment documentation for libpcap
Summary(es):	Arquivos de cabeçalho e bibliotecas de desenvolvimento para libpcap
Summary(pl):	Pliki nag³ówkowe i dokumetacja do libpcap
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para a libpcap
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libpcap0-devel

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

%description devel -l pl
Pliki nag³ówkowe i dokumetacja do libpcap.

%description devel -l pt_BR
Tcpdump imprime os cabeçalhos dos pacotes em uma interface de rede.
Ele é muito prático para resolver problemas na rede e para operações
de segurança.

%package static
Summary:	Static libpcap library
Summary(es):	Biblioteca estática usada no desenvolvimento de aplicativos com libpcap
Summary(pl):	Biblioteka statyczna libpcap
Summary(pt_BR):	Biblioteca estática de desenvolvimento
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Libpcap provides a portable framework for low-level network
monitoring. Libpcap can provide network statistics collection,
security monitoring and network debugging. Since almost every system
vendor provides a different interface for packet capture, the libpcap
authors created this system-independent API to ease in porting and to
alleviate the need for several system-dependent packet capture modules
in each application.

This package contains the static library used for development.

%description static -l pt_BR
Tcpdump imprime os cabeçalhos dos pacotes em uma interface de rede.
Ele é muito prático para resolver problemas na rede e para operações
de segurança.

%description static -l pl
Biblioteka statyczna libpcap.

%prep
%setup  -q -n %{name}-%{version}
%patch0 -p1

%build
autoconf
%configure \
	--with-pcap=linux \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/net \
	$RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man3}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGES CREDITS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES,CREDITS}.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_includedir}/net/*.h
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
