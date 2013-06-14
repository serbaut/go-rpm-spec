Name:		go
Version:	1.1.1
Release:	1%{?dist}
Summary:	Go development tools
Group:		Development/Languages
License:	BSD
URL:		http://golang.org
Source:		https://go.googlecode.com/files/%{name}%{version}.src.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	gcc
AutoReqProv:	no

%define __spec_install_post %{nil}

%description
Go is an open source programming environment that makes
it easy to build simple, reliable, and efficient software.

This package also includes support for cross compiling to
windows/amd64 and darwin/amd64.

%prep
%setup -q -n go

%build
cd src
unset GOROOT GOBIN
export GOROOT_FINAL=%{_libdir}/go
for os in linux darwin windows; do
    for arch in amd64; do
        GOOS=$os GOARCH=$arch ./make.bash --no-clean
    done
done

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/go
cp -a pkg src %{buildroot}%{_libdir}/go
install -d %{buildroot}%{_bindir}
install -m 755 bin/{go,godoc,gofmt} %{buildroot}%{_bindir}
install -d %{buildroot}%{_includedir}/go
cp -a include/* %{buildroot}%{_includedir}/go
install -d %{buildroot}%{_datadir}/go
cp -a lib misc %{buildroot}%{_datadir}/go
install -D misc/bash/go %{buildroot}%{_sysconfdir}/bash_completion.d/go

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS CONTRIBUTORS LICENSE PATENTS README VERSION api doc/*
%{_libdir}/go
%{_bindir}/*
%{_datadir}/go
%{_includedir}/go
%{_sysconfdir}/bash_completion.d/go
