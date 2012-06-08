%define svn 1070828

Name: strigi
Version: 0.7.7
Release: 1
Epoch: 1
Summary: Desktop Search
License: LGPLv2+
Group: Graphical desktop/KDE
Url: http://strigi.sourceforge.net
Source: http://www.vandenoever.info/software/strigi/%{name}-%{version}.tar.xz
Patch0: strigi-0.7.7-ffmpeg-0.11.patch
Patch1: strigi-0.7.7-missinglink.patch
Patch2: strigi-0.7.7-glibc-2.15.patch
BuildRequires: cmake >= 2.4.5
BuildRequires: qt4-devel >= 4.2.0
BuildRequires: bzip2-devel
BuildRequires: clucene-devel >= 0.9.16
BuildRequires: magic-devel
BuildRequires: openssl-devel
BuildRequires: expat-devel
BuildRequires: attr-devel
BuildRequires: dbus-devel
BuildRequires: cppunit-devel
BuildRequires: libexiv-devel
BuildRequires: boost-devel
BuildRequires: ffmpeg-devel
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
%_bindir/strigiclient

#--------------------------------------------------------------------

%define searchclient_major 0
%define libsearchclient %mklibname searchclient %searchclient_major

%package -n %libsearchclient
Summary: Strigi library
Group: System/Libraries
Obsoletes: %{_lib}strigi0 < 1:0.5.5-1mdv2008.0

%description -n %libsearchclient
Strigi library.

%files -n %libsearchclient
%{_libdir}/libsearchclient.so.%{searchclient_major}*

#--------------------------------------------------------------------

%define libstreamanalyzer %mklibname streamanalyzer 0

%package -n %libstreamanalyzer
Summary: Strigi library
Group: System/Libraries
Obsoletes: %{_lib}strigi0 < 1:0.5.5-1mdv2008.0

%description -n %libstreamanalyzer
Strigi library.

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

%files -n %libstrigiqtdbusclient
%defattr(-,root,root)
%{_libdir}/libstrigiqtdbusclient.so.*

#--------------------------------------------------------------------

%package devel
Summary: Development files for %name
Group:  Development/Other
Requires: %libstrigihtmlgui = %epoch:%version-%release
Requires: %libstrigiqtdbusclient = %epoch:%version-%release
Requires: %libsearchclient = %epoch:%version-%release
Requires: %libstreamanalyzer = %epoch:%version-%release
Requires: %libstreams = %epoch:%version-%release
Requires: strigi = %epoch:%version-%release
Provides: libstrigi-devel = %epoch:%version-%release
Obsoletes: %{_lib}strigi0-devel < 1:0.5.5-1mdv2008.0

%description devel
Development files for %name.

%files devel
%defattr(-,root,root)
%_libdir/*.so
%_includedir/strigi
%_libdir/pkgconfig/*
%_libdir/libsearchclient/LibSearchClientConfig.cmake
%_libdir/libstreamanalyzer/LibStreamAnalyzerConfig.cmake
%_libdir/libstreams/LibStreamsConfig.cmake
%_libdir/libstreams/LibStreamsTargets.cmake
%_libdir/libstreams/LibStreamsTargets-noconfig.cmake

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .ffmpeg11~
%patch1 -p1 -b .missinglink~
%patch2 -p1 -b .glibc215~

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

%clean
rm -fr %buildroot
