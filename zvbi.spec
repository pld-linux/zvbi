Summary:	Raw VBI, Teletext and Closed Caption decoding library
Summary(pl):	Biblioteka dekoduj±ca VBI
Name:		zvbi
Version:	0.2.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://unc.dl.sourceforge.net/sourceforge/zapping/%{name}-%{version}.tar.bz2
URL:		http://zapping.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libunicode-devel
BuildRequires:	doxygen
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

%description -l pl
VBI jest skrótem od Vertical Blanking Interval, czyli interwa³
wygaszania pionowego, który jest odstêpem pomiêdzy danymi obrazu
transmitowanymi w analogowym sygnale wideo. Ten odstêp jest u¿ywany do
transmisji danych rozmaitych us³ug takich, jak teletekst i Closed
Caption, modulowanych w AM.

Biblioteka zvbi udostêpnia funkcje do odczytu z surowych urz±dzeñ
próbkuj±cych VBI, do demodulacji surowych danych VBI i do
interpretacji tych danych dla kilku popularnych us³ug. Zosta³a ona
napisana dla programu TV Zapping <http://zapping.sourceforge.net/>.

%package devel
Summary:	zvbi heades files
Summary(pl):	Pliki nag³ówkowe do zvbi
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libunicode-devel

%description devel
Header files and documentation for the support library for the zvbi
library.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do zvbi.

%package static
Summary:	Static zvbi library
Summary(pl):	Biblioteka statyczna do zvbi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static zvbi library.

%description static -l pl
Statyczna biblioteka zvbi.

%prep
%setup -q

#Throw away AM_ACLOCAL_INCLUDE with breaks aclocal regeneration
sed -e 's/AM_ACLOCAL_INCLUDE(m4)//g' configure.in > configure.in.new;
mv configure.in.new configure.in  

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog doc/html
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
