### RPM spec file for Go

Build with

    sudo yum install rpmdevtools yum-utils
    sudo yum-builddep go.spec
    rpmdev-setuptree
    spectool -R -g go.spec
    rpmbuild -bb go.spec
    spectool -R -g go-tools.spec
    rpmbuild -bb go-tools.spec
