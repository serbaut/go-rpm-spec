Name:           go-tools
Version:        1.4
Release:        4%{?dist}
Summary:        Go development tools
Group:          Development/Languages
License:        BSD
URL:            http://golang.org
Source:         http://tools.go.googlecode.com/archive/release-branch.go%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  go >= %{version}
AutoReqProv:    no
Requires:       go >= %{version}

%define __spec_install_post %{nil}

%define tooldir %{_libdir}/go/pkg/tool/linux_amd64

%description
This package includes additional go development tools.

%prep
%setup -T -c -n go/src/golang.org/x/tools
tar --strip-components=1 -x -f %{SOURCE0}

%build
export GOPATH=%{_builddir}/go
(cd cmd/godoc && go build)
(cd cmd/cover && go build)
(cd cmd/vet && go build)

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{tooldir}
install cmd/godoc/godoc %{buildroot}%{_bindir}
install cmd/cover/cover %{buildroot}%{tooldir}
install cmd/vet/vet %{buildroot}%{tooldir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/godoc
%{tooldir}/cover
%{tooldir}/vet
