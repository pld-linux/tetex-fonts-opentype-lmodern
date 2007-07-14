Summary:	TeX LM fonts in OpenType format
Summary(pl.UTF-8):	Fonty TeX LM w formacie OpenType
Name:		tetex-fonts-opentype-lmodern
Version:	1.010
Release:	1
License:	GPL
Group:		Fonts
Source0:	http://www.gust.org.pl/projects/e-foundry/latin-modern/download/lm%{version}x-otf.zip
# Source0-md5:	eeb4573b52367fc361394d7540323877
URL:		http://www.gust.org.pl/projects/e-foundry/latin-modern/
Requires(post,postun):	tetex
Requires:	tetex
Requires:	tetex-dirs-fonts >= 1:3.0-5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	texmf	%{_datadir}/texmf

%description
The Latin Modern fonts are derived from the famous Computer Modern
fonts designed by Donald E. Knuth and first published by the American
Matematical Society (AMS) in 1997. One of the main extensions is the
addition of an extensive set of diacritical characters, covering many
scripts based on the Latin character set, mainly european, but not
only, most notably Vietnamese. The project is authored by Bogusław
“Jacko” Jackowski and Janusz M. Nowacki aka “Ulan”, supported in LaTeX
matters by Marcin Woliński.

%description -l pl.UTF-8
Fonty Latin Modern wywodzą się ze słynnych fontów Computer Modern
zaprojektowanych przez Donalda E. Knutha i opublikowanych po raz
pierwszy przez Amerykańskie Towarzystwo Matematyczne (AMS) w 1997.
Jednym z najważniejszych rozszerzeń jest dodanie pokaźnego zbioru
znaków diakrytycznych, obejmujących wiele alfabetów bazujących
na alfabecie łacińskim, głównie europejskich, ale nie tylko,
w szczególności wietnamski. Projekt jest autorstwa Bogusława „Jacko”
Jackowskiego i Janusza M. Nowackiego „Ulana”, wspieranych w sprawach
LaTeXowych przez Marcina Wolińskiego.

%prep
%setup -q -c -T -a0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{texmf}
cp -a fonts $RPM_BUILD_ROOT%{texmf}

%clean
rm -rf $RPM_BUILD_ROOT

%post
texhash

%postun
[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash

%files
%defattr(644,root,root,755)
%{texmf}/fonts/opentype/public/lm
