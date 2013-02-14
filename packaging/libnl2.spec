Name:       libnl2
Summary:    Library for netlink sockets
Version:    2.0
Release:    2
Group:      System/Network
License:    GNU LESSER GENERAL PUBLIC LICENSE Version 2.1
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  flex

%description
This is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and various
netlink family specific interfaces.

%package devel
Summary:    Development library and headers for libnl2
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and various
netlink family specific interfaces.
This package contains all files that are needed to build applications using
libnl2.

%prep
%setup -q

./autogen.sh

%build
%configure

#No much jobs, make sure -j1
#make %{?jobs:-j%jobs}
make -j1

%install
%make_install

rm -f %{buildroot}/etc/libnl/pktloc

%files
%defattr(-,root,root,-)
%{_libdir}/libnl*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/libnl*.so
