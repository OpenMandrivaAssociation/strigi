%define lib_name_orig %mklibname %name
%define lib_major 0
%define lib_name %lib_name_orig%lib_major
%define versiondate 20070502

# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/
%define _mandir %_prefix/man/

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}


Name:          strigi
Version:       0.5.1
Release:       %mkrel 1
Epoch:	       1
Summary:       Desktop Search
License:       GPL
Group:         Graphical desktop/KDE
Url:           http://www.vandenoever.info/software/strigi/
Source:        %name-%version.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-buildroot
BuildRequires: cmake >= 2.4.5
BuildRequires: qt4-devel >= 4.2.0
BuildRequires: bzip2-devel
BuildRequires: clucene-devel >= 0.9.16
BuildRequires: libmagic-devel
BuildRequires: openssl-devel
BuildRequires: expat-devel
BuildRequires: attr-devel
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
%{_bindir}/deepfind
%{_bindir}/deepgrep
%{_bindir}/strigidaemon
%{_bindir}/xmlindexer
%{_bindir}/luceneindexer
%_bindir/strigiclient
%_bindir/strigicmd
#%_datadir/apps/strigi/fieldproperties/*.fieldproperties

#--------------------------------------------------------------------

%package -n %lib_name
Summary:        Headers files for %name
Group:          Development/Other
Provides:       libstrigi

%description -n %lib_name

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %lib_name
%defattr(-,root,root)
%{_libdir}/libsearchclient.so.*
%_libdir/libstreamanalyzer.so.*
%{_libdir}/libstreams.so.*
%{_libdir}/libstrigihtmlgui.so.*
%_libdir/libcluceneindex.so.*
%_libdir/libstrigiqtdbusclient.so.*
%_libdir/strigi/strigila_deb.so
%_libdir/strigi/strigila_xpm.so
%_libdir/strigi/strigita_au.so
%_libdir/strigi/strigita_pcx.so
%_libdir/strigi/strigita_xbm.so
%_libdir/strigi/strigila_cpp.so

#--------------------------------------------------------------------

%package  -n %lib_name-devel
Requires:       %{lib_name} = %epoch:%{version}
Summary:        Development files for %name
Group:          Development/Other
Provides:       strigi-devel

%description -n %lib_name-devel

%files  -n %lib_name-devel
%defattr(-,root,root)
%_libdir/libstreamanalyzer.so
%{_libdir}/libsearchclient.so
%{_libdir}/libstreams.so
%{_libdir}/libstrigihtmlgui.so
%_libdir/libcluceneindex.so
%_libdir/libstrigiqtdbusclient.so

%dir %_includedir/strigi/
%_includedir/strigi/*.h
%{_libdir}/libstrigihtmlgui.so
%dir %_includedir/strigi/qtdbus/
%_includedir/strigi/qtdbus/*.h
%_libdir/pkgconfig/libstreamanalyzer.pc
%_libdir/pkgconfig/libstreams.pc


#--------------------------------------------------------------------

%prep
%setup -q  -n%name-%version


%build
cd $RPM_BUILD_DIR/%name-%version
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make

%install
cd $RPM_BUILD_DIR/%name-%version/build
make DESTDIR=%buildroot install

%clean
rm -fr %buildroot
