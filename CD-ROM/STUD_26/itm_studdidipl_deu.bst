%%
%% This file was initially generated with 'latex makebst'
%% The original source files were:
%%
%% merlin.mbs  (with options: `alph,alf-f,nm-rvv,jnrlst,aunm-semi,xmth,atit-u,jttl-rm,vnum-nr,volp-com,jwdpg,jwdvol,num-xser,btit-rm,bt-rm,add-pub,edparxc,bkedcap,au-col,pp,ed,abr,xedn,varand,and-xcom,xand,em-x')
%% ----------------------------------------
%% *** This bibliography style is ment for ITM phd thesis ***
%% 
%% Copyright 1994-2002 Patrick W Daly
 % ===============================================================
 % IMPORTANT NOTICE:
 % This bibliographic style (bst) file has been generated from one or
 % more master bibliographic style (mbs) files, listed above.
 %
 % This generated file can be redistributed and/or modified under the terms
 % of the LaTeX Project Public License Distributed from CTAN
 % archives in directory macros/latex/base/lppl.txt; either
 % version 1 of the License, or any later version.
 % ===============================================================
 % Name and version information of the main mbs file:
 % \ProvidesFile{merlin.mbs}[2002/10/21 4.05 (PWD, AO, DPC)]
 %   For use with BibTeX version 0.99a or later
 %-------------------------------------------------------------------
 % This bibliography style file is intended for texts in ENGLISH
 % This is a labelled citation style similar to the standard alpha.bst,
 %   where labels are of the form Dal90 or DBK89.
 % It requires no extra package to interface to the main text.
 % The form of the \bibitem entries is
 %   \bibitem[label]{key}...
 % Usage of \cite is as follows:
 %   \cite{key} ==>>          [label]
 %   \cite[chap. 2]{key} ==>> [label, chap. 2]
 % The order in the reference list is by label.
 %---------------------------------------------------------------------

 % Author: Florian Fleissner December 2007
 %
 % The major changes to the original file created by 'latex makebst' are:
 %
 %	- Citation labels with author names. The BibTex entries
 %			Author: P.A. Cundall and O. Strack
 %			Year: 1979
 %	  result in the citation label [CundallStrack79]
 %   Therefore, the function 'format.lab.names2' was inserted that manages
 %	  the format of the names as used in the label string
 %
 %%%
 %
 % modifications by CHH 2008: german abbreviations
 %
 % p.   -> S.
 % pp.  -> S.
 % ch.  -> Kap.
 % Vol. -> Bd.
 % No.  -> Nr.	
 % Eds. -> Hrsg.
 % masters thesis -> Masterarbeit
 % Phd thesis -> Doktorarbeit
 %
 % modifications by M. Burkhardt 2010: citation labels changed
 %
 % The citation labels don't include f.e. 'van' for names like 'van Beethoven'
 %
 % Example: For an item like 
 %
 % @INCOLLECTION{WanMerve01,
 %  author = {Eric Wan and Rudolph van der Merwe},
 %  title = {The Unscented Kalman Filter},
 %  booktitle = {Kalman Filtering and Neural Networks},
 %  chapter = {7},
 %  year = {2001},
 %  pages = {221--280},
 %  address = {Hoboken},
 %  publisher = {John Wiley \& Sons},
 % }
 % the entry in the reference list will look like
 %
 % [WanMerwe01] Wan, E.; van der Merwe, R.: The Unscented Kalman Filter. In
 %	Kalman Filtering and Neural Networks, Kap. 7, S. 221–280. Hoboken:
 %	John Wiley & Sons, 2001.
 % 
 % instead of
 %
 % [WanvanderMerwe01] Wan, E.; van der Merwe, R.: The Unscented Kalman Filter. In
 %	Kalman Filtering and Neural Networks, Kap. 7, S. 221–280. Hoboken:
 %	John Wiley & Sons, 2001.
 %
 % Amendments have been done in function 'format.lab.names2';
 %
 % modifications by M. Burkhardt 2010: citation labels changed
 %
 % If there are more than four authors, the reference label will look like
 % [BechtoldEtAl05].
 % 
 % Example: For an item like 
 %
 % @ARTICLE{BechtoldEtAl05,
 %  author = {Tamara Bechtold and Evgenii B Rudnyi and Jan G Korvink and Markus
 %	Graf and Andreas Hierlemann},
 %  title = {Connecting heat transfer macromodels for array MEMS structures},
 %  journal = {J. Micromech. Microeng.},
 %  year = {2005},
 %  volume = {15},
 %  pages = {1205--1214},
 %  file = {BechtoldEtAl05.pdf:/home/itm/institut/latex/ITM_Literatur_pdf/BechtoldEtAl05.pdf:PDF},
 %  owner = {fehr},
 %  timestamp = {2008.10.13}
 % }
 %
 % the entry in the reference list will look like
 %
 % [BechtoldEtAl05] Bechtold, T.; Rudnyi, E.B.; Korvink, J.G.; Graf, M.; Hierlemann,
 %       A.: Connecting heat transfer macromodels for array MEMS structures.
 %       J. Micromech. Microeng., Bd. 15, S. 1205–1214, 2005.
 %
 % instead of 
 %
 % [BechtoldRudnyiKorvinkGrafHierlemann05] Bechtold, T.; Rudnyi, E.B.; Korvink, J.G.; Graf, M.;
 %       Hierlemann, A.: Connecting heat transfer macromodels for array MEMS structures.
 %       J. Micromech. Microeng., Bd. 15, S. 1205–1214, 2005.
 %
 % Amendments have been done in function 'format.lab.names2';
 %%%
		
ENTRY
  { address
    author
    booktitle
    chapter
    edition
    editor
    howpublished
    institution
    journal
    key
    month
    note
    number
    organization
    pages
    publisher
    school
    series
    title
    type
    volume
    year
  }
  {}
  { label extra.label sort.label }
INTEGERS { output.state before.all mid.sentence after.sentence after.block }
FUNCTION {init.state.consts}
{ #0 'before.all :=
  #1 'mid.sentence :=
  #2 'after.sentence :=
  #3 'after.block :=
}
STRINGS { s t z}
FUNCTION {output.nonnull}
{ 's :=
  output.state mid.sentence =
    { ", " * write$ }
    { output.state after.block =
        { add.period$ write$
          newline$
          "\newblock " write$
        }
        { output.state before.all =
            'write$
            { add.period$ " " * write$ }
          if$
        }
      if$
      mid.sentence 'output.state :=
    }
  if$
  s
}
FUNCTION {output}
{ duplicate$ empty$
    'pop$
    'output.nonnull
  if$
}
FUNCTION {output.check}
{ 't :=
  duplicate$ empty$
    { pop$ "empty " t * " in " * cite$ * warning$ }
    'output.nonnull
  if$
}
FUNCTION {fin.entry}
{ add.period$
  write$
  newline$
}

FUNCTION {new.block}
{ output.state before.all =
    'skip$
    { after.block 'output.state := }
  if$
}
FUNCTION {new.sentence}
{ output.state after.block =
    'skip$
    { output.state before.all =
        'skip$
        { after.sentence 'output.state := }
      if$
    }
  if$
}
FUNCTION {add.blank}
{  " " * before.all 'output.state :=
}

FUNCTION {add.colon}
{ duplicate$ empty$
    'skip$
    { ":" * add.blank }
  if$
}

FUNCTION {date.block}
{
  new.block
}

FUNCTION {not}
{   { #0 }
    { #1 }
  if$
}
FUNCTION {and}
{   'skip$
    { pop$ #0 }
  if$
}
FUNCTION {or}
{   { pop$ #1 }
    'skip$
  if$
}
FUNCTION {new.block.checka}
{ empty$
    'skip$
    'new.block
  if$
}
FUNCTION {new.block.checkb}
{ empty$
  swap$ empty$
  and
    'skip$
    'new.block
  if$
}
FUNCTION {new.sentence.checka}
{ empty$
    'skip$
    'new.sentence
  if$
}
FUNCTION {new.sentence.checkb}
{ empty$
  swap$ empty$
  and
    'skip$
    'new.sentence
  if$
}
FUNCTION {field.or.null}
{ duplicate$ empty$
    { pop$ "" }
    'skip$
  if$
}
FUNCTION {emphasize}
{ skip$ }
FUNCTION {tie.or.space.prefix}
{ 
 %duplicate$ 
 %text.length$ #3 <
 %   { "~" }
 %   { " " }
 % if$
 %duplicate$ text.length$ #3 < % original version
 %   { "~" }
 %   { " " }
 % if$
 % swap$
 "~"                           % modified by FF/CHH for fixed blank after "S.", "Bd.", ...
 swap$
}

FUNCTION {capitalize}
{ "u" change.case$ "t" change.case$ }

FUNCTION {space.word}
{ " " swap$ * " " * }
 % Here are the language-specific definitions for explicit words.
 % Each function has a name bbl.xxx where xxx is the English word.
 % The language selected here is ENGLISH
FUNCTION {bbl.and}
{ "\protect\BIBand{}"}

FUNCTION {bbl.etal}
{ "et~al." }

FUNCTION {bbl.editors}
{ "Hrsg." }

FUNCTION {bbl.editor}
{ "Hrsg." }

FUNCTION {bbl.edby}
{ "edited by" }

FUNCTION {bbl.edition}
{ "Aufl." }

FUNCTION {bbl.volume}
{ "Bd." }

FUNCTION {bbl.of}
{ "von" }

FUNCTION {bbl.number}
{ "Nr." }

FUNCTION {bbl.nr}
{ "Nr." }

FUNCTION {bbl.in}
{ "in" }

FUNCTION {bbl.pages}
{ "S." }

FUNCTION {bbl.page}
{ "S." }

FUNCTION {bbl.chapter}
{ "Kap." }

FUNCTION {bbl.techrep}
{ "{Techn. Bericht}" }

FUNCTION {bbl.mthesis}
{ "Masterarbeit" }

FUNCTION {bbl.phdthesis}
{ "Doktorarbeit" }

MACRO {jan} {"Jan."}

MACRO {feb} {"Feb."}

MACRO {mar} {"Mrz"}

MACRO {apr} {"Apr."}

MACRO {may} {"Mai"}

MACRO {jun} {"Jun."}

MACRO {jul} {"Jul."}

MACRO {aug} {"Aug."}

MACRO {sep} {"Sept."}

MACRO {oct} {"Okt."}

MACRO {nov} {"Nov."}

MACRO {dec} {"Dez."}

MACRO {acmcs} {"ACM Computing Surveys"}

MACRO {acta} {"Acta Informatica"}

MACRO {cacm} {"Communications of the ACM"}

MACRO {ibmjrd} {"IBM Journal of Research and Development"}

MACRO {ibmsj} {"IBM Systems Journal"}

MACRO {ieeese} {"IEEE Transactions on Software Engineering"}

MACRO {ieeetc} {"IEEE Transactions on Computers"}

MACRO {ieeetcad}
 {"IEEE Transactions on Computer-Aided Design of Integrated Circuits"}

MACRO {ipl} {"Information Processing Letters"}

MACRO {jacm} {"Journal of the ACM"}

MACRO {jcss} {"Journal of Computer and System Sciences"}

MACRO {scp} {"Science of Computer Programming"}

MACRO {sicomp} {"SIAM Journal on Computing"}

MACRO {tocs} {"ACM Transactions on Computer Systems"}

MACRO {tods} {"ACM Transactions on Database Systems"}

MACRO {tog} {"ACM Transactions on Graphics"}

MACRO {toms} {"ACM Transactions on Mathematical Software"}

MACRO {toois} {"ACM Transactions on Office Information Systems"}

MACRO {toplas} {"ACM Transactions on Programming Languages and Systems"}

MACRO {tcs} {"Theoretical Computer Science"}
FUNCTION {bibinfo.check}
{ swap$
  duplicate$ missing$
    {
      pop$ pop$
      ""
    }
    { duplicate$ empty$
        {
          swap$ pop$
        }
        { swap$
          pop$
        }
      if$
    }
  if$
}
FUNCTION {bibinfo.warn}
{ swap$
  duplicate$ missing$
    {
      swap$ "missing " swap$ * " in " * cite$ * warning$ pop$
      ""
    }
    { duplicate$ empty$
        {
          swap$ "empty " swap$ * " in " * cite$ * warning$
        }
        { swap$
          pop$
        }
      if$
    }
  if$
}
STRINGS  { bibinfo}
INTEGERS { nameptr namesleft numnames }

FUNCTION {format.names}
{ 'bibinfo :=
  duplicate$ empty$ 'skip$ {
  's :=
  "" 't :=
  #1 'nameptr :=
  s num.names$ 'numnames :=
  numnames 'namesleft :=
    { namesleft #0 > }
    { s nameptr
    %  "{vv~}{ll}{, f{.}.}{ jj}" % original version
      "{vv~}{ll}{,~f{.}.}{ jj}"  % modified by CHH for fixed blank between name and inital
      format.name$
      bibinfo bibinfo.check
      't :=
      nameptr #1 >
        {
          namesleft #1 >
            { "; " * t * }
            {
              ";" *
              s nameptr "{ll}" format.name$ duplicate$ "others" =
                { 't := }
                { pop$ }
              if$
              t "others" =
                {
                  " " * bbl.etal *
                }
                { " " * t * }
              if$
            }
          if$
        }
        't
      if$
      nameptr #1 + 'nameptr :=
      namesleft #1 - 'namesleft :=
    }
  while$
  } if$
}
FUNCTION {format.names.ed}
{
  'bibinfo :=
  duplicate$ empty$ 'skip$ {
  's :=
  "" 't :=
  #1 'nameptr :=
  s num.names$ 'numnames :=
  numnames 'namesleft :=
    { namesleft #0 > }
    { s nameptr
      "{f{.}.~}{vv~}{ll}{ jj}"
      format.name$
      bibinfo bibinfo.check
      't :=
      nameptr #1 >
        {
          namesleft #1 >
            { "; " * t * }
            {
              ";" *
              s nameptr "{ll}" format.name$ duplicate$ "others" =
                { 't := }
                { pop$ }
              if$
              t "others" =
                {

                  " " * bbl.etal *
                }
                { " " * t * }
              if$
            }
          if$
        }
        't
      if$
      nameptr #1 + 'nameptr :=
      namesleft #1 - 'namesleft :=
    }
  while$
  } if$
}
FUNCTION {format.authors}
{ author "author" format.names
}
FUNCTION {get.bbl.editor}
{ editor num.names$ #1 > 'bbl.editors 'bbl.editor if$ }

FUNCTION {format.editors}
{ editor "editor" format.names duplicate$ empty$ 'skip$
    {
      " " *
      get.bbl.editor
      capitalize
   "(" swap$ * ")" *
      *
    }
  if$
}
FUNCTION {format.note}
{
 note empty$
    { "" }
    { note #1 #1 substring$
      duplicate$ "{" =
        'skip$
        { output.state mid.sentence =
          { "l" }
          { "u" }
        if$
        change.case$
        }
      if$
      note #2 global.max$ substring$ * "note" bibinfo.check
    }
  if$
}

FUNCTION {format.title}
{ title
  "title" bibinfo.check
}
FUNCTION {output.bibitem}
{ newline$
  "\bibitem[" label * "]{" * write$
  cite$ write$
  "}" write$
  newline$
  ""
  before.all 'output.state :=
}

FUNCTION {n.dashify}
{
  't :=
  ""
    { t empty$ not }
    { t #1 #1 substring$ "-" =
        { t #1 #2 substring$ "--" = not
            { "--" *
              t #2 global.max$ substring$ 't :=
            }
            {   { t #1 #1 substring$ "-" = }
                { "-" *
                  t #2 global.max$ substring$ 't :=
                }
              while$
            }
          if$
        }
        { t #1 #1 substring$ *
          t #2 global.max$ substring$ 't :=
        }
      if$
    }
  while$
}

FUNCTION {word.in}
{ bbl.in capitalize
  " " * }

FUNCTION {format.date}
{
  ""
  duplicate$ empty$
  year  "year"  bibinfo.check duplicate$ empty$
    { swap$ 'skip$
        { "there's a month but no year in " cite$ * warning$ }
      if$
      *
    }
    { swap$ 'skip$
        {
          swap$
          " " * swap$
        }
      if$
      *
    }
  if$
}
FUNCTION {format.btitle}
{ title "title" bibinfo.check
  duplicate$ empty$ 'skip$
    {
    }
  if$
}
FUNCTION {either.or.check}
{ empty$
    'pop$
    { "can't use both " swap$ * " fields in " * cite$ * warning$ }
  if$
}
FUNCTION {format.bvolume}
{ volume empty$
    { "" }
    { bbl.volume volume tie.or.space.prefix
      "volume" bibinfo.check * *
      series "series" bibinfo.check
      duplicate$ empty$ 'pop$
        { swap$ bbl.of space.word * swap$
          emphasize * }
      if$
      "volume and number" number either.or.check
    }
  if$
}
FUNCTION {format.number.series}
{ volume empty$
    { number empty$
        { series field.or.null }
        { series empty$
            { number "number" bibinfo.check }
        { output.state mid.sentence =
            { bbl.number }
            { bbl.number capitalize }
          if$
          number tie.or.space.prefix "number" bibinfo.check * *
          bbl.in space.word *
          series "series" bibinfo.check *
        }
      if$
    }
      if$
    }
    { "" }
  if$
}

FUNCTION {format.edition}
{ edition duplicate$ empty$ 'skip$
    {
      output.state mid.sentence =
        { "l" }
        { "t" }
      if$ change.case$
      "edition" bibinfo.check
      " " * bbl.edition *
    }
  if$
}
INTEGERS { multiresult }
FUNCTION {multi.page.check}
{ 't :=
  #0 'multiresult :=
    { multiresult not
      t empty$ not
      and
    }
    { t #1 #1 substring$
      duplicate$ "-" =
      swap$ duplicate$ "," =
      swap$ "+" =
      or or
        { #1 'multiresult := }
        { t #2 global.max$ substring$ 't := }
      if$
    }
  while$
  multiresult
}
FUNCTION {format.pages}
{ pages duplicate$ empty$ 'skip$
    { duplicate$ multi.page.check
        {
          bbl.pages swap$
          n.dashify
        }
        {
          bbl.page swap$
        }
      if$
      tie.or.space.prefix
      "pages" bibinfo.check
      * *
    }
  if$
}
FUNCTION {format.journal.pages}
{ pages duplicate$ empty$ 'pop$
    { swap$ duplicate$ empty$
        { pop$ pop$ format.pages }
        {
          ", " *
          swap$
          n.dashify
          pages multi.page.check
            'bbl.pages
            'bbl.page
          if$
          swap$ tie.or.space.prefix
          "pages" bibinfo.check
          * *
          *
        }
      if$
    }
  if$
}
FUNCTION {format.vol.num.pages}
{ volume field.or.null
  duplicate$ empty$ 'skip$
    {
      bbl.volume swap$ tie.or.space.prefix
      "volume" bibinfo.check
      * *
    }
  if$
  number "number" bibinfo.check duplicate$ empty$ 'skip$
    {
      swap$ duplicate$ empty$
        { "there's a number but no volume in " cite$ * warning$ }
        'skip$
      if$
      swap$
      ", " bbl.nr * number tie.or.space.prefix pop$ * swap$ *
    }
  if$ *
  format.journal.pages
}

FUNCTION {format.chapter.pages}
{ chapter empty$
    'format.pages
    { type empty$
        { bbl.chapter }
        { type "l" change.case$
          "type" bibinfo.check
        }
      if$
      chapter tie.or.space.prefix
      "chapter" bibinfo.check
      * *
      pages empty$
        'skip$
        { ", " * format.pages * }
      if$
    }
  if$
}

FUNCTION {format.booktitle}
{
  booktitle "booktitle" bibinfo.check
}
FUNCTION {format.series}
{
  series "series" bibinfo.check
}
FUNCTION {format.in.ed.booktitle}
{ format.booktitle duplicate$ empty$ 'skip$
    {
      editor "editor" format.names.ed duplicate$ empty$ 'pop$
        {
          " " *
          get.bbl.editor
          capitalize
          "(" swap$ * ") " *
          * swap$
          * }
      if$
      word.in swap$ *
    }
  if$
}
FUNCTION {format.in.ed.series}
{ format.series duplicate$ empty$ 'skip$
    {
      editor "editor" format.names.ed duplicate$ empty$ 'pop$
        {
          " " *
          get.bbl.editor
          capitalize
          "(" swap$ * ") " *
          * swap$
          * }
      if$
      word.in swap$ *
    }
  if$
}
FUNCTION {empty.misc.check}
{ author empty$ title empty$ howpublished empty$
  month empty$ year empty$ note empty$
  and and and and and
  key empty$ not and
    { "all relevant fields are empty in " cite$ * warning$ }
    'skip$
  if$
}
%FUNCTION {format.thesis.type}                original version
%{ type duplicate$ empty$
%    'pop$
%    { swap$ pop$
%      "t" change.case$ "type" bibinfo.check
%    }
%  if$
%}
FUNCTION {format.thesis.type}  % modiication by CHH: no change of case
{ type duplicate$ empty$
    'pop$
    { swap$ pop$
      "type" bibinfo.check
    }
  if$
}
FUNCTION {format.tr.number}
{ number "number" bibinfo.check
  type duplicate$ empty$
    { pop$ bbl.techrep }
    'skip$
  if$
  "type" bibinfo.check
  swap$ duplicate$ empty$
    { pop$ "t" change.case$ }
    { tie.or.space.prefix * * }
  if$
}
FUNCTION {format.article.crossref}
{
  key duplicate$ empty$
    { pop$
      journal duplicate$ empty$
        { "need key or journal for " cite$ * " to crossref " * crossref * warning$ }
        { "journal" bibinfo.check emphasize word.in swap$ * }
      if$
    }
    { word.in swap$ * " " *}
  if$
  " \cite{" * crossref * "}" *
}
FUNCTION {format.crossref.editor}
{ editor #1 "{vv~}{ll}" format.name$
  "editor" bibinfo.check
  editor num.names$ duplicate$
  #2 >
    { pop$
      "editor" bibinfo.check
      " " * bbl.etal
      *
    }
    { #2 <
        'skip$
        { editor #2 "{ff }{vv }{ll}{ jj}" format.name$ "others" =
            {
              "editor" bibinfo.check
              " " * bbl.etal
              *
            }
            {
             bbl.and space.word
              * editor #2 "{vv~}{ll}" format.name$
              "editor" bibinfo.check
              *
            }
          if$
        }
      if$
    }
  if$
}
FUNCTION {format.book.crossref}
{ volume duplicate$ empty$
    { "empty volume in " cite$ * "'s crossref of " * crossref * warning$
      pop$ word.in
    }
    { bbl.volume
      capitalize
      swap$ tie.or.space.prefix "volume" bibinfo.check * * bbl.of space.word *
    }
  if$
  editor empty$
  editor field.or.null author field.or.null =
  or
    { key empty$
        { series empty$
            { "need editor, key, or series for " cite$ * " to crossref " *
              crossref * warning$
              "" *
            }
            { series emphasize * }
          if$
        }
        { key * }
      if$
    }
    { format.crossref.editor * }
  if$
  " \cite{" * crossref * "}" *
}
FUNCTION {format.incoll.inproc.crossref}
{
  editor empty$
  editor field.or.null author field.or.null =
  or
    { key empty$
        { format.booktitle duplicate$ empty$
            { "need editor, key, or booktitle for " cite$ * " to crossref " *
              crossref * warning$
            }
            { word.in swap$ * }
          if$
        }
        { word.in key * " " *}
      if$
    }
    { word.in format.crossref.editor * " " *}
  if$
  " \cite{" * crossref * "}" *
}
FUNCTION {format.org.or.pub}
{ 't :=
  ""
  address empty$ t empty$ and
    'skip$
    {
      address "address" bibinfo.check *
      t empty$
        'skip$
        { address empty$
            'skip$
            { ": " * }
          if$
          t *
        }
      if$
    }
  if$
}
FUNCTION {format.publisher.address}
{ publisher "publisher" bibinfo.warn format.org.or.pub
}

FUNCTION {format.organization.address}
{ organization "organization" bibinfo.check format.org.or.pub
}

FUNCTION {article}
{ output.bibitem
  format.authors "author" output.check
  add.colon
  new.block
  format.title "title" output.check
  new.block
  crossref missing$
    {
      journal
      "journal" bibinfo.check
      "journal" output.check
      format.vol.num.pages output
      format.date "year" output.check
    }
    { format.article.crossref output.nonnull
      format.pages output
    }
  if$
  new.block
  format.note output
  fin.entry
}
FUNCTION {book}
{ output.bibitem
  author empty$
    { format.editors "author and editor" output.check
      add.colon
    }
    { format.authors output.nonnull
      add.colon
      crossref missing$
        { "author and editor" editor either.or.check }
        'skip$
      if$
    }
  if$
  new.block
  format.btitle "title" output.check
  crossref missing$
    { format.bvolume output
      new.block
      format.number.series output
      new.sentence
      format.publisher.address output
    }
    {
      new.block
      format.book.crossref output.nonnull
    }
  if$
  format.edition output
  format.date "year" output.check
  new.block
  format.note output
  fin.entry
}
FUNCTION {booklet}
{ output.bibitem
  format.authors output
  add.colon
  new.block
  format.title "title" output.check
  new.block
  howpublished "howpublished" bibinfo.check output
  address "address" bibinfo.check output
  format.date output
  new.block
  format.note output
  fin.entry
}

FUNCTION {inbook}
{ output.bibitem
  author empty$
    { format.editors "author and editor" output.check
      add.colon
    }
    { format.authors output.nonnull
      add.colon
      crossref missing$
        { "author and editor" editor either.or.check }
        'skip$
      if$
    }
  if$
  new.block
  format.btitle "title" output.check
  new.block
  crossref missing$
    {
	 	format.in.ed.series "series" output.check
      format.bvolume output
      format.chapter.pages "chapter and pages" output.check
      %new.block
      %format.number.series output
      new.sentence
      format.publisher.address output
    }
    {
      format.chapter.pages "chapter and pages" output.check
      new.block
      format.book.crossref output.nonnull
    }
  if$
  format.edition output
  format.date "year" output.check
  new.block
  format.note output
  fin.entry
}

FUNCTION {incollection}
{ output.bibitem
  format.authors "author" output.check
  add.colon
  new.block
  format.title "title" output.check
  new.block
  crossref missing$
    { format.in.ed.booktitle "booktitle" output.check
      format.bvolume output
      format.number.series output
      format.chapter.pages output
      new.sentence
      format.publisher.address output
      format.edition output
      format.date "year" output.check
    }
    { format.incoll.inproc.crossref output.nonnull
      format.chapter.pages output
    }
  if$
  new.block
  format.note output
  fin.entry
}
FUNCTION {inproceedings}
{ output.bibitem
  format.authors "author" output.check
  add.colon
  new.block
  format.title "title" output.check
  new.block
  crossref missing$
    { format.in.ed.booktitle "booktitle" output.check
      format.bvolume output
      format.number.series output
      format.pages output
      new.sentence
      publisher empty$
        { format.organization.address output }
        { organization "organization" bibinfo.check output
          format.publisher.address output
        }
      if$
      format.date "year" output.check
    }
    { format.incoll.inproc.crossref output.nonnull
      format.pages output
    }
  if$
  new.block
  format.note output
  fin.entry
}
FUNCTION {conference} { inproceedings }
FUNCTION {manual}
{ output.bibitem
  author empty$
    { organization "organization" bibinfo.check
      duplicate$ empty$ 'pop$
        { output
          address "address" bibinfo.check output
        }
      if$
    }
    { format.authors output.nonnull }
  if$
  add.colon
  new.block
  format.btitle "title" output.check
  author empty$
    { organization empty$
        {
          address new.block.checka
          address "address" bibinfo.check output
        }
        'skip$
      if$
    }
    {
      organization address new.block.checkb
      organization "organization" bibinfo.check output
      address "address" bibinfo.check output
    }
  if$
  format.edition output
  format.date output
  new.block
  format.note output
  fin.entry
}

FUNCTION {mastersthesis}
{ output.bibitem
  format.authors "author" output.check
  add.colon
  new.block
  format.btitle
  "title" output.check
  new.block
  bbl.mthesis format.thesis.type output.nonnull
  school "school" bibinfo.warn output
  address "address" bibinfo.check output
  format.date "year" output.check
  new.block
  format.note output
  fin.entry
}

FUNCTION {misc}
{ output.bibitem
  format.authors output
  add.colon
  title howpublished new.block.checkb
  format.title output
  howpublished new.block.checka
  howpublished "howpublished" bibinfo.check output
  format.date output
  new.block
  format.note output
  fin.entry
  empty.misc.check
}
FUNCTION {phdthesis}
{ output.bibitem
  format.authors "author" output.check
  add.colon
  new.block
  format.btitle
  "title" output.check
  new.block
  bbl.phdthesis format.thesis.type output.nonnull
  school "school" bibinfo.warn output
  address "address" bibinfo.check output
  format.date "year" output.check
  new.block
  format.note output
  fin.entry
}

FUNCTION {proceedings}
{ output.bibitem
  editor empty$
    { organization "organization" bibinfo.check output
    }
    { format.editors output.nonnull }
  if$
  add.colon
  new.block
  format.btitle "title" output.check
  format.bvolume output
  format.number.series output
  editor empty$
    { publisher empty$
        'skip$
        {
          new.sentence
          format.publisher.address output
        }
      if$
    }
    { publisher empty$
        {
          new.sentence
          format.organization.address output }
        {
          new.sentence
          organization "organization" bibinfo.check output
          format.publisher.address output
        }
      if$
     }
  if$
      format.date "year" output.check
  new.block
  format.note output
  fin.entry
}

FUNCTION {techreport}
{ output.bibitem
  format.authors "author" output.check
  add.colon
  new.block
  format.title
  "title" output.check
  new.block
  format.tr.number output.nonnull
  institution "institution" bibinfo.warn output
  address "address" bibinfo.check output
  format.date "year" output.check
  new.block
  format.note output
  fin.entry
}

FUNCTION {unpublished}
{ output.bibitem
  format.authors "author" output.check
  add.colon
  new.block
  format.title "title" output.check
  format.date output
  new.block
  format.note "note" output.check
  fin.entry
}

FUNCTION {default.type} { misc }
READ
FUNCTION {sortify}
{ purify$
  "l" change.case$
}
INTEGERS { len }
FUNCTION {chop.word}
{ 's :=
  'len :=
  s #1 len substring$ =
    { s len #1 + global.max$ substring$ }
    's
  if$
}
INTEGERS { et.al.char.used }
FUNCTION {initialize.et.al.char.used}
{ #0 'et.al.char.used :=
}
EXECUTE {initialize.et.al.char.used}
FUNCTION {format.lab.names}
{ 
	's :=
	s #1 "{vv{}}{ll}" format.name$
}

% Old version
%
%FUNCTION {format.lab.names2}
%{ 
%	's :=
%	s #1 "{vv{}}{ll}" format.name$
%	
%	s num.names$ #1 > 
%	{
%		s #2 "{vv{}}{ll}" format.name$
%		*
%	}
%	{}
%	if$
%	s num.names$ #2 > 
%	{
%		s #3 "{vv{}}{ll}" format.name$
%		*
%	}
%	{}
%	if$
%}

% New version by MB

FUNCTION {remove.spaces}					% function added by G. Schneider, 2016-10-18
{	'z :=
	""
	{ z empty$ not }
	{ z #1 #1 substring$
		z #2 global.max$ substring$ 'z :=
		duplicate$ "~" =
		'pop$
		{ duplicate$ " " =
			'pop$
			{ * }
			if$
		}
		if$
	}
	while$
}

FUNCTION {format.lab.names2}
{ 	's :=
	s #1 "{}{ll{}}" format.name$			% amendment by G. Schneider: "{}{ll}" --> "{}{ll{}}" (removes spaces, hyphens etc. in case of multiple surnames)
	remove.spaces								% amendment by G. Schneider: removes spaces when author is given in curled braces (e.g. a company name)
	s num.names$ duplicate$
	#3 >
	{ 
	  pop$
	  "EtAl" *
	}
	{ #2 <
		'skip$
		{  s #2 "{ff }{vv }{ll}{ jj}" format.name$ "others" =
			{ "EtAl" * }
			{ s #2 "{}{ll{}}" format.name$ remove.spaces * }			% same as in comments above
			if$
		}
		if$
	  	s num.names$ #3 <
		'skip$
		{  s #2 "{ff }{vv }{ll}{ jj}" format.name$ "others" =
			{ "EtAl" * }
			{ s #3 "{}{ll{}}" format.name$ remove.spaces * }			% same as in comments above
			if$
		}
		if$
	}
	if$
}

FUNCTION {author.key.label}
{ author empty$
	{ title empty$
     { key empty$
        { cite$ #1 #3 substring$ }
        { key #3 text.prefix$ }
      if$
     }
	  { title format.lab.names }
	  if$
	}
  { author format.lab.names2 }
  if$
}

FUNCTION {author.editor.key.label}
{ author empty$
    { editor empty$
        { key empty$
            { cite$ #1 #3 substring$ }
            { key #3 text.prefix$ }
          if$
        }
        { editor format.lab.names }
      if$
    }
    { author format.lab.names2 }
  if$
}

FUNCTION {author.key.organization.label}
{ author empty$
    { key empty$
        { organization empty$
            { cite$ #1 #3 substring$ }
            { "The " #4 organization chop.word #3 text.prefix$ }
          if$
        }
        { key #3 text.prefix$ }
      if$
    }
    { author format.lab.names2 }
  if$
}

FUNCTION {editor.key.organization.label}
{ editor empty$
    { key empty$
        { organization empty$
            { cite$ #1 #3 substring$ }
            { "The " #4 organization chop.word #3 text.prefix$ }
          if$
        }
        { key #3 text.prefix$ }
      if$
    }
    { editor format.lab.names }
  if$
}

FUNCTION {calc.label}
{ type$ "book" =
  type$ "inbook" =
  or
    'author.editor.key.label
    { type$ "proceedings" =
        'editor.key.organization.label
        { type$ "manual" =
            'author.key.organization.label
            'author.key.label
          if$
        }
      if$
    }
  if$
  duplicate$
  year field.or.null purify$ #-1 #2 substring$
  *
  'label :=
  year field.or.null purify$ #-1 #4 substring$
  *
  sortify 'sort.label :=
}
FUNCTION {sort.format.names}
{ 's :=
  #1 'nameptr :=
  ""
  s num.names$ 'numnames :=
  numnames 'namesleft :=
    { namesleft #0 > }
    { s nameptr
      "{vv{ } }{ll{ }}{  f{ }}{  jj{ }}"
      format.name$ 't :=
      nameptr #1 >
        {
          "   "  *
          namesleft #1 = t "others" = and
            { "zzzzz" * }
            { t sortify * }
          if$
        }
        { t sortify * }
      if$
      nameptr #1 + 'nameptr :=
      namesleft #1 - 'namesleft :=
    }
  while$
}

FUNCTION {sort.format.title}
{ 't :=
  "A " #2
    "An " #3
      "The " #4 t chop.word
    chop.word
  chop.word
  sortify
  #1 global.max$ substring$
}
FUNCTION {author.sort}
{ author empty$
    { key empty$
        { "to sort, need author or key in " cite$ * warning$
          ""
        }
        { key sortify }
      if$
    }
    { author sort.format.names }
  if$
}
FUNCTION {author.editor.sort}
{ author empty$
    { editor empty$
        { key empty$
            { "to sort, need author, editor, or key in " cite$ * warning$
              ""
            }
            { key sortify }
          if$
        }
        { editor sort.format.names }
      if$
    }
    { author sort.format.names }
  if$
}
FUNCTION {author.organization.sort}
{ author empty$
    { organization empty$
        { key empty$
            { "to sort, need author, organization, or key in " cite$ * warning$
              ""
            }
            { key sortify }
          if$
        }
        { "The " #4 organization chop.word sortify }
      if$
    }
    { author sort.format.names }
  if$
}
FUNCTION {editor.organization.sort}
{ editor empty$
    { organization empty$
        { key empty$
            { "to sort, need editor, organization, or key in " cite$ * warning$
              ""
            }
            { key sortify }
          if$
        }
        { "The " #4 organization chop.word sortify }
      if$
    }
    { editor sort.format.names }
  if$
}
FUNCTION {presort}
{ calc.label
  sort.label
  "    "
  *
  type$ "book" =
  type$ "inbook" =
  or
    'author.editor.sort
    { type$ "proceedings" =
        'editor.organization.sort
        { type$ "manual" =
            'author.organization.sort
            'author.sort
          if$
        }
      if$
    }
  if$
  *
  "    "
  *
  year field.or.null sortify
  *
  "    "
  *
  title field.or.null
  sort.format.title
  *
  #1 entry.max$ substring$
  'sort.key$ :=
}
ITERATE {presort}
SORT
STRINGS { longest.label last.sort.label next.extra }
INTEGERS { longest.label.width last.extra.num }
FUNCTION {initialize.longest.label}
{ "" 'longest.label :=
  #0 int.to.chr$ 'last.sort.label :=
  "" 'next.extra :=
  #0 'longest.label.width :=
  #0 'last.extra.num :=
}
FUNCTION {forward.pass}
{ last.sort.label sort.label =
    { last.extra.num #1 + 'last.extra.num :=
      last.extra.num int.to.chr$ 'extra.label :=
    }
    { "a" chr.to.int$ 'last.extra.num :=
      "" 'extra.label :=
      sort.label 'last.sort.label :=
    }
  if$
}
FUNCTION {reverse.pass}
{ next.extra "b" =
    { "a" 'extra.label := }
    'skip$
  if$
  label extra.label * 'label :=
  label width$ longest.label.width >
    { label 'longest.label :=
      label width$ 'longest.label.width :=
    }
    'skip$
  if$
  extra.label 'next.extra :=
}
EXECUTE {initialize.longest.label}
ITERATE {forward.pass}
REVERSE {reverse.pass}
FUNCTION {begin.bib}
{ et.al.char.used
    { "\newcommand{\etalchar}[1]{$^{#1}$}" write$ newline$ }
    'skip$
  if$
  preamble$ empty$
    'skip$
    { preamble$ write$ newline$ }
  if$
  % If you want the indentation to be as wide as the longest
  % label, uncomment the following line and comment the one
  % that follows
  %"\begin{thebibliography}{"  longest.label  * "}" *
  "\begin{thebibliography}{aber}"
  write$ newline$
}
EXECUTE {begin.bib}
EXECUTE {init.state.consts}
ITERATE {call.type$}
FUNCTION {end.bib}
{ newline$
  "\end{thebibliography}" write$ newline$
}
EXECUTE {end.bib}
%% End of customized bst file
