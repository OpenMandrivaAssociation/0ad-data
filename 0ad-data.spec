%define revision 08413

Name:           0ad-data
Version:        1.0
Release:        %mkrel 0.%{revision}.1
Summary:        The Data Files for 0 AD
License:        GNU GPL v2 or later
Group:          Games/Strategy
Url:            http://wildfiregames.com/0ad/
Source:         0ad-r%{revision}-alpha-unix-data.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform
real-time strategy (RTS) game of ancient warfare. In short, it is a
historically-based war/economy game that allows players to relive or rewrite
the history of Western civilizations, focusing on the years between 500 B.C.
and 500 A.D. The project is highly ambitious, involving state-of-the-art 3D
graphics, detailed artwork, sound, and a flexible and powerful custom-built
game engine.

The game has been in development by Wildfire Games (WFG), a group of volunteer, 
hobbyist game developers, since 2001. The code and data are available under the
GPL license, and the art, sound and documentation are available under CC-BY-SA.
In short, we consider 0 A.D. an an educational celebration of game development
and ancient history.

%prep
%setup -q -n 0ad-%{version}-alpha

%build

%install
%__mkdir_p %{buildroot}%{_datadir}
%__mv binaries/data %{buildroot}%{_datadir}/0ad

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/0ad
