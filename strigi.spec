%define svn 895463

Name: strigi
Version: 0.6.1
Release: %mkrel 0.%svn.2
Epoch: 1
Summary: Desktop Search
License: LGPLv2+
Group: Graphical desktop/KDE
Url: http://strigi.sourceforge.net
Source: http://www.vandenoever.info/software/strigi/%{name}-%{version}.%svn.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
BuildRequires: libexiv-devel
Obsoletes: %mklibname cluceneindex 0

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
%doc README
%_bindir/*
%dir %_libdir/strigi
%_libdir/strigi/*
%_datadir/strigi/*
%_datadir/dbus-1/services/
%exclude %_bindir/strigiclient

#--------------------------------------------------------------------

%package gui
Summary: Strigi interface
Group: Graphical desktop/KDE

%description gui
Strigi interface

%files gui
%defattr(-,root,root)
%_bindir/strigiclient

#--------------------------------------------------------------------

%define libsearchclient %mklibname searchclient 0

%package -n %libsearchclient
Summary: Strigi library
Group: System/Libraries
Obsoletes: %{_lib}strigi0 < 1:0.5.5-1mdv2008.0

%description -n %libsearchclient
Strigi library.

%if %mdkversion < 200900
%post -n %libsearchclient -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libsearchclient -p /sbin/ldconfig
%endif

%files -n %libsearchclient
%defattr(-,root,root)
%{_libdir}/libsearchclient.so.*

#--------------------------------------------------------------------

%define libstreamanalyzer %mklibname streamanalyzer 0

%package -n %libstreamanalyzer
Summary: Strigi library
Group: System/Libraries
Obsoletes: %{_lib}strigi0 < 1:0.5.5-1mdv2008.0

%description -n %libstreamanalyzer
Strigi library.

%if %mdkversion < 200900
%post -n %libstreamanalyzer -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libstreamanalyzer -p /sbin/ldconfig
%endif

%files -n %libstreamanalyzer
%defattr(-,root,root)
%{_libdir}/libstreamanalyzer.so.*

#--------------------------------------------------------------------

%define libstreams %mklibname streams 0

%package -n %libstreams
Summary: Strigi library
Group: System/Libraries
Obsoletes: %{_lib}strigi0 < 1:0.5.5-1mdv2008.0

%description -n %libstreams
Strigi library.

%if %mdkversion < 200900
%post -n %libstreams -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libstreams -p /sbin/ldconfig
%endif

%files -n %libstreams
%defattr(-,root,root)
%{_libdir}/libstreams.so.*

#--------------------------------------------------------------------

%define libstrigihtmlgui %mklibname strigihtmlgui 0

%package -n %libstrigihtmlgui
Summary: Strigi library
Group: System/Libraries
Obsoletes: %{_lib}strigi0 < 1:0.5.5-1mdv2008.0

%description -n %libstrigihtmlgui
Strigi library.

%if %mdkversion < 200900
%post -n %libstrigihtmlgui -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libstrigihtmlgui -p /sbin/ldconfig
%endif

%files -n %libstrigihtmlgui
%defattr(-,root,root)
%{_libdir}/libstrigihtmlgui.so.*

#--------------------------------------------------------------------

%define libstrigiqtdbusclient %mklibname strigiqtdbusclient 0

%package -n %libstrigiqtdbusclient
Summary: Strigi library
Group: System/Libraries
Obsoletes: %{_lib}strigi0 < 1:0.5.5-1mdv2008.0

%description -n %libstrigiqtdbusclient
Strigi library.

%if %mdkversion < 200900
%post -n %libstrigiqtdbusclient -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libstrigiqtdbusclient -p /sbin/ldconfig
%endif

%files -n %libstrigiqtdbusclient
%defattr(-,root,root)
%{_libdir}/libstrigiqtdbusclient.so.*

#--------------------------------------------------------------------

%package devel
Requires: %libstrigihtmlgui
Requires: %libstrigiqtdbusclient
Requires: %libsearchclient
Requires: %libstreamanalyzer
Requires: %libstreams
Summary: Development files for %name
Group:  Development/Other
Provides: libstrigi-devel
Obsoletes: %{_lib}strigi0-devel < 1:0.5.5-1mdv2008.0

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
%setup -q -n %name

%build
%cmake_qt4 -DCMAKE_BUILD_TYPE=debugfull
%make

%install
cd build
%makeinstall_std
cd -

%clean
rm -fr %buildroot
