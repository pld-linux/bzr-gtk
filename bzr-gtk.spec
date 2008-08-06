# TODO:  Add locale files
Summary:	Plugin for Bazaar-NG providing GUI to most operations
Summary(pl.UTF-8):	Wtyczka do Bazaar-NG udostępniająca interfejs graficzny dla większości operacji
Name:		bzr-gtk
%define		ver	0.95
%define		minor	0
Version:	%{ver}.%{minor}
Release:	2
License:	GPL v2+
Group:		Development/Version Control
# Source0:	https://launchpad.net/bzr-gtk/%{ver}/%{version}/+download/bzr-gtk-%{version}.tar.gz
Source0:	http://samba.org/~jelmer/bzr/bzr-gtk-%{version}.tar.gz
# Source0-md5:	00aedce625672abca13d2d962b047ac0
Patch0:		%{name}-dbus_detection_fix.patch
URL:		http://bazaar-vcs.org/bzr-gtk
BuildRequires:	python >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires(post,postun):	desktop-file-utils
%pyrequires_eq	python
Requires:	bzr >= %{ver}
Requires:	python-pygtk-glade >= 2:2.10
Requires:	python-pygtk-gtk >= 2:2.10
Suggests:	python-pycairo
Suggests:	python-gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bzr-gtk is a plugin for Bazaar-NG (bzr) that aims to provide GTK+o s
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
%setup 
%patch0 -p1


%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
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
%attr(755,root,root) %{_bindir}/olive-gtk
%attr(755,root,root) %{_bindir}/bzr-handle-patch
%attr(755,root,root) %{_bindir}/bzr-notify

%{py_sitedir}/bzrlib/plugins/gtk
%{_datadir}/olive
%{_pixmapsdir}/olive-gtk.png
%{_desktopdir}/bazaar-properties.desktop
%{_desktopdir}/bzr-notify.desktop
%{_desktopdir}/bzr-handle-patch.desktop
%{_desktopdir}/olive-gtk.desktop

%{_datadir}/application-registry
%{_datadir}/application-registry/bzr-gtk.applications
%{_datadir}/bzr-gtk
#%%{_datadir}/bzr-gtk/icons
%{_datadir}/icons/hicolor/scalable/emblems/
%{_datadir}/pixmaps/bzr-icon-64.png
