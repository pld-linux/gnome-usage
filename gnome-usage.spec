# TODO: use gtk4-update-icon-cache
Summary:	View information about use of system resources, like memory and disk space
Summary(pl.UTF-8):	Widok informacji o użyciu zasobów systemowych, takich jak pamięć czy miejsce na dysku
Name:		gnome-usage
Version:	46.1
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	https://download.gnome.org/sources/gnome-usage/46/%{name}-%{version}.tar.xz
# Source0-md5:	a832ba0ea2b958bf8cb50c5cac9b7900
URL:		https://wiki.gnome.org/Apps/Usage
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.74
BuildRequires:	gtk4-devel >= 4.11.3
BuildRequires:	libadwaita-devel >= 1.5
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	libgtop-devel >= 1:2.34.0
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker3-devel >= 3.0
BuildRequires:	vala
BuildRequires:	vala-libadwaita >= 1.5
BuildRequires:	vala-tracker3 >= 3.0
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.74
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.74
Requires:	gtk4 >= 4.11.3
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.5
Requires:	libgtop >= 1:2.34.0
Requires:	tracker3 >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A nice way to view information about use of system resources, like
memory and disk space.

Notable features:
 - Monitor processor, memory, disk and network usage.
 - Finding what application is using all your CPU.
 - Allow the user to forcefully close applications.

%description -l pl.UTF-8
Ładny widok informacji o wykorzystaniu zasobów systemowych, takich jak
pamięć czy miejsce na dysku.

Główne możliwości:
 - monitorowanie wykorzystania procesora, pamięci, dysku i sieci,
 - znajdowanie aplikacji wykorzystujących całą moc procesora,
 - wymuszenie zamknięcia aplikacji przez użytkownika.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-usage
%{_datadir}/glib-2.0/schemas/org.gnome.Usage.gschema.xml
%{_datadir}/metainfo/org.gnome.Usage.appdata.xml
%{_desktopdir}/org.gnome.Usage.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Usage.svg
