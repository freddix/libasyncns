Summary:	C library for executing name service queries asynchronously
Name:		libasyncns
Version:	0.8
Release:	4
License:	LGPL v2+
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/libasyncns/%{name}-%{version}.tar.gz
# Source0-md5:	1f553d6ce1ad255bc83b3d8e9384f515
Patch0:		%{name}-link.patch
URL:		http://0pointer.de/lennart/projects/libasyncns/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libasyncns is a C library for Linux/Unix for executing name service
queries asynchronously. It is an asynchronous wrapper around
getaddrinfo(3) and getnameinfo(3) from the libc.

In contrast to GNU's asynchronous name resolving API getaddrinfo_a(),
libasyncns does not make use of UNIX signals for reporting completion
of name queries. Instead, the API exports a standard UNIX file
descriptor which may be integerated cleanly into custom main loops.

%package devel
Summary:	Header files for libasyncns library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libasyncns library.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-lynx \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %ghost %{_libdir}/libasyncns.so.?
%attr(755,root,root) %{_libdir}/libasyncns.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libasyncns.so
%{_includedir}/asyncns.h
%{_pkgconfigdir}/libasyncns.pc

