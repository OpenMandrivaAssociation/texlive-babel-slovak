%global tl_name babel-slovak
%global tl_revision 30292

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1a
Release:	%{tl_revision}.1
Summary:	Babel support for typesetting Slovak
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/slovak
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-slovak.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-slovak.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-slovak.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the language definition file for support of Slovak
in babel, including Slovak variants of LaTeX built-in-names. Shortcuts
are also defined.

