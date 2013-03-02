%define svn 1070828

Name:		strigi
Version:	0.7.8
Release:	4
Epoch:		1
Summary:	Desktop Search
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://strigi.sourceforge.net
Source:		http://www.vandenoever.info/software/strigi/%{name}-%{version}.tar.bz2
Patch1:		strigi-0.7.7-missinglink.patch
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	bzip2-devel
BuildRequires:	clucene-devel
BuildRequires:	magic-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	expat-devel
BuildRequires:	attr-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	ffmpeg-devel
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

%define libstreamanalyzer %mklibname streamanalyzer 0

%package -n %{libstreamanalyzer}
Summary:	Strigi library
Group:		System/Libraries

%description -n %{libstreamanalyzer}
Strigi library.

%files -n %{libstreamanalyzer}
%{_libdir}/libstreamanalyzer.so.*

#--------------------------------------------------------------------

%define libstreams %mklibname streams 0

%package -n %{libstreams}
Summary:	Strigi library
Group:		System/Libraries

%description -n %{libstreams}
Strigi library.

%files -n %{libstreams}
%{_libdir}/libstreams.so.*

#--------------------------------------------------------------------

%define libstrigihtmlgui %mklibname strigihtmlgui 0

%package -n %{libstrigihtmlgui}
Summary:	Strigi library
Group:		System/Libraries

%description -n %{libstrigihtmlgui}
Strigi library.

%files -n %{libstrigihtmlgui}
%{_libdir}/libstrigihtmlgui.so.*

#--------------------------------------------------------------------

%define libstrigiqtdbusclient %mklibname strigiqtdbusclient 0

%package -n %{libstrigiqtdbusclient}
Summary:	Strigi library
Group:		System/Libraries

%description -n %{libstrigiqtdbusclient}
Strigi library.

%files -n %{libstrigiqtdbusclient}
%{_libdir}/libstrigiqtdbusclient.so.*

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
%{_libdir}/cmake/LibStreams/LibStreamsConfig.cmake
%{_libdir}/cmake/LibStreams/LibStreamsTargets.cmake
%{_libdir}/cmake/Libstreams/LibStreamsTargets-noconfig.cmake

#--------------------------------------------------------------------

%prep
%setup -q
%patch1 -p1 -b .missinglink~

%build
%cmake_qt4 -DCMAKE_INSTALL_LIBDIR=%{_lib}
%make

%install
%makeinstall_std -C build

%changelog
* Fri Jun 08 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:0.7.7-1
+ Revision: 803474
- Update to 0.7.7
- Port to ffmpeg 0.11.x
- Port to glibc 2.15.x

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.7.6-3
+ Revision: 702764
- bump release
- sync with what's in 2011 (what the bloody hell?)

* Fri Sep 23 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.7.5-1
+ Revision: 701010
- Remove old obsoletes
- Clean spec file
- Clean spec file
- Rebuild against new libpng

  + Zé <ze@mandriva.org>
    - version 0.7.5
    - arrange spec
    - remove useless specs
    - clean section is done by default
    - BR is done by default

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.7.2-4
+ Revision: 670204
- mass rebuild

* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 1:0.7.2-3mdv2011.0
+ Revision: 604426
- rebuild for new exiv2

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 1:0.7.2-2mdv2011.0
+ Revision: 565547
- rebuild for new exiv2

* Thu Feb 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.7.2-1mdv2010.1
+ Revision: 500667
- New version: 0.7.2

* Wed Jan 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.7.0-1.1070828.2mdv2010.1
+ Revision: 487007
- New snapshot

* Thu Dec 31 2009 Funda Wang <fwang@mandriva.org> 1:0.7.0-1.1045403.2mdv2010.1
+ Revision: 484288
- rebuild for new exiv

* Fri Nov 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.7.0-1.1045403.1mdv2010.1
+ Revision: 460536
- Update to a new svn snapshot

