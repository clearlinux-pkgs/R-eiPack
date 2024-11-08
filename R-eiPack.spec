#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-eiPack
Version  : 0.2.2
Release  : 52
URL      : https://cran.r-project.org/src/contrib/eiPack_0.2-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/eiPack_0.2-2.tar.gz
Summary  : Ecological Inference and Higher-Dimension Data Management
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-eiPack-lib = %{version}-%{release}
Requires: R-eiPack-license = %{version}-%{release}
Requires: R-coda
Requires: R-msm
BuildRequires : R-coda
BuildRequires : R-msm
BuildRequires : buildreq-R

%description
tables using the extreme case analysis, ecological regression,
        and Multinomial-Dirichlet ecological inference models.  Also
        provides tools for manipulating higher-dimension data objects.

%package lib
Summary: lib components for the R-eiPack package.
Group: Libraries
Requires: R-eiPack-license = %{version}-%{release}

%description lib
lib components for the R-eiPack package.


%package license
Summary: license components for the R-eiPack package.
Group: Default

%description license
license components for the R-eiPack package.


%prep
%setup -q -n eiPack
cd %{_builddir}/eiPack

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678817190

%install
export SOURCE_DATE_EPOCH=1678817190
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-eiPack
cp %{_builddir}/eiPack/COPYING %{buildroot}/usr/share/package-licenses/R-eiPack/5779f8f325460008fc233b70db6e1a774fc83643 || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/eiPack/DESCRIPTION
/usr/lib64/R/library/eiPack/INDEX
/usr/lib64/R/library/eiPack/LICENSE
/usr/lib64/R/library/eiPack/Meta/Rd.rds
/usr/lib64/R/library/eiPack/Meta/data.rds
/usr/lib64/R/library/eiPack/Meta/demo.rds
/usr/lib64/R/library/eiPack/Meta/features.rds
/usr/lib64/R/library/eiPack/Meta/hsearch.rds
/usr/lib64/R/library/eiPack/Meta/links.rds
/usr/lib64/R/library/eiPack/Meta/nsInfo.rds
/usr/lib64/R/library/eiPack/Meta/package.rds
/usr/lib64/R/library/eiPack/NAMESPACE
/usr/lib64/R/library/eiPack/R/eiPack
/usr/lib64/R/library/eiPack/R/eiPack.rdb
/usr/lib64/R/library/eiPack/R/eiPack.rdx
/usr/lib64/R/library/eiPack/data/redistrict.tab.gz
/usr/lib64/R/library/eiPack/data/senc.tab.gz
/usr/lib64/R/library/eiPack/data/tuneA.tab.gz
/usr/lib64/R/library/eiPack/data/tuneB.tab.gz
/usr/lib64/R/library/eiPack/demo/bounds.R
/usr/lib64/R/library/eiPack/demo/ei.MD.bayes.R
/usr/lib64/R/library/eiPack/demo/ei.reg.R
/usr/lib64/R/library/eiPack/demo/ei.reg.bayes.R
/usr/lib64/R/library/eiPack/demo/lambda.MD.R
/usr/lib64/R/library/eiPack/demo/lambda.reg.R
/usr/lib64/R/library/eiPack/demo/lambda.reg.bayes.R
/usr/lib64/R/library/eiPack/help/AnIndex
/usr/lib64/R/library/eiPack/help/aliases.rds
/usr/lib64/R/library/eiPack/help/eiPack.rdb
/usr/lib64/R/library/eiPack/help/eiPack.rdx
/usr/lib64/R/library/eiPack/help/paths.rds
/usr/lib64/R/library/eiPack/html/00Index.html
/usr/lib64/R/library/eiPack/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/eiPack/libs/eiPack.so
/usr/lib64/R/library/eiPack/libs/eiPack.so.avx2
/usr/lib64/R/library/eiPack/libs/eiPack.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-eiPack/5779f8f325460008fc233b70db6e1a774fc83643
