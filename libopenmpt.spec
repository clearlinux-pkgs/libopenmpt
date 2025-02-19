#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: e36a856
#
Name     : libopenmpt
Version  : 0.7.13
Release  : 4
URL      : https://lib.openmpt.org/files/libopenmpt/src/libopenmpt-0.7.13+release.autotools.tar.gz
Source0  : https://lib.openmpt.org/files/libopenmpt/src/libopenmpt-0.7.13+release.autotools.tar.gz
Summary  : Tracker module player based on OpenMPT
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0
Requires: libopenmpt-bin = %{version}-%{release}
Requires: libopenmpt-lib = %{version}-%{release}
Requires: libopenmpt-license = %{version}-%{release}
Requires: libopenmpt-man = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-configure
BuildRequires : doxygen
BuildRequires : file
BuildRequires : perl
BuildRequires : pkgconfig(flac)
BuildRequires : pkgconfig(libmpg123)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : pkgconfig(ogg)
BuildRequires : pkgconfig(portaudio-2.0)
BuildRequires : pkgconfig(sdl2)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(vorbis)
BuildRequires : pkgconfig(vorbisfile)
BuildRequires : pkgconfig(zlib)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
======
OpenMPT and libopenmpt
======================
This repository contains OpenMPT, a free Windows/Wine-based
[tracker](https://en.wikipedia.org/wiki/Music_tracker) and libopenmpt,
a library to render tracker music (MOD, XM, S3M, IT MPTM and dozens of other
legacy formats) to a PCM audio stream. libopenmpt is directly based on OpenMPT,
offering the same playback quality and format support, and development of the
two happens in parallel.

%package bin
Summary: bin components for the libopenmpt package.
Group: Binaries
Requires: libopenmpt-license = %{version}-%{release}

%description bin
bin components for the libopenmpt package.


%package dev
Summary: dev components for the libopenmpt package.
Group: Development
Requires: libopenmpt-lib = %{version}-%{release}
Requires: libopenmpt-bin = %{version}-%{release}
Provides: libopenmpt-devel = %{version}-%{release}
Requires: libopenmpt = %{version}-%{release}

%description dev
dev components for the libopenmpt package.


%package doc
Summary: doc components for the libopenmpt package.
Group: Documentation
Requires: libopenmpt-man = %{version}-%{release}

%description doc
doc components for the libopenmpt package.


%package lib
Summary: lib components for the libopenmpt package.
Group: Libraries
Requires: libopenmpt-license = %{version}-%{release}

%description lib
lib components for the libopenmpt package.


%package license
Summary: license components for the libopenmpt package.
Group: Default

%description license
license components for the libopenmpt package.


%package man
Summary: man components for the libopenmpt package.
Group: Default

%description man
man components for the libopenmpt package.


%prep
%setup -q -n libopenmpt-0.7.13+release.autotools
cd %{_builddir}/libopenmpt-0.7.13+release.autotools
pushd ..
cp -a libopenmpt-0.7.13+release.autotools buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739385368
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1739385368
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libopenmpt
cp %{_builddir}/libopenmpt-%{version}+release.autotools/LICENSE %{buildroot}/usr/share/package-licenses/libopenmpt/a024ea8e611a74d5eff3219126c74b9e28f83925 || :
cp %{_builddir}/libopenmpt-%{version}+release.autotools/src/mpt/LICENSE.BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libopenmpt/fae158dea25fa7046add744a8dce4746b4aed467 || :
cp %{_builddir}/libopenmpt-%{version}+release.autotools/src/mpt/LICENSE.BSL-1.0.txt %{buildroot}/usr/share/package-licenses/libopenmpt/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/openmpt123
/usr/bin/openmpt123

%files dev
%defattr(-,root,root,-)
/usr/include/libopenmpt/libopenmpt.h
/usr/include/libopenmpt/libopenmpt.hpp
/usr/include/libopenmpt/libopenmpt_config.h
/usr/include/libopenmpt/libopenmpt_ext.h
/usr/include/libopenmpt/libopenmpt_ext.hpp
/usr/include/libopenmpt/libopenmpt_stream_callbacks_buffer.h
/usr/include/libopenmpt/libopenmpt_stream_callbacks_fd.h
/usr/include/libopenmpt/libopenmpt_stream_callbacks_file.h
/usr/include/libopenmpt/libopenmpt_stream_callbacks_file_mingw.h
/usr/include/libopenmpt/libopenmpt_stream_callbacks_file_msvcrt.h
/usr/include/libopenmpt/libopenmpt_stream_callbacks_file_posix.h
/usr/include/libopenmpt/libopenmpt_stream_callbacks_file_posix_lfs64.h
/usr/include/libopenmpt/libopenmpt_version.h
/usr/lib64/libopenmpt.so
/usr/lib64/pkgconfig/libopenmpt.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/libopenmpt/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libopenmpt.so.0.4.4
/usr/lib64/libopenmpt.so.0
/usr/lib64/libopenmpt.so.0.4.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libopenmpt/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/libopenmpt/a024ea8e611a74d5eff3219126c74b9e28f83925
/usr/share/package-licenses/libopenmpt/fae158dea25fa7046add744a8dce4746b4aed467

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/openmpt123.1
