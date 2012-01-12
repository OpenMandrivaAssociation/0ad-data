# http://trac.wildfiregames.com/wiki/BuildInstructions#Linux

Name:           0ad-data
Epoch:		1
Version:        r10803
Release:        0.1
Summary:        The Data Files for 0 AD
License:        GPLv2+
Group:          Games/Strategy
Url:            http://wildfiregames.com/0ad/
Source:         0ad-%{version}-alpha-unix-data.tar.xz
BuildArch:      noarch

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
%__mkdir_p %{buildroot}%{_gamesdatadir}
%__mv binaries/data %{buildroot}%{_gamesdatadir}/0ad

%files
%{_gamesdatadir}/0ad
