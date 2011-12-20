Summary:	Raw VBI, Teletext and Closed Caption decoding library
Summary(pl.UTF-8):	Biblioteka dekodująca VBI
Name:		zvbi
Version:	0.2.33
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/zapping/%{name}-%{version}.tar.bz2
# Source0-md5:	1741a6045c3eedfb611d645f2da69ac8
Patch0:		%{name}-include.patch
Patch1:		%{name}-includes.patch
Patch2:		%{name}-link.patch
URL:		http://zapping.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	doxygen
BuildRequires:	gettext-devel >= 0.16.1
BuildRequires:	libpng-devel
BuildRequires:	libtool
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
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
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
%doc AUTHORS ChangeLog BUGS NEWS README TODO
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
