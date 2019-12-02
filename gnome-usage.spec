Summary:	View information about use of system resources, like memory and disk space
Summary(pl.UTF-8):	Widok informacji o użyciu zasobów systemowych, takich jak pamięć czy miejsce na dysku
Name:		gnome-usage
Version:	3.32.0
Release:	2
License:	GPL v3+
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-usage/3.32/%{name}-%{version}.tar.xz
# Source0-md5:	41fe4f9d9d33709d8fcb5538c51ba40b
URL:		https://wiki.gnome.org/Apps/Usage
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38
BuildRequires:	gtk+3-devel >= 3.20.10
BuildRequires:	libdazzle-devel >= 3.30
BuildRequires:	libgtop-devel >= 1:2.34.0
BuildRequires:	meson >= 0.37.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.38
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.38
Requires:	gtk+3 >= 3.20.10
Requires:	hicolor-icon-theme
Requires:	libdazzle >= 3.30
Requires:	libgtop >= 1:2.34.0
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
