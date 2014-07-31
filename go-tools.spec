Name:           go-tools
Version:        1.3
Release:        3%{?dist}
Summary:        Go development tools
Group:          Development/Languages
License:        BSD
URL:            http://golang.org
Source:         https://tools.go.googlecode.com
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  go >= %{version}
AutoReqProv:    no
Requires:       go >= %{version}

%define __spec_install_post %{nil}

%define tooldir %{_libdir}/go/pkg/tool/linux_amd64

%description
This package includes additional go development tools.

%prep
export GOPATH=$(pwd)/go-tools
go get -d code.google.com/p/go.tools/cmd/godoc code.google.com/p/go.tools/cmd/cover

%build
export GOPATH=$(pwd)/go-tools
(cd go-tools/src/code.google.com/p/go.tools/cmd/godoc && go build)
(cd go-tools/src/code.google.com/p/go.tools/cmd/cover && go build)
(cd go-tools/src/code.google.com/p/go.tools/cmd/vet && go build)

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{tooldir}
install go-tools/src/code.google.com/p/go.tools/cmd/godoc/godoc %{buildroot}%{_bindir}
install go-tools/src/code.google.com/p/go.tools/cmd/cover/cover %{buildroot}%{tooldir}
install go-tools/src/code.google.com/p/go.tools/cmd/vet/vet %{buildroot}%{tooldir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/godoc
%{tooldir}/cover
%{tooldir}/vet
