# http://trac.wildfiregames.com/wiki/BuildInstructions#Linux

Name:		0ad-data
Epoch:		1
Version:	0.0.11
Release:	3
Summary:	The Data Files for 0 AD
License:	GPLv2+
Group:		Games/Strategy
Url:		http://wildfiregames.com/0ad/
Source:		http://releases.wildfiregames.com/0ad-%{version}-alpha-unix-data.tar.xz
BuildRequires:	unzip
Requires:	fonts-ttf-dejavu
BuildArch:	noarch

%description
0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform
real-time strategy (RTS) game of ancient warfare. In short, it is a
historically-based war/economy game that allows players to relive or rewrite
the history of Western civilizations, focusing on the years between 500 B.C.
and 500 A.D. The project is highly ambitious, involving state-of-the-art 3D
graphics, detailed artwork, sound, and a flexible and powerful custom-built
game engine.

This package contains the 0ad data files.

%prep
%setup -q -n 0ad-%{version}-alpha

%build
pushd binaries/data/mods/public
    mkdir tmp
    pushd tmp
        unzip -x ../public.zip
	cp -a art/LICENSE.txt ../../../../../LICENSE-art.txt
	cp -a audio/LICENSE.txt ../../../../../LICENSE-audio.txt
        rm -fr *
    popd
    rm -fr tmp
popd

%install
mkdir -p %{buildroot}%{_gamesdatadir}
rm -f tools/fontbuilder/fonts/*.ttf
mv binaries/data %{buildroot}%{_gamesdatadir}/0ad

%files
%doc LICENSE-art.txt LICENSE-audio.txt
%{_gamesdatadir}/0ad


%changelog
* Fri Sep 28 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:0.0.11-2
+ Revision: 817862
- Use same pattern for release tag as main 0ad package.
- Do not install duplicate dejavu fonts.
- Synch with fedora package.
- Unpack and install license files for art and audio.

  + Sergey Zhemoitel <serg@mandriva.org>
    - Update to 0.0.11 Alpha

* Fri Jun 29 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:r11863-0.1
+ Revision: 807490
- Update to alpha 10 aka r11863

* Sat Mar 17 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:r11339-0.1
+ Revision: 785457
- Update to alpha9

* Thu Jan 12 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:r10803-0.1
+ Revision: 760250
- Install data files in gamesdatadir.
- Use upstream suggested versioning schema.

* Sun Jan 08 2012 Sergey Zhemoitel <serg@mandriva.org> 1.0-0.10803.1
+ Revision: 758717
- add new revision 10803

* Sat Sep 17 2011 Sergey Zhemoitel <serg@mandriva.org> 1.0-0.10288.1
+ Revision: 700144
- new revision 10288

* Mon Jul 18 2011 Sergey Zhemoitel <serg@mandriva.org> 1.0-0.09786.1
+ Revision: 690391
- imported package 0ad-data

* Wed Oct 20 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-0.08413.1mdv2011.0
+ Revision: 586980
- set version to 1.0, and use svn revision number in release tag instead

* Wed Oct 20 2010 Guillaume Rousse <guillomovitch@mandriva.org> r08413-1mdv2011.0
+ Revision: 586941
- import 0ad-data

