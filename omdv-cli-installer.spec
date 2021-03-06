Summary:	A CLI installer for OpenMandriva Lx
Name:		omdv-cli-installer
Version:	0.0.1
Release:	1
License:	GPLv2
Group:		System/Base
URL:		https://abf.io/openmandriva/omdv-cli-installer
Source0:	omdv-cli-install.sh
Source1:	TODO
Source2:	omdv-cli-installer.service
BuildArch:	noarch
BuildRequires:	systemd-units
Requires:	basesystem
Requires(post,postun):	rpm-helper

%description
A basic CLI installer for OpenMandriva Lx.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}{%{_bindir},%{_unitdir}}
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}/omdv-cli-install.sh
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

# (tpg) enable service by default
install -d %{buildroot}%{_presetdir}
cat > %{buildroot}%{_presetdir}/90-%{name}.preset << EOF
enable %{name}.service
EOF

%files
%doc TODO
%{_bindir}/omdv-cli-install.sh
%{_unitdir}/%{name}.service
