## 3. Background


### 3.1. History of Open Source Voting in San Francisco

To provide context to the recommendations in this document, this section
describes some of the history of the open source voting topic in San
Francisco government.

In May 2007, the [San Francisco Elections Commission][elections-commission]
passed a resolution that, among other things, established a policy that the
Department of Elections give priority to voting systems that “provide the
maximum level of security and transparency possible consistent with the
principles of public disclosure.” However, like today, no certified open
source voting systems were available at that time.

In December 2007 the City, through the Department of Elections, entered into
contract with Sequoia Voting Systems, Inc. for a new, proprietary voting
system. In June 2010, [Dominion Voting Systems,
Inc.](http://www.dominionvoting.com/) acquired Sequoia and assumed Sequoia's
contract. The Department and City extended the contract with Dominion more
than once. The current contract is scheduled to end at the end of 2018. The
total cost of the extended contract over the eleven years (including hardware
and hardware maintenance, software license fees, and election services) was
approximately $22 million, with $9.6 million of that up front. This averages
to around $2 million per year (see [this table][dominion-costs-2008] for an
annual breakdown).

In November 2008, the [Board of Supervisors][board-of-supervisors] passed an
[ordinance][bos-ordinance-vstf] creating a [Voting Systems Task Force][vstf]
(VSTF) to provide the City with recommendations on voting systems and related
matters, including “models for [the] development of a voting system including
proprietary, disclosed and open source software and hardware approaches.”

In June 2011, the VSTF issued its [final report][vstf-report],
“Recommendations on Voting Systems for the City and County of San Francisco”
(57 pages). Here are two excerpts from the recommendation text that mention
open source (from page 52):

> **2.5.4.3 Transparency, Source Code Disclosure, Licensing, and Contingency
Planning**
>
> 6\. The DOE should give strong preference to a voting system licensing
structure that gives San Francisco all of the rights provided by an
OSI-approved license, even if the system is maintained by an external party.
>
> ...
>
> 8\. San Francisco should be an active participant in the movement toward
more open and transparent voting systems. We acknowledge the complexity of
moving from the existing marketplace toward more innovative voting systems
and urge San Francisco to move steadily toward the goal of transparency—even
if it must do so in incremental steps.

In December 2014, the San Francisco Board of Supervisors unanimously passed a
[resolution][bos-open-source-voting-res] supporting the creation of open
source voting systems and requesting that the [San Francisco Local Agency
Formation Commission][lafco] (LAFCo) conduct a feasibility study. In October
2015, LAFCo issued its [final report][lafco-report], “Study on Open Source
Voting Systems” (37 pages).

In November 2015, the Elections Commission unanimously passed an [Open Source
Voting Systems Resolution][commission-resolutions] requesting that the Mayor
and Board of Supervisors initiate and fund a project to develop and certify
an open source voting system.

In August 2016, San Francisco Mayor Ed Lee
[signed][mayor-budget-press-release] the City and County of San Francisco’s
two-year budget for the 2016-2017 and 2017-2018 fiscal years. The budget
allocated $300,000 towards the planning phase of an open source voting system
project. Below are two excerpts from the [proposed budget
document][proposed-budget-2016] that reference the open source voting project.

The section for the Department of Elections references the project on pages
204-205:

> As the City's current voting system nears end-of-life, the proposed budget
includes $300,000 towards planning and development of a new voting system
based on open source software. If completed, San Francisco would be the first
City to do this. Development of an open source voting system would enable the
City to own the voting system's software and to have a choice of publicly
releasing it under open source license. Additionally, other jurisdictions as
well as the general people could use, participate, and improve the software.

The section for the [Committee on Information Technology][coit] (COIT)
includes the project as one of five highlighted projects out of twenty-four,
alongside initiatives like the City's new [Digital
Services][sf-digital-services] Team, cybersecurity, and improving the City's
network (pages 447-448):

> ANNUAL PROJECTS
>
> ...
>
> Over the two-year period, the proposed budget recommends $15.7 million of
General Fund COIT allocation to support 24 projects. Below are a few
highlighted projects.
>
> ...
>
> OPEN SOURCE VOTING SYSTEM
>
> As the City’s current voting system is aging, the Department of Elections
is exploring an opportunity to develop a new voting system based on open
source software. If completed, San Francisco would be the first city to do
this. Development of an open source voting system would enable the City to
own the voting system’s software and have a choice of publicly releasing it
under an open source license. Additionally, other jurisdictions as well as
the general public could use and improve the software. The proposed budget
supports initial project planning and scoping of this project.

