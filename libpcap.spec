Summary:	Libpcap provides promiscuous mode access to network interfaces
Summary(es):	libpcap ofrece acceso a modo promiscuo en interfaces de red
Summary(pl):	Libpcap pozwala na bezpo╤redni dostЙp do interfejsСw sieciowych
Summary(pt_BR):	A libpcap fornece acesso ao modo promМscuo em interfaces de rede
Summary(ru):	Предоставляет доступ к сетевым интерфейсам в promiscuous-режиме
Summary(uk):	Нада╓ доступ до мережевих ╕нтерфейс╕в в promiscuous-режим╕
Name:		libpcap
Version:	0.8.1
Release:	1
Epoch:		2
License:	GPL
Group:		Libraries
Source0:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	f03f588e1f0ba783004d76f60507cebd
Patch0:		%{name}-shared.patch
Patch1:		%{name}-ac25x.patch
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
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
paquetes en modo usuario. Ofrece un esquema portАtil para el control
de la red en bajo nivel. Se utiliza para colecta de estadМsticas de
red, Control de seguridad, depuraciСn de la red, etc. Tiene una API
independiente de sistema que se usa por varias aplicaciones, entre
ellas tcpdump y arpwatch.

%description -l pl
libpcap to niezale©ny od systemu interfejs do przechwytywania pakietСw
z poziomu u©ytkownika.

%description -l pt_BR
A libpcap И uma interface independente de sistema para captura de
pacotes em modo usuАrio. Fornece um esquema portАtil para monitoraГЦo
da rede em baixo nМvel. и utilizada para coleta de estatМsticas de
rede, monitoramento de seguranГa, depuraГЦo da rede, etc. Tem uma API
independente de sistema que И usada por vАrias aplicaГУes, entre elas
tcpdump e arpwatch.

%description -l ru
Libpcap - это системнонезависимый интерфейс для захвата пакетов с
пользовательского уровня и низкоуровневого сетевого мониторинга.
Возможные применения включают сбор сетевой статистики, наблюдение за
безопасностью, отладка сети и т.д. Libpcap имеет системнонезависимый
API, используемый многими приложениями, включая tcpdump и arpwatch.

%description -l uk
Libpcap - це системнонезалежний ╕нтерфейс для захвату пакет╕в з р╕вня
користувача та н╕зкор╕вневого мон╕торингу мереж╕. Можлив╕ використання
включають зб╕р статистики мереж╕, спостереження за безпекою, в╕дладка
мереж╕ ╕ т.╕. Libpcap ма╓ системнонезалежний API що використову╓ться
багатьма програмами, такими ял tcpdump, arpwatch та trafshow.

%package devel
Summary:	Header files and develpment documentation for libpcap
Summary(es):	Arquivos de cabeГalho e bibliotecas de desenvolvimento para libpcap
Summary(pl):	Pliki nagЁСwkowe i dokumetacja do libpcap
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo para a libpcap
Summary(ru):	Хедеры и библиотеки програмиста для libpcap
Summary(uk):	Хедери та б╕бл╕отеки програм╕ста для libpcap
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
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
Pliki nagЁСwkowe i dokumetacja do libpcap.

%description devel -l pt_BR
Tcpdump imprime os cabeГalhos dos pacotes em uma interface de rede.
Ele И muito prАtico para resolver problemas na rede e para operaГУes
de seguranГa.

%description devel -l ru
Хедеры и библиотеки програмиста, необходимые для программирования с
libpcap.

%description devel -l uk
Хедери та б╕бл╕отеки програм╕ста, необх╕дн╕ для програмування з
libpcap.

%package static
Summary:	Static libpcap library
Summary(es):	Biblioteca estАtica usada no desenvolvimento de aplicativos com libpcap
Summary(pl):	Biblioteka statyczna libpcap
Summary(pt_BR):	Biblioteca estАtica de desenvolvimento
Summary(ru):	Статическая библиотека libpcap
Summary(uk):	Статична б╕бл╕отека libpcap
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

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
Tcpdump imprime os cabeГalhos dos pacotes em uma interface de rede.
Ele И muito prАtico para resolver problemas na rede e para operaГУes
de seguranГa.

%description static -l pl
Biblioteka statyczna libpcap.

%description static -l ru
Статическая библиотека, необходимая для программирования с libpcap.

%description static -l uk
Статична б╕бл╕отека, необх╕дна для програмування з libpcap.

%prep
# -c because of "tar: Removing leading `libpcap-0.8.1/./' from member names"
%setup -q -c
# tar < 1.13.9x compat
[ -f configure ] || cd %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
[ -f configure ] || cd %{name}-%{version}
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%configure \
	--with-pcap=linux \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
if [ ! -f configure ]; then
	mv -f %{name}-%{version}/{README,CHANGES,CREDITS} .
	cd %{name}-%{version}
fi

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README CHANGES CREDITS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
