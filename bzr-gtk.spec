# TODO: Fix or wait until released olive-gtk menu log will work again (fixed already in repo)
Summary:	Plugin for Bazaar-NG providing GUI to most operations
Summary(pl.UTF-8):	Wtyczka do Bazaar-NG udostępniająca interfejs graficzny dla większości operacji
Name:		bzr-gtk
%define		ver	0.93
%define		minor	0
Version:	%{ver}.%{minor}
Release:	1.90
License:	GPL v2
Group:		Development/Version Control
Source0:	https://launchpad.net/bzr-gtk/%{ver}/%{version}/+download/bzr-gtk-%{version}.tar.gz
# Source0-md5:	de4951911d7e39d88916d276177476f3
Patch0:		%{name}-kill-pygtk-2_10-reqs.patch

URL:		http://bazaar-vcs.org/bzr-gtk
BuildRequires:	python >= 1:2.4
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq  python
Requires:	bzr >= %{ver}
Requires:	python-pygtk-glade
Requires:	python-pygtk-gtk >= 2.8
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
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_datadir}/olive
