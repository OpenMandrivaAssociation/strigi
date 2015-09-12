Summary:	Desktop Search
Name:		strigi
Version:	0.7.8
Release:	20
Epoch:		1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://strigi.sourceforge.net
Source0:	http://www.vandenoever.info/software/strigi/%{name}-%{version}.tar.bz2
Patch0:		strigi-0.7.7-missinglink.patch
BuildRequires:	cmake
BuildRequires:	attr-devel
BuildRequires:	bzip2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	magic-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(libclucene-core)
BuildRequires:	pkgconfig(openssl)
Obsoletes:	%{mklibname cluceneindex 0} < 0.7.7-2

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
%{_bindir}/*
%dir %{_libdir}/strigi
%{_libdir}/strigi/*
%{_datadir}/strigi/*
%{_datadir}/dbus-1/services/
%exclude %{_bindir}/strigiclient

#--------------------------------------------------------------------

%package gui
Summary:	Strigi interface
Group:		Graphical desktop/KDE

%description gui
Strigi interface

%files gui
%{_bindir}/strigiclient

#--------------------------------------------------------------------

%define searchclient_major 0
%define libsearchclient %mklibname searchclient %{searchclient_major}

%package -n %{libsearchclient}
Summary:	Strigi library
Group:		System/Libraries

%description -n %{libsearchclient}
Strigi library.

%files -n %{libsearchclient}
%{_libdir}/libsearchclient.so.%{searchclient_major}*

#--------------------------------------------------------------------

%define streamanalyzer_major 0
%define libstreamanalyzer %mklibname streamanalyzer %{streamanalyzer_major}

%package -n %{libstreamanalyzer}
Summary:	Strigi library
Group:		System/Libraries

%description -n %{libstreamanalyzer}
Strigi library.

%files -n %{libstreamanalyzer}
%{_libdir}/libstreamanalyzer.so.%{streamanalyzer_major}*

#--------------------------------------------------------------------

%define streams_major 0
%define libstreams %mklibname streams %{streams_major}

%package -n %{libstreams}
Summary:	Strigi library
Group:		System/Libraries

%description -n %{libstreams}
Strigi library.

%files -n %{libstreams}
%{_libdir}/libstreams.so.%{streams_major}*

#--------------------------------------------------------------------

%define strigihtmlgui_major 0
%define libstrigihtmlgui %mklibname strigihtmlgui %{strigihtmlgui_major}

%package -n %{libstrigihtmlgui}
Summary:	Strigi library
Group:		System/Libraries

%description -n %{libstrigihtmlgui}
Strigi library.

%files -n %{libstrigihtmlgui}
%{_libdir}/libstrigihtmlgui.so.%{strigihtmlgui_major}*

#--------------------------------------------------------------------

%define strigiqtdbusclient_major 0
%define libstrigiqtdbusclient %mklibname strigiqtdbusclient %{strigiqtdbusclient_major}

%package -n %{libstrigiqtdbusclient}
Summary:	Strigi library
Group:		System/Libraries

%description -n %{libstrigiqtdbusclient}
Strigi library.

%files -n %{libstrigiqtdbusclient}
%{_libdir}/libstrigiqtdbusclient.so.%{strigiqtdbusclient_major}*

#--------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libstrigihtmlgui} = %{EVRD}
Requires:	%{libstrigiqtdbusclient} = %{EVRD}
Requires:	%{libsearchclient} = %{EVRD}
Requires:	%{libstreamanalyzer} = %{EVRD}
Requires:	%{libstreams} = %{EVRD}
Requires:	strigi = %{EVRD}
Provides:	libstrigi-devel = %{EVRD}

%description devel
Development files for %{name}.

%files devel
%{_libdir}/*.so
%{_includedir}/strigi
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/LibSearchClient/LibSearchClientConfig.cmake
%{_libdir}/cmake/LibStreamAnalyzer/LibStreamAnalyzerConfig.cmake
%{_libdir}/cmake/LibStreamAnalyzer/LibStreamAnalyzerConfigVersion.cmake
%{_libdir}/cmake/LibStreams/LibStreamsConfig.cmake
%{_libdir}/cmake/LibStreams/LibStreamsTargets.cmake
%{_libdir}/cmake/LibStreams/LibStreamsTargets-noconfig.cmake
%{_libdir}/cmake/LibStreams/LibStreamsConfigVersion.cmake
%{_libdir}/cmake/Strigi

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .missinglink~

%build
%cmake_qt4 -DCMAKE_INSTALL_LIBDIR=%{_lib}
%make

%install
%makeinstall_std -C build

