# TODO:
# - Add locale files
# - Add new package for Olive, previously included here now it's own project: http://wiki.bazaar.canonical.com/Olive/
%define		ver	0.99
%define		minor	1
Summary:	Plugin for Bazaar-NG (bzr)
Summary(pl.UTF-8):	Wtyczka do Bazaar-NG (bzr)
Name:		bzr-gtk
Version:	%{ver}.%{minor}
Release:	8
License:	GPL v2+
Group:		Development/Version Control
# Source0:	https://launchpad.net/bzr-gtk/%{ver}/%{version}/+download/bzr-gtk-%{version}.tar.gz
Source0:	http://samba.org/~jelmer/bzr/%{name}-%{version}.tar.gz
# Source0-md5:	68354924f3104ab1ba7efc8bfe15ae0b
URL:		http://bazaar-vcs.org/bzr-gtk
BuildRequires:	bzr >= %{ver}
BuildRequires:	gettext-tools
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.4
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires(post,postun):	desktop-file-utils
%pyrequires_eq	python
Requires:	bzr >= %{ver}
Requires:	python-pygtk-glade >= 2:2.10
Requires:	python-pygtk-gtk >= 2:2.10
Suggests:	python-gnome
Suggests:	python-pycairo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bzr-gtk is a plugin for Bazaar-NG (bzr) that aims to provide GTK+
interfaces to most Bazaar operations. Provided commands are:
- gcommit
- gdiff
- visualise
- gannotate
- gbranch

%description -l pl.UTF-8
bzr-gtk jest wtyczką dla Bazaar-NG (bzr), która ma na celu
dostarczenie graficznego interfejsu GTK+ dla większości poleceń
Bazaar. Dostępnymi poleceniami są:
- gcommit
- gdiff
- visualise
- gannotate
- gbranch

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--install-purelib %{py_sitedir} \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%banner %{name} -e << EOF
For full functionality, you need to install:
- python-pycairo (for graphs in the visualisation tool)
- python-gnome (for Nautilus integration)
EOF

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/bzr-handle-patch
%attr(755,root,root) %{_bindir}/bzr-notify
%{py_sitedir}/bzrlib/plugins/gtk
%{_datadir}/bzr-gtk
%{_desktopdir}/bazaar-properties.desktop
%{_desktopdir}/bzr-notify.desktop
%{_desktopdir}/bzr-handle-patch.desktop
%{_pixmapsdir}/bzr-icon-64.png
%{_iconsdir}/hicolor/scalable/emblems
%{_datadir}/application-registry/bzr-gtk.applications
