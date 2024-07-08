Name:           fragments
Version:        3.0.1
Release:        1
Summary:        A GTK4 BitTorrent Client
License:        GPL-3.0
Group:          Productivity/Networking/Other
URL:            https://gitlab.gnome.org/World/Fragments
Source0:        https://gitlab.gnome.org/World/Fragments/-/archive/%{version}/Fragments-%{version}.tar.bz2
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  gettext
BuildRequires:  appstream-util
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  git
BuildRequires:  libxml2-utils
BuildRequires:  meson
BuildRequires:  pkgconfig(openssl)
BuildRequires:  rust-packaging
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.66
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk4) >= 4.0.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.0.0
BuildRequires:  pkgconfig(sqlite3) >= 3.20
Requires:       transmission-daemon

%description
Fragments is an easy to use BitTorrent client which follows the
GNOME HIG and includes well thought-out features.

%lang_package

%prep
%autosetup -a1 -n Fragments-%{version}
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%meson
%meson_build

%install
%meson_install
%find_lang fragments %{?no_lang_C}

%files -f fragments.lang
%license COPYING.md
%doc README.md
%{_bindir}/fragments
%{_datadir}/applications/de.haeckerfelix.Fragments.desktop
%{_datadir}/glib-2.0/schemas/de.haeckerfelix.Fragments.gschema.xml
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/de.haeckerfelix.Fragments.metainfo.xml
%{_datadir}/dbus-1/services/de.haeckerfelix.Fragments.service
%{_datadir}/fragments/
