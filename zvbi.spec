Summary:	Raw VBI, Teletext and Closed Caption decoding library
Summary(pl.UTF-8):	Biblioteka dekodująca VBI
Name:		zvbi
Version:	0.2.44
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/zapping-vbi/zvbi/releases
Source0:	https://github.com/zapping-vbi/zvbi/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ca5e49a80f08ae27517c95d0e07d5039
Patch0:		%{name}-include.patch
Patch1:		%{name}-link.patch
URL:		https://zapping.sourceforge.net/ZVBI/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1:1.16
BuildRequires:	doxygen >= 1.9.8
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libpng-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VBI stands for Vertical Blanking Interval, a gap between the image
data transmitted in an analog video signal. This gap is used to
transmit AM modulated data for various data services like Teletext and
Closed Caption.

The zvbi library provides routines to read from raw VBI sampling
devices, to demodulate raw to sliced VBI data, and to interpret the
data of several popular services. It has been written for the Zapping
TV viewer <http://zapping.sourceforge.net/>.

%description -l pl.UTF-8
VBI jest skrótem od Vertical Blanking Interval, czyli interwał
wygaszania pionowego, który jest odstępem pomiędzy danymi obrazu
transmitowanymi w analogowym sygnale wideo. Ten odstęp jest używany do
transmisji danych rozmaitych usług takich, jak teletekst i Closed
Caption, modulowanych w AM.

Biblioteka zvbi udostępnia funkcje do odczytu z surowych urządzeń
próbkujących VBI, do demodulacji surowych danych VBI i do
interpretacji tych danych dla kilku popularnych usług. Została ona
napisana dla programu TV Zapping <http://zapping.sourceforge.net/>.

%package devel
Summary:	zvbi heades files
Summary(pl.UTF-8):	Pliki nagłówkowe do zvbi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libpng-devel

%description devel
Header files and documentation for the support library for the zvbi
library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do zvbi.

%package static
Summary:	Static zvbi library
Summary(pl.UTF-8):	Biblioteka statyczna zvbi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static zvbi library.

%description static -l pl.UTF-8
Statyczna biblioteka zvbi.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README.md TODO
%attr(755,root,root) %{_bindir}/zvbi-*
%attr(755,root,root) %{_sbindir}/zvbid
%attr(755,root,root) %{_libdir}/libzvbi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzvbi.so.0
%attr(755,root,root) %{_libdir}/libzvbi-chains.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzvbi-chains.so.0
%{_mandir}/man1/zvbi-*.1*
%{_mandir}/man1/zvbid.1*

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_libdir}/libzvbi.so
%attr(755,root,root) %{_libdir}/libzvbi-chains.so
%{_libdir}/libzvbi.la
%{_libdir}/libzvbi-chains.la
%{_includedir}/libzvbi.h
%{_pkgconfigdir}/zvbi-0.2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libzvbi.a
%{_libdir}/libzvbi-chains.a