In April 2017, the Board of Supervisors approved the City’s fourth Five-Year
[Information & Communication Technology (ICT) Plan for Fiscal Years 2018-22][ict-plan-2008].
The plan included the open source voting system project among four major IT
projects under consideration for the future, alongside projects like
Universal Broadband and Voice over Internet Protocol (VoIP). For example, on
page 11:

> However, several future projects are currently being scoped out as
potentially the City’s next Major IT Project, including:
>
> ...
>
> **Voting System Replacement:** The Department of Elections is currently
investigating alternative voting systems, including the possibility of
building an open source system.

And on page 53:

> **Future Major IT Projects**
>
> In addition, the City has begun investigating what may become the next major
technology project. Before beginning any new technology venture, the City
recommends extensive planning and scoping to better understand the true cost
of any new technology. The City has begun evaluating various different
projects that may be considered as major investments, which include:
>
> ...
>
> **Voting System Replacement:** The City’s current voting system license is
set to expire in 2018. Without a long-term contract in place, the City has an
opportunity to pursue alternative voting systems that could promote
transparency and more security. The City is currently investigating
alternative options, including the possibility of building an open source
system.

In April 2017, the Elections Commission voted to create an [Open Source Voting
System Technical Advisory Committee][commission-osvtac] to “provide technical guidance, ideas,
and support to the Elections Commission (’Commission’) on ways to improve and
help ensure the success of the City and County of San Francisco's open source
voting system project.” The Commission voted on the Committee's initial
membership at its May meeting. The Committee was fully constituted on June 2,
2017, when the appointment of the fifth member was made final.

