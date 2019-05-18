# http://trac.wildfiregames.com/wiki/BuildInstructions#Linux

Name:		0ad-data
Epoch:		1
Version:	0.0.23b
Release:	1
Summary:	The Data Files for 0 AD
License:	CC-BY-SA
Group:		Games/Strategy
Url:		http://wildfiregames.com/0ad/
Source0:	http://releases.wildfiregames.com/0ad-%{version}-alpha-unix-data.tar.xz
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
        unzip ../public.zip
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
