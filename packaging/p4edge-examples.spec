%{!?examplesroot: %global examplesroot /usr/share/p4edge/t4p4s}
Name:           p4edge-examples
Version:        0.0.0
Release:        0%{?dist}
Summary:        P4Edge examples
License:        Apache 2.0
URL:            https://github.com/p4edge/examples
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Packager:       Dávid Kis <kidraai@.inf.elte.hu>

%description
P4Edge examples

%prep
%autosetup

%build

%install

rm -rf %{buildroot}

mkdir -p %{buildroot}%{examplesroot}
cp -r arp_icmp/ %{buildroot}%{examplesroot}
cp -r calc/ %{buildroot}%{examplesroot}
cp -r l2switch/ %{buildroot}%{examplesroot}
cp -r stateful-firewall/ %{buildroot}%{examplesroot}
cp -r traffic-filter/ %{buildroot}%{examplesroot}
cp -r basic_mirror/ %{buildroot}%{examplesroot}

%files
%{examplesroot}/arp_icmp/*
%{examplesroot}/calc/*
%{examplesroot}/l2switch/*
%{examplesroot}/stateful-firewall/*
%{examplesroot}/traffic-filter/*
%{examplesroot}/basic_mirror/*