In May 2017, the Department of Elections [issued an
RFP][rfp-business-case-pdf] (REG RFP #2017‑01)
for a contractor to “prepare a business case for developing an accessible,
open source voting system.” The RFP would use a portion of the $300,000
budgeted in August 2016. In September 2017, Slalom was selected as the
winning bidder. Slalom's deliverable will be due in January 2018, and it
will inform the City's next budget process, which will begin around that time.
See here for [Slalom's RFP response][slalom-rfp-response], the City's
[contract][slalom-contract] with Slalom, and
[Appendix A][slalom-contract-appendix-a] and
[Appendix B][slalom-contract-appendix-b] of the contract.

The Department of Elections' contract for its current voting system expires
at the end of December 2018. The Director of Elections is aiming to lease an
interim system from that point forward that can be used while an open source
voting system is developed and certified. The RFP for the interim system may
be issued as early as the fall of 2017.


### 3.2. Voting System


#### 3.2.1. Definition

The [Help America Vote Act][hava] (HAVA) of 2002 defines a voting system as
follows (from 52 USC §21081: Voting systems standards):

    (b) Voting system defined
     In this section, the term "voting system" means—
     (1) the total combination of mechanical, electromechanical,
      or electronic equipment (including the software, firmware,
      and documentation required to program, control, and support
      the equipment) that is used—
      (A) to define ballots;
      (B) to cast and count votes;
      (C) to report or display election results; and
      (D) to maintain and produce any audit trail information; and
     (2) the practices and associated documentation used—
      (A) to identify system components and versions of such
       components;
      (B) to test the system during its development and maintenance;
      (C) to maintain records of system errors and defects;
      (D) to determine specific system changes to be made to a system
       after the initial qualification of the system; and
      (E) to make available any materials to the voter (such as
       notices, instructions, forms, or paper ballots).

[hava]: https://www.eac.gov/about/help-america-vote-act/


### 3.3. Other Voting System Projects

This section includes information about some of the other voting system
projects that are either (1) open source and have been or plan to be used in
a US jurisdiction, or (2) are or were being developed by a jurisdiction in
the US.

Special attention is paid in this section towards whether the various
projects are open source because that determines whether and to what extent
the source code will be available for use in San Francisco's project.


#### 3.3.1. New Hampshire - Prime III

[TODO]


#### 3.3.2. Los Angeles County - VSAP

Los Angeles County has been planning or working on its [Voting Systems
Assessment Project][la-vsap] (VSAP) at least since 2009, when
it held an event at Caltech on September 16, 2009. VSAP is a project for Los
Angeles County to develop its own voting system using a “voter-centered
approach.“ The project is led by Los Angeles County Registrar-Recorder/County
Clerk (RR/CC) Dean Logan.

There is conflicting evidence as to whether any of the VSAP system will be
open source and, if so, how much. On the one hand, press coverage of the
project frequently mentions that the system will be open source, and Mr.
Logan says it will be open source when he speaks publicly and is quoted in
the media. For example, in [this
tweet](https://twitter.com/LACountyRRCC/status/904871828799209472) he says,
“Encouraging to see movement in this direction. #LACounty advances
#opensource in #votingmodernization effort too.“

Los Angeles County's April 24, 2017 [VSAP RFI #17-001][la-vsap-rfi] also supports the
view that it will be open source. For example, on page 24, it says:

> Accordingly, RR/CC is considering a Copyleft type of license such as GNU
General Public License (GPL) or OSET Public License (OPL), that promotes
“forever free” provisions, however it has not ruled out the use of more
“permissive” open source licenses, such as the Mozilla Public License Version
2.0 (MPL), the Apache License, Version 2.0 (ALv2), the BSD 3.0 or MIT
licenses. Whatever the chosen license, the transparency and ability to share
the IP and the technology would need to be ensured.
> ...
> LA County is seeking candid feedback from the vendor community on the
intellectual property approach for VSAP.

On the other hand, there is no obvious mention of open source on VSAP's main
website (e.g. on its [“Principles“](http://vsap.lavote.net/principles/)
page). Moreover, Los Angeles County's 54-page [RFP Phase 1: #17-008][la-vsap-rfp-phase-1],
which was issued five months after the RFI on September 18, 2017 to
prequalify vendors, does not mention open source. The Phase 1 RFP also
describes a new “Tally System“ the County is working on:

> A new Tally System is required to capture and process ballot images so that
vote selections on paper ballots can be digitally counted. This includes
votes cast on BMD ballots at Vote Centers, as well as on Vote By Mail
ballots. Similar to the ECBMS, RR/CC is currently developing the software
required for the new Tally System in anticipation of a pilot in June 2018.

Los Angeles County submitted its VSAP Tally Version 1.0 to the California
Secretary of State for certification on September 19, 2017.  See their
application for approval [here][la-vsap-application-tally] (PDF, 21 pages).

However, even though the County is developing the Tally System and submitted
it for certification, as
of October 2017, none of the code for the Tally System appears to be publicly
available, let alone open source. In addition, on page 41 of the RFP in
Section 6.2 “Non-Disclosure Agreement,“ the RFP says—

> Prime Contractor-Led Teams who are prequalified as a result of this RFP
Phase 1 will be required to sign a Non-Disclosure Agreement (NDA) as part of
RFP Phase 2 prior to receiving County IP.

The requirement to sign an NDA seems inconsistent with the technology being
open source.

Finally, in response to an October 5 question on Twitter about whether
VSAP will be open source, Mr. Logan [replied](https://twitter.com/LACountyRRCC/status/916114599241330689):

> Open source platform for UI and tally; publicly owned design specs and
code. More detail in RFI docs at http://vsap.lavote.net

And in a [second reply](https://twitter.com/LACountyRRCC/status/916381787605000192):

> Tally stack is all open source; details of licensing for custom code will
be in Phase II RFP & was discussed in RFI; all publicly owned.

So if “platform“ and “stack“ refer to things like the operating system,
database, programming language, etc. but not the code itself, it seems
possible that none of the code will be open source but instead simply be
“publicly owned.“ It would be helpful if Los Angeles County can provide a
clearer guarantee if this interpretation isn't correct.


#### 3.3.3. Travis County, Texas - STAR-Vote™

In 2012, Travis County, Texas started researching and designing a new voting
system it called STAR-Vote™. The County spent over $330,000 in its research
and design phase.

In October 2016, Travis County issued a detailed 208-page [RFP][star-vote-rfp]
covering the first phase of STAR-Vote, which was the “in-person voting
module of the STAR-Vote system.“ The RFP made frequent reference to open
source software. For example, on page 5:

> The STAR-Vote system requirements were developed from the ground up with
the purpose, among other objectives, of specifying an entire voting system
developed under the open source code software model.

However, the commitment to open source seemed uncertain because the RFP said
the code would start out not as open source but as disclosed source,
and possibly be made open source later. For example, on page 37 (note the
phrase, “with a view toward ultimately ...“):

> Source code for all modules would be published, but usage rights for actual
elections as well as derivative rights (as in using the code to create a
derivative voting system) would be controlled by Travis County (and/or
consortium) with a view toward ultimately releasing usage and derivative
rights under a “suitable” (as determined by Travis County and/or consortium)
open source license that would allow and encourage preparation of third-party
derivative work, recognizing that voting systems must be state and federally
certified;

The RFP was accompanied by an additional 16-page [“Statement of Intent“][star-vote-entity]
document, which sought $25 million (initially a minimum of
$15 million) for an entity (likely a non-profit) called the “STAR-Vote
Entity.“

On September 28, 2017, Travis County announced via a [press
release][star-vote-final-press-release] that the County would not be pursuing
STAR-Vote. From their [Final Report][star-vote-final-report] (6 pages)--

> In a nutshell, we have run into too many obstacles. There has not been
enough funding, time, or support to bring STAR-Vote into the phase of being a
start-up, through development and the legally-required certification process
and then into use.


### 3.4. Resources

This section contains links to other resources and documents that may be
useful for the project.


#### 3.4.1. San Francisco

   * The San Francisco Department of Elections' [planning phase
     RFP][rfp-business-case-pdf] (REG RFP #2017‑01, "Preparing a Business
     Case for Developing an Accessible, Open Source Voting System"). In
     particular, see the list of links in Section I.A. starting on page 5.
   * [San Francisco Digital Services Team][sf-digital-services]


#### 3.4.2. Procurement

   * U.S. Digital Services' [TechFAR Handbook][techfar-handbook]
   * 18F's [Modular Contracting][18f-modular-contracting] page


#### 3.4.3. Related Software Projects for US Government Elections

   * [ColoradoRLA][colorado-rla-home], (Risk Limiting Audit) Project. Colorado Secretary of State.
     Software to upload electronic CVRs (cast-vote-records), randomly
     select ballots to audit, then hand check hand selected paper ballots
     against stored CVRs or re-scanned paper ballots.

     Contractor for open source software is [Free & Fair][free-and-fair]
     git: [ColoradoRLA][colorado-rla-repo], [OpenRLA][open-rla-repo].

     OpenCount now from Free & Fair \[[git][open-count]\] is software to
     tabulate scanned ballots, used with RLA when original systems
     do not store CVRs. \[[Presentation][open-count-pres]\].

   * [Voting Systems Assessment Project][la-vsap] (VSAP), Los Angeles County
     Voting station design with tablet and printer-scanner. Blank ballot sheets
     are inserted into printer-scanner, tablet used to make selections,
     printer emits printed and marked ballot for review, scanner records
     and feeds into collection box. Smartphone app allows pre-recorded
     votes to be entered via QR code. Soliciting vendors for implementation.

   * [Prime III][prime-iii], Dr. Juan E. Gilbert (now hosted at University of Florida)
     Tablet with docking station with keyboard and laser printer, open software.
     Allows home computer or phone to prepare QR code.
     \[[Video Demo][prime-iii-video]\] \[[Online Demo][prime-iii-demo]\]
     \[[git][prime-iii-repo]\]

     Used by NH in 2016 for accessible voting (ballot marking device) statewide.
     NH revised version is known as [one4all][one4all-vvf]
     (no known source code location). Can print OCR ballot or mark
     ovals on preprinted ballot. A [slide presentation ][one4all-ppt]
     describes the hardware (windows tablet, keyboard, and printer).
     Videos: \[[Demo][one4all-demo]\], \[[How to Use][one4all-howto]\],
     \[[Setup Instructions][one4all-setup]\].
     The Secretary of State, William Gardner, sent a [letter][one4all-ltr]
     to [CAVO][cavo] describing the program.

     _[Item edited: Feb. 8, 2018 meeting.]_

   * [STAR-Vote][star-vote-usenix], Travis County, TX
     PDF paper and slides for presentation on Travis County TX proposed system.
     Uses off the shelf tablet to produce printed ballot with only choices
     made. Scanner only reads IDs of ballots placed in box to record which
     ballots printed are cast. Electronic records separate. (No mail ballots.)
     Voters can check receipt with QR code.
     [Demo/prototype implementation by Free & Fair][star-vote-faf-repo].


#### 3.4.4. Other Open Source Voting Projects and Research

   * [Pvote][pvote], a model for an open source voting application where
     sensitive software is minimized-- 460 lines of python code, audited
     in a security review.

   * [VoteBox][votebox], a prototype electronic voting machine based on
     COTS hardware. Several technical publications are available with
     detailed descriptions of the system components.

   * [Low Error Voting Interface][levi] (LEVI), research paper of a voting
     machine GUI designed to reduce user errors. Used by Prime-III.

_[Subsection added: Jan. 18, 2018 meeting.]_


#### 3.4.5. Open Source Voting Organization

   * [OSET Foundation][oset-foundation] 501c umbrella nonprofit to support [Trust the Vote][trust-the-vote],
     site with actual software. \[Currently, mostly Ruby-On-Rails in ruby
     using IEEE 1622 data models.\]

     Useful diagrams of voting software architecture: ([PDF][oset-arch-pdf], [broken interactive HTML][oset-arch-html]),
     Simpler [diagram of modules][oset-modules].

     Prototype of [VoteStream][trust-the-vote-votestream] election results display.

   * [Open Voting Consortium][open-voting-consortium] Inactive (since 2011)
     prior effort to develop open source software. Efforts moved to CAVO.
     A demo implementation was created and
     [technical paper][open-voting-consortium-usenix-paper] with a
     detailed description of the system using COTS hardware.

     _[Item edited: Jan. 18, 2018 meeting.]_

   * [California Association of Voting Officials][cavo] (CAVO)
     Nonprofit organization to promote open source voting. Election officials
     from several California counties are members, as well as other groups.

   * [Verified Voting Foundation][verified-voting-foundation],
     nonprofit to provide resources on election systems and equipment.
     Has links and information on voting equipment and usage across the US.


#### 3.4.6. Election Data Standards & Organizations

   * [Voluntary Voting System Guidelines][eac-vvsg] (VVSG). In January 2016,
     the [U.S. Election Assistance Commission][eac] (EAC) adopted a plan
     where, starting in July 2017, all new voting systems would be required
     to be tested against the Voluntary Voting System Guidelines Version 1.1
     (VVSG 1.1). The EAC approved the VVSG 1.1 in March 2015.

     The EAC was established by the Help America Vote Act of 2002 (HAVA) to
     develop guidance on HAVA requirements. The EAC works with NIST to
     sponsor Technical Guidelines Development Committee (TGDC) working groups
     for newer versions of the VVSG.

     _[Item edited: Dec. 14, 2017 meeting.]_

   * Election Markup Language (EML), Original XML-based election data interchange format.
     [Wikipedia Overview][eml-wikipedia], [Specifications][eml-specs]. \[2011\] (Obsolete)

   * [IEEE VSSC/1622: Common Data Format for Election Equipment][ieee-1622]
     (Institute of Electrical and Electronic Engineers), Voting Systems
     Standards Committee). Based on EML, Superceeded by NIST SP1500.

   * [NIST SP1500-10x Voting Common Data Format][nist-voting] standards.
     Ongoing effort on XML standards for interoperable election information.
     From the [NIST Voting section of the Information Technology Laboratory][nist-itl].
     Coordinating and funded by EAC to produce new *Voluntary Voting Systems Guidelines*.

     Includes a good [VVSG Principles and Guidelines][nist-vvsg-principles] summary.

   * [Voting Information Project][vip-project] Google/Pew effort to develop
     election data interchange standards, originally based on EML.
     Project includes collecting data from election officials nationwide.
     Used for Google's Civic API and third parties using Civic API.
     In 2016, California Secretary of State collected data from all CA counties.
     \[2016 original contributed data is not public/open--
     private to Google/Pew except by special arrangement.\]
     The VIP spec allows contest definitions, but in practice,
     only used for poll lookup. [git][vip-repo]


#### 3.4.7. California Election Laws and Regulations

   * [Advisories to County Election Officials][sos-advisories], announcements
     from the California Secretary of State on new regulations, required
     procedures, and notices on statewide propositions and elected offices.
     Includes certifications of new equipment including remote accessible
     vote by mail.

   * [Elections Officers Digest][sos-digest], an annotated summary of election
     laws prepared for local election officials, with procedures,
     responsibilites and definitions of terms.
     Includes references to code sections.

_[Subsection added: Jan. 18, 2018 meeting.]_


#### 3.4.8. Additional Links

   * [GitHub][github]
   * [Open Source Initiative][osi] (OSI)
   * [OpenCount][open-count]
