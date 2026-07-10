%global tl_name forum
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Forum fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/forum
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/forum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/forum.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Forum font, designed by Denis Masharov. Forum has antique, classic
"Roman" proportions. It can be used to set body texts and works well in
titles and headlines too. It is truly multilingual, with glyphs for
Central and Eastern Europe, Baltics, Cyrillic and Asian Cyrillic
communities. There is currently just a regular weight and an
artificially emboldened bold.

