Summary:	A VBI library
Name:		zvbi
Version:	0.1.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/zapping/%{name}-%{version}.tar.bz2
URL:		http://zapping.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr

%description
A VBI library

%package devel
Summary:	zvbi heades files
Summary(pl):	Pliki nag³ówkowe do zvbi
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for the support library for the zvbi library.

%package static
Summary:	Static zvbi libraries
Summary(pl):	Biblioteki statyczne do zvbi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static zvbi libraries.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS BUGS ChangeLog NEWS README TODO
%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc [^C]*.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog.gz
%doc doc/html
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
