Name:		texlive-forum
Version:	64566
Release:	1
Summary:	Forum fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/forum
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forum.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Forum font, designed by Denis Masharov. Forum
has antique, classic "Roman" proportions. It can be used to set
body texts and works well in titles and headlines too. It is
truly multilingual, with glyphs for Central and Eastern Europe,
Baltics, Cyrillic and Asian Cyrillic communities. There is
currently just a regular weight and an artificially emboldened
bold.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/forum
%{_texmfdistdir}/fonts/vf/public/forum
%{_texmfdistdir}/fonts/type1/public/forum
%{_texmfdistdir}/fonts/tfm/public/forum
%{_texmfdistdir}/fonts/opentype/public/forum
%{_texmfdistdir}/fonts/map/dvips/forum
%{_texmfdistdir}/fonts/enc/dvips/forum
%doc %{_texmfdistdir}/doc/fonts/forum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
