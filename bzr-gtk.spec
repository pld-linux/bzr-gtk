Summary:	Plugin for Bazaar-NG providing GUI to most operations
Summary(pl.UTF-8):	Wtyczka do Bazaar-NG udostępniająca interfejs graficzny dla większości operacji
Name:		bzr-gtk
Version:	0.17.0
Release:	1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://samba.org/~jelmer/bzr/%{name}-%{version}.tar.gz
# Source0-md5:	053425c9fa3f95e3d72330ec9c3fe5f4
URL:		http://bazaar-vcs.org/bzr-gtk
BuildRequires:	python >= 1:2.4
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq  python
Requires:	bzr >= 0.13
Requires:	python-pygtk-glade
BuildArch:	noarch
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
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
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
%{py_sitescriptdir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_datadir}/olive