* Tue Sep 15 2009 Helio Chissini de Castro <helio@mandriva.com> 1:0.7-0.RC1.3mdv2010.0
+ Revision: 443175
- Invalid requires break strigi-devel instalation

* Tue Sep 15 2009 Helio Chissini de Castro <helio@mandriva.com> 1:0.7-0.RC1.2mdv2010.0
+ Revision: 443116
- Devel package should requires main strigi analysers

* Thu Jul 23 2009 Helio Chissini de Castro <helio@mandriva.com> 1:0.7-0.RC1.1mdv2010.0
+ Revision: 398838
- New upstream version 0.7 RC1

* Thu May 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.95-0.974206.1mdv2010.0
+ Revision: 380614
- New snapshot

* Thu May 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.95-0.970837.1mdv2010.0
+ Revision: 378144
- New snapshot

* Thu May 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.95-0.964927.1mdv2010.0
+ Revision: 372989
- New snapshot

* Thu Apr 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.5-0.958999.1mdv2010.0
+ Revision: 369183
- New snapshot ( needed for kde 4.2.70)
  Remove merged patch

* Sun Apr 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.4-2mdv2009.1
+ Revision: 364241
- Strigi now allows path that start with protocol:/* like file:/// or remote:/

* Mon Feb 02 2009 Funda Wang <fwang@mandriva.org> 1:0.6.4-1mdv2009.1
+ Revision: 336333
- New version 0.6.4

* Wed Jan 14 2009 Funda Wang <fwang@mandriva.org> 1:0.6.3-1mdv2009.1
+ Revision: 329481
- New version 0.6.3

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 1:0.6.1-0.895463.2mdv2009.1
+ Revision: 324533
- rebuild for new exiv

* Wed Dec 10 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.1-0.895463.1mdv2009.1
+ Revision: 312591
- Update to new snapshot

* Sat Oct 18 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.6.0-0.872738.1mdv2009.1
+ Revision: 294820
- New snapshot
  Remove merged patches

* Mon Aug 04 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.5.11-2mdv2009.0
+ Revision: 262845
- Update release field
- Add back patch that install indexpluginloader.h header file needed by next kdebase4-runtime for nepomuk related stuffs

* Sun Aug 03 2008 Frederik Himpe <fhimpe@mandriva.org> 1:0.5.11-1mdv2009.0
+ Revision: 262223
- Update to new upstream version 0.5.11 (should fix Dolphin crash when
  hovering over some video files: http://bugs.kde.org/show_bug.cgi?id=164296)
- Use more up to date source URL
- Remove 0.5.11 patch which was not even applied
- Update license

* Fri Aug 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.5.10-2mdv2009.0
+ Revision: 260071
- Install header indexpluginloader.h needed by kdebase4-runtime

* Tue Jul 29 2008 Helio Chissini de Castro <helio@mandriva.com> 1:0.5.10-1mdv2009.0
+ Revision: 252952
- Using upstream offical tarball for 0.5.10

* Mon Jul 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.5.10-0.832233.1mdv2009.0
+ Revision: 234485
- New snapshot

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu May 15 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.5.9-0.808174.1mdv2009.0
+ Revision: 207918
- Fix tarball
- Update to 0.5.9 svn ( needed by kdelibs 4.0.74)

* Mon Jan 07 2008 Helio Chissini de Castro <helio@mandriva.com> 1:0.5.7-1.758303.1mdv2008.1
+ Revision: 146273
- Update to current devel status of strigi
- Removed unused patch
- Update for revision 745576
- Disable gcc 4.3 patch ( already integrated )

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.5.7-1.732630.2mdv2008.1
+ Revision: 111913
- Rebuild because of new libexiv2

* Mon Nov 05 2007 Funda Wang <fwang@mandriva.org> 1:0.5.7-1.732630.1mdv2008.1
+ Revision: 106020
- add suse patch to have it build
- Update to svn snapshot because tarball does not build :(
- fix file list
- New version 0.5.7

* Mon Oct 15 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.5.6-0.725465.1mdv2008.1
+ Revision: 98608
- New snapshot release for 0.5.6

* Wed Sep 19 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:0.5.5-2mdv2008.0
+ Revision: 91162
- Make all Obsoletes entries versioned

* Thu Aug 09 2007 Funda Wang <fwang@mandriva.org> 1:0.5.5-1mdv2008.0
+ Revision: 60733
- New version 0.5.5

* Fri Jul 27 2007 Helio Chissini de Castro <helio@mandriva.com> 1:0.5.4-0.693047.1mdv2008.0
+ Revision: 56191
- Update for strigi 0.5.4 revision 693047

* Fri Jul 20 2007 Helio Chissini de Castro <helio@mandriva.com> 1:0.5.3-0.689230.1mdv2008.0
+ Revision: 54001
- Update to 0.5.3 revision 689230

* Wed Jul 04 2007 Helio Chissini de Castro <helio@mandriva.com> 1:0.5.2-0.682982.1mdv2008.0
+ Revision: 48186
- Update for recent 0.5.2 svn

* Mon Jun 25 2007 Helio Chissini de Castro <helio@mandriva.com> 1:0.5.1-4mdv2008.0
+ Revision: 44095
- Fix group
- Update for recent svn snapshot
- Update for recent svn snapshot
- Split strigi interface from main package
- Update for latest svn

* Thu Jun 14 2007 Helio Chissini de Castro <helio@mandriva.com> 1:0.5.1-3mdv2008.0
+ Revision: 39571
- Update for latest svn strigi from 20070614
- Added recent svn strigi
- Changed package layout. No more the one lib rule then all. All libraries will be properly
  separated. Lets cleanup the mess on kde 4 packages when we still have time

  + Laurent Montel <lmontel@mandriva.org>
    - Fix spec file
    - Readd "versiondate" ...

* Fri May 04 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.5.1-1mdv2008.0
+ Revision: 22312
- New version 0.5.1
- Fix version ( we are in 0.5.0 now )

* Wed May 02 2007 Laurent Montel <lmontel@mandriva.org> 1:0.3.11-0.20070502.11mdv2008.0
+ Revision: 20421
- New version

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix description

* Tue Apr 17 2007 Laurent Montel <lmontel@mandriva.org> 1:0.3.11-0.20070417.10mdv2008.0
+ Revision: 13739
- New version (need by new snapshot)

* Tue Apr 17 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.3.11-0.20070406.9mdv2007.1
+ Revision: 13529
- Rebuild


* Sat Apr 07 2007 Laurent Montel <lmontel@mandriva.com> 0.3.11-0.20070406.8mdv2007.1
+ Revision: 150887
- New version

* Wed Mar 28 2007 Laurent Montel <lmontel@mandriva.com> 1:0.3.11-0.20070327.7mdv2007.1
+ Revision: 149079
- New version requires by new kdelibs
  Fix buildrequires

* Sun Mar 11 2007 Laurent Montel <lmontel@mandriva.com> 1:0.3.11-0.20070311.6mdv2007.1
+ Revision: 141256
- New version for new kdelibs update

* Wed Mar 07 2007 Laurent Montel <lmontel@mandriva.com> 1:0.3.11-0.20070305.5mdv2007.1
+ Revision: 134477
- Fix typo
- Fix spec file

* Mon Mar 05 2007 Laurent Montel <lmontel@mandriva.com> 1:0.3.11-0.20070305.3mdv2007.1
+ Revision: 133216
- Fix provides

* Mon Mar 05 2007 Laurent Montel <lmontel@mandriva.com> 1:0.3.11-0.20070305.2mdv2007.1
+ Revision: 132840
- New version (need by kde4 shortly)

* Fri Jan 12 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.3.11-1mdv2007.1
+ Revision: 107713
- Add Patch0: Fix install on x86_64
- Fix BuildRequires
- Fix File list
- Fix BuildRequires
- Fix Description
- Fix Group
- New version 0.3.11
- Fix File list
- Import strigi

