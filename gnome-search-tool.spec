Summary:	GNOME search tool
Summary(pl.UTF-8):	Narzędzie wyszukujące dla GNOME
Name:		gnome-search-tool
Version:	3.6.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-search-tool/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	6aed3d63b77ceb0685a57300bc057a7e
URL:		http://live.gnome.org/GnomeUtils
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.30.0
Requires:	glib2 >= 1:2.30.0
Requires:	gtk+3 >= 3.4.0
Provides:	gnome-utils-search-tool = 1:%{version}-%{release}
Obsoletes:	gnome-utils-search-tool < 1:3.3.2-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows to search for files on system.

%description -l pl.UTF-8
Pozwala na wyszukiwanie plików w systemie.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/gnome-search-tool
%{_desktopdir}/gnome-search-tool.desktop
%{_pixmapsdir}/gsearchtool
%{_mandir}/man1/gnome-search-tool.1*
%{_datadir}/GConf/gsettings/gnome-search-tool.convert
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-search-tool.gschema.xml
