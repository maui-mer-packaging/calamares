# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       calamares

# >> macros
# << macros

Summary:    The distribution-independent installer framework
Version:    0.1.0
Release:    1
Group:      System/Base
License:    GPLv3+
URL:        https://github.com/calamares/calamares.git
Source0:    %{name}-%{version}.tar.xz
Source1:    settings.conf
Source2:    locale.conf
Source100:  calamares.yaml
Requires:   kf5-filesystem
Requires:   parted
Requires:   udisks2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(libatasmart)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  kcoreaddons-devel
BuildRequires:  kconfig-devel
BuildRequires:  solid-devel
BuildRequires:  ki18n-devel
BuildRequires:  libudisks2-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  python3-devel
BuildRequires:  boost-devel

%description
The distribution-independent installer framework.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup

sed -i 's|PythonLibs 3.3|PythonLibs 3.4|g' CMakeLists.txt

# << setup

%build
# >> build pre
# << build pre

%cmake .  \
    -DWITH_PARTITIONMANAGER=1 \
    -DCMAKE_INSTALL_LIBDIR=%{_lib}

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
install -D -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/calamares/modules/locale.conf
sed 's|/path/to/squashfs/image.sqfs|/run/initramfs/live/LiveOS/squashfs.img|' -i %{buildroot}%{_datadir}/calamares/modules/unsquashfs.conf
# << install post

%files
%defattr(-,root,root,-)
%{_kf5_prefix}/*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_libdir}/*.so
# >> files devel
# << files devel
