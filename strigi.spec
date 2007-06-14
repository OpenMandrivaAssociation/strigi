%define versiondate 20070614

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%if %{unstable}
%define dont_strip 1
%endif

Name: strigi
Version: 0.5.1
Release: %mkrel 3 
Epoch: 1
Summary: Desktop Search
License: GPL
Group: Graphical desktop/KDE
Url: http://www.vandenoever.info/software/strigi/
Source: %name-%version.%{versiondate}.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-buildroot
BuildRequires: cmake >= 2.4.5
BuildRequires: qt4-devel >= 4.2.0
BuildRequires: bzip2-devel
BuildRequires: clucene-devel >= 0.9.16
BuildRequires: libmagic-devel
BuildRequires: openssl-devel
BuildRequires: expat-devel
BuildRequires: attr-devel
BuildRequires: dbus-devel
BuildRequires: cppunit-devel

%description
Here are the main features of Strigi:

    * very fast crawling
    * very small memory footprint
    * no hammering of the system
    * pluggable backend, currently clucene and hyperestraier, 
	sqlite3 and xapian are in the works
    * communication between daemon and search program over an 
	abstract interface, this is currently a simple socket 
	but implementation of dbus is a possibility. There's a 
	small perl program in the code as an example of how to 
	query. This is so easy that any KDE app could implement this.
    * simple interface for implementing plugins for extracting 
	information. we'll try to reuse the kat plugins, although 
	native plugins will have a large speed advantage
    * calculation of sha1 for every file crawled (allows fast finding
	 of duplicates)


%files
%defattr(-,root,root)
%_bindir/*
%dir %_libdir/strigi
%_libdir/strigi/*
%_datadir/strigi/*
%_datadir/dbus-1/services/

#--------------------------------------------------------------------

%define libsearchclient %mklibname searchclient 0

%package -n %libsearchclient
Summary: Strigi library
Group: System/Libraries
Obsoletes: %{_lib}strigi0

%description -n %libsearchclient
Strigi library.

%post -n %libsearchclient -p /sbin/ldconfig
%postun -n %libsearchclient -p /sbin/ldconfig

%files -n %libsearchclient
%defattr(-,root,root)
%{_libdir}/libsearchclient.so.*

#--------------------------------------------------------------------

%define libstreamanalyzer %mklibname streamanalyzer 0

%package -n %libstreamanalyzer
Summary: Strigi library
Group: System/Libraries
Obsoletes: %{_lib}strigi0

%description -n %libstreamanalyzer
Strigi library.

%post -n %libstreamanalyzer -p /sbin/ldconfig
%postun -n %libstreamanalyzer -p /sbin/ldconfig

%files -n %libstreamanalyzer
%defattr(-,root,root)
%{_libdir}/libstreamanalyzer.so.*

#--------------------------------------------------------------------

%define libstreams %mklibname streams 0

%package -n %libstreams
Summary: Strigi library
Group: System/Libraries
Obsoletes: %{_lib}strigi0

%description -n %libstreams
Strigi library.

%post -n %libstreams -p /sbin/ldconfig
%postun -n %libstreams -p /sbin/ldconfig

%files -n %libstreams
%defattr(-,root,root)
%{_libdir}/libstreams.so.*

#--------------------------------------------------------------------

%define libstrigihtmlgui %mklibname strigihtmlgui 0

%package -n %libstrigihtmlgui
Summary: Strigi library
Group: System/Libraries
Obsoletes: %{_lib}strigi0

%description -n %libstrigihtmlgui
Strigi library.

%post -n %libstrigihtmlgui -p /sbin/ldconfig
%postun -n %libstrigihtmlgui -p /sbin/ldconfig

%files -n %libstrigihtmlgui
%defattr(-,root,root)
%{_libdir}/libstrigihtmlgui.so.*

#--------------------------------------------------------------------

%define libcluceneindex %mklibname cluceneindex 0

%package -n %libcluceneindex
Summary: Strigi library
Group: System/Libraries
Obsoletes: %{_lib}strigi0

%description -n %libcluceneindex
Strigi library.

%post -n %libcluceneindex -p /sbin/ldconfig
%postun -n %libcluceneindex -p /sbin/ldconfig

%files -n %libcluceneindex
%defattr(-,root,root)
%{_libdir}/libcluceneindex.so.*

#--------------------------------------------------------------------

%define libstrigiqtdbusclient %mklibname strigiqtdbusclient 0

%package -n %libstrigiqtdbusclient
Summary: Strigi library
Group: System/Libraries
Obsoletes: %{_lib}strigi0

%description -n %libstrigiqtdbusclient
Strigi library.

%post -n %libstrigiqtdbusclient -p /sbin/ldconfig
%postun -n %libstrigiqtdbusclient -p /sbin/ldconfig

%files -n %libstrigiqtdbusclient
%defattr(-,root,root)
%{_libdir}/libstrigiqtdbusclient.so.*

#--------------------------------------------------------------------

%package devel
Requires: %libstrigihtmlgui
Requires: %libstrigiqtdbusclient
Requires: %libsearchclient
Requires: %libstreamanalyzer
Requires: %libcluceneindex
Requires: %libstreams
Summary: Development files for %name
Group:  Development/Other
Provides: libstrigi-devel
Obsoletes: %{_lib}strigi0-devel

%description devel
Development files for %name.

%files devel
%defattr(-,root,root)
%_libdir/*.so
%dir %_includedir/strigi
%_includedir/strigi/*
%_libdir/pkgconfig/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
export QTDIR=%qt4dir
export PATH=$QTDIR/bin:$PATH

mkdir build && cd build

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %unstable
      -DCMAKE_BUILD_TYPE=debugfull \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make

%install
cd build && make DESTDIR=%buildroot install

%clean
rm -fr %buildroot


