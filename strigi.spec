Name:          strigi
Summary:       Desktop Search
Group:         Graphical desktop/KDE
Version:       0.7.5
Release:       1
Epoch:         1
License:       LGPLv2+
Url:           http://strigi.sourceforge.net
Source0:       http://www.vandenoever.info/software/strigi/%{name}-%{version}.tar.bz2
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
Obsoletes:     %mklibname cluceneindex 0

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
%doc AUTHORS ChangeLog COPYING
%{_bindir}/*
%{_libdir}/strigi/
%{_datadir}/strigi/
%{_datadir}/dbus-1/services/
%exclude %{_bindir}/strigiclient

#--------------------------------------------------------------------

%package gui
Summary:         Strigi interface
Group:           Graphical desktop/KDE

%description gui
Strigi interface

%files gui
%{_bindir}/strigiclient

#--------------------------------------------------------------------

%define libsearchclient %mklibname searchclient 0

%package -n %{libsearchclient}
Summary:         Strigi library
Group:           System/Libraries
Obsoletes:       %{_lib}strigi0 < 1:0.5.5-1mdv2008.0

%description -n %{libsearchclient}
Strigi library.

%files -n %{libsearchclient}
%{_libdir}/libsearchclient.so.*

#--------------------------------------------------------------------

%define libstreamanalyzer %mklibname streamanalyzer 0

%package -n %{libstreamanalyzer}
Summary:         Strigi library
Group:           System/Libraries
Obsoletes:       %{_lib}strigi0 < 1:0.5.5-1mdv2008.0

%description -n %{libstreamanalyzer}
Strigi library.

%files -n %{libstreamanalyzer}
%{_libdir}/libstreamanalyzer.so.*

#--------------------------------------------------------------------

%define libstreams %mklibname streams 0

%package -n %{libstreams}
Summary:         Strigi library
Group:           System/Libraries
Obsoletes:       %{_lib}strigi0 < 1:0.5.5-1mdv2008.0

%description -n %{libstreams}
Strigi library.

%files -n %{libstreams}
%{_libdir}/libstreams.so.*

#--------------------------------------------------------------------

%define libstrigihtmlgui %mklibname strigihtmlgui 0

%package -n %{libstrigihtmlgui}
Summary:         Strigi library
Group:           System/Libraries
Obsoletes:       %{_lib}strigi0 < 1:0.5.5-1mdv2008.0

%description -n %{libstrigihtmlgui}
Strigi library.

%files -n %{libstrigihtmlgui}
%{_libdir}/libstrigihtmlgui.so.*

#--------------------------------------------------------------------

%define libstrigiqtdbusclient %mklibname strigiqtdbusclient 0

%package -n %{libstrigiqtdbusclient}
Summary:         Strigi library
Group:           System/Libraries
Obsoletes:       %{_lib}strigi0 < 1:0.5.5-1mdv2008.0

%description -n %{libstrigiqtdbusclient}
Strigi library.

%files -n %{libstrigiqtdbusclient}
%{_libdir}/libstrigiqtdbusclient.so.*

#--------------------------------------------------------------------

%package devel
Summary:         Development files for %{name}
Group:           Development/Other
Requires:        %{libstrigihtmlgui}= %{epoch}:%{version}-%{release}
Requires:        %{libstrigiqtdbusclient} = %{epoch}:%{version}-%{release}
Requires:        %{libsearchclient} = %{epoch}:%{version}-%{release}
Requires:        %{libstreamanalyzer} = %{epoch}:%{version}-%{release}
Requires:        %{libstreams} = %{epoch}:%{version}-%{release}
Requires:        %{name} = %{epoch}:%{version}-%{release}
Provides:        lib%{name}-devel = %{epoch}:%{version}-%{release}

%description devel
Development files for %{name}.

%files devel
%{_libdir}/lib*/Lib*.cmake
%{_libdir}/pkgconfig/libstream*.pc
%{_libdir}/*.so
%{_includedir}/strigi/

#--------------------------------------------------------------------
%prep
%setup -q

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build
