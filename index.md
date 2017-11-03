# Open Source Voting System Project Recommendations

(Approved by OSVTAC on September 21, 2017.)

Last update: September 29, 2017 (2nd update)

**Note: these recommendations are a work in progress and not yet complete.**

This document contains the recommendations of San Francisco's [Open Source
Voting System Technical Advisory Committee][osvtac] (OSVTAC, or TAC) for
the City and County of San Francisco's open source voting system project, as
of the version date that appears above.

The committee started this document on August 30, 2017 and will continue to
work on it over time. Substantive updates to this document occur by a vote of
the committee at a committee meeting. Meetings occur approximately once a
month.

To learn more about the committee, visit the committee's website at
[https://osvtac.github.io][osvtac]. To learn how to suggest changes to this
document, view the "Project Recommendations" section of the [About
page][osvtac-about-recs] of the committee's website.


## Contents

* [1. Goals](#1-goals)
  * [1.1. Scope](#11-scope)
  * [1.2. Priorities](#12-priorities)
  * [1.3. Non-goals](#13-non-goals)
* [2. Background](#2-background)
  * [2.1. History of Open Source Voting](#21-history-of-open-source-voting)
  * [2.2. Voting System](#22-voting-system)
* [3. Assumptions](#3-assumptions)
* [4. Resources](#4-resources)
* [5. Recommendations](#5-recommendations)
  * [5.1. Interim Voting System](#51-interim-voting-system)
  * [5.2. Incremental Approach](#52-incremental-approach)
  * [5.3. Requirements-gathering](#53-requirements-gathering)
  * [5.4. Requirements](#54-requirements)
  * [5.5. Project Management](#55-project-management)
  * [5.6. Open Source](#56-open-source)
  * [5.7. Procurement](#57-procurement)
  * [5.8. Software architecture and design](#58-software-architecture-and-design)
  * [5.9. Software development](#59-software-development)
  * [5.10. Hardware design](#510-hardware-design)
  * [5.11. Documentation](#511-documentation)
  * [5.12. Security](#512-security)
  * [5.13. Testing](#513-testing)
  * [5.14. Certification](#514-certification)
  * [5.15. Hardware manufacturing or assembly](#515-hardware-manufacturing-or-assembly)
  * [5.16. Deployment](#516-deployment)
  * [5.17. Software maintenance](#517-software-maintenance)
  * [5.18. Hardware maintenance](#518-hardware-maintenance)


## 1. Goals

This section discusses the goals, scope, and priorities of this document and
the Committee.

The TAC’s Bylaws say that the TAC’s purpose is to “provide technical
guidance, ideas, and support to the Elections Commission on ways to improve
and help ensure the success of the City and County of San Francisco's open
source voting system project.” The focus of TAC's effort will be on
establishing parameters and recommendations to guide the future development
of the voting system.

The TAC will draw on its technical expertise, the expertise of other members
in the community, and from similar efforts (including other open source
voting efforts) to provide guidance in areas including but not limited to
open source, requirements-gathering, design, architecture, development,
documentation, security, testing, certification, manufacturing, deployment,
system maintenance, strategies for procurement, and project management.


### 1.1. Scope

* This document will limit itself to current laws that San Francisco must
  satisfy, or to changes in law that San Francisco anticipates (e.g. possibly
  transitioning to the “vote center” model allowed by [SB
  450][bill-sb-450-2015] of 2015-2016). In particular, the document will
  restrict itself to considering paper-ballot systems.

* For the purposes of this document, “voting system” includes anything that
  is currently the responsibility of the voting system in use today.
  Responsibilities of a voting system include allowing voters to mark ballots
  (if not using pen and paper), counting ballots, reporting election
  results, and ensuring the integrity of the process.
  In addition, it may include ballot design and layout, as well as
  the functionality of a “remote accessible vote by mail system” as described
  in [AB 2252][bill-ab-2252-2015] (2015-2016). It should also facilitate
  auditing the results of an election. The responsibilities of a voting
  system do not include the responsibilities of a voter registration system.
  The voting system may need to interoperate with the Department’s election
  management system (EMS). If the ballots
  are pre-printed, the voting system need not be capable of printing ballots.


### 1.2. Priorities

* This document should prioritize high-level recommendations over low-level
  recommendations.

* This document should prioritize recommendations that are needed sooner
  rather than later.


### 1.3. Non-goals

* The Committee will not be designing or developing a voting system.

* The Committee will not be drafting detailed, low-level specs that the
  voting system should satisfy.

* The Committee will not be drafting an exhaustive list of requirements.

* The Committee will not make explicit attempts to accommodate internet
  voting in any form, nor voting methods not used in San Francisco. This does
  not preclude the Committee from recommending software designs or practices
  that could make such things easier to accommodate as a side effect.

* The Committee's recommendations will prioritize the voting system needs of
  San Francisco without emphasizing the needs of other jurisdictions.
  The needs of other
  jurisdictions will be considered insofar as it could help to develop and
  certify a system for use in San Francisco sooner (for example, if San
  Francisco were to collaborate with another jurisdiction and share costs).
  However, as stated in the previous point, this does not preclude
  recommending designs and practices that could make it easier to accommodate
  other jurisdictions.


## 2. Background


### 2.1. History of Open Source Voting

To provide context to the recommendations in this document, this section
describes some of the history of the open source voting topic in San
Francisco government.

In May 2007, the [San Francisco Elections Commission][elections-commission]
passed a resolution that, among other things, established a policy that the
Department of Elections give priority to voting systems that “provide the
maximum level of security and transparency possible consistent with the
principles of public disclosure.” However, like today, no certified open
source voting systems were available at that time. In December 2007, the
Department signed a contract for a new voting system that was proprietary.
The Department still uses this system today. The contract for this system
ends at the end of 2018.

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
building an open-source system.

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
alternative options, including the possibility of building an open-source
system.

In April 2017, the Elections Commission voted to create an [Open Source Voting
System Technical Advisory Committee][commission-osvtac] to “provide technical guidance, ideas,
and support to the Elections Commission (’Commission’) on ways to improve and
help ensure the success of the City and County of San Francisco's open source
voting system project.” The Commission voted on the Committee's initial
membership at its May meeting. The Committee was fully constituted on June 2,
2017, when the appointment of the fifth member was made final.

In May 2017, the Department of Elections [issued an RFP][rfp-business-case-page]
for a contractor to “prepare a business case for developing an accessible,
open source voting system.” The RFP would use a portion of the $300,000
budgeted in August 2016. The contractor's deliverable will be due in January
2018, and it will inform the City's next budget process, which will begin
around that time.

The Department of Elections' contract for its current voting system expires
at the end of December 2018. The Director of Elections is aiming to lease an
interim system from that point forward that can be used while an open source
voting system is developed and certified. The RFP for the interim system may
be issued as early as the fall of 2017.


### 2.2. Voting System


#### 2.2.1. Definition

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


#### 2.2.2. Components

This section provides one possible way of listing the components of a
“generic” optical-scan paper-ballot voting system. This list is not rigorous
or exhaustive. Rather, it is meant for discussion purposes and to provide a
sense of what functionalities are needed and how they are divided up, etc.

For simplicity, we assume that the voting system uses pre-printed ballots, as
opposed to being a ballot on-demand system. We also assume that in-precinct
voters are allowed to mark their ballot with a pen, as opposed to being
required to interact with an electronic device. Finally, we assume the voting
system includes a precinct tally, which means the system tallies the
in-precinct ballots at the precinct.

The assumptions above are only for the purposes of the example illustration
in this section. They should not be construed in any way as recommendations
of the Committee or to constrain the type of voting system that San Francisco
should develop.

The components in this particular list are not necessarily independent. They
may overlap or contain one another. For example, the precinct ballot scanner
hardware component contains a scanner device driver, the ballot image
interpreter, and the high-level scanner software components.

Finally, note that there are many possible ways to divide a given voting
system into components. For example, the granularity at which one views the
system affects the number of components. We chose a mid-level granularity for
this list. This lets us show how some software components are used in more
than one hardware component. Differences can also result from where the
“boundaries” are drawn between components (e.g. what functionalities one
assigns to different components).


##### 2.2.2.1. Hardware Components

Each of the hardware components below also needs software to function. In
most cases, we list this software in the “Software Components” section.

**1\. Accessible Ballot-Marking Device**

A device used in polling places that lets people with disabilities vote
independently. It supports different accessible interfaces like audio,
sip-and-puff, etc. If the computer is COTS, it may also need a custom casing
or shell to increase durability and assist with polling-place transport and
setup.

**2\. Central Ballot Scanner**

A device responsible for high-speed, high-volume ballot scanning (e.g. for
vote-by-mail ballots). The scanning with these machines is done in a
controlled environment under staff supervision.

**3\. Precinct Ballot Scanner**

A device used in polling places to scan and tabulate ballots cast in person.
It has features like returning the ballot to the voter for possible
correction if the ballot contains an overvote. Similar to the accessible
device, this device may also need a custom casing or shell for durability and
to facilitate polling-place use.

**4\. Standard laptop or desktop computers**

Standard computers will also be needed for administrative tasks like ballot
layout, adjudicating digital images of ballots, aggregating and totaling
votes, and generating results reports.


##### 2.2.2.2. Software Components

**1\. Voting System Database / Management**

Central store (e.g. file system and/or database) storing and providing access
to the voting-system information needed to conduct an election. This can
include things like contest and ballot definitions, ballot images, cast vote
records, and election results. A management interface can let staff perform
tasks like import and export data in open data formats, digitally evaluate
"out-stacked" ballots and ballots with write-in candidates, and perform other
functions needed during the canvass. This software may support running other
software components like EMS integration, tabulation, and results reporting.

**2\. Election Definition EMS Integration.**

Interfaces with the Department's Election Management System (EMS) to import
and convert election definition information from the EMS into the voting
system database. This can include things like what offices, candidates, and
measures, etc. are in the election and in what precincts and districts, etc.

**3\. Ballot Layout**

This is a software application that lets staff generate paper-ballot layouts
from the election definition for each ballot type in automated or
semi-automated fashion, including support for multiple languages.

**4\. Accessible Ballot-Marking Device Software**

This is the software corresponding to the Accessible Ballot-Marking Device
hardware component.

**5\. Ballot Image Interpreter**

This is a software library responsible for interpreting ballot images. It
generates a cast vote record (CVR) from a digital image of a ballot. This
software component could potentially be used in all of the precinct scanners,
the central scanners, and a software-only ballot adjudication application.

**6\. Scanner Device Drivers (one for precinct and one for central)**

This is low-level software needed on both precinct and central ballot
scanners that provides a software API to the basic hardware functionality of
a ballot scanner (e.g. out-stacking a ballot, returning a ballot, advancing a
ballot, etc.). This might come with COTS hardware. Separate versions are
likely needed for the precinct and central scanners.

**7\. High-level Scanner Software (one for precinct and one for central)**

This is high-level software controlling the precinct and central ballot
scanners. It interacts with the scanner device driver and ballot image
interpreter components and is responsible for things like scanning and
storing ballot images, detecting the ballot layout, interpreting and
tabulating ballot markings, controlling the scanner in response to the
markings on a ballot, and exporting ballot data after scanning is complete.
Separate versions are likely needed for the precinct and central scanners.

**8\. Vote Totaler**

Aggregates and counts all vote totals and generates the results in an open
data format. Includes the RCV tabulation algorithm.

**9\. Results Reporter**

Generates human-readable results reports from the results data from the vote
totaler (e.g. printable results and results posted on the Department website).


## 3. Assumptions

This section lists certain assumptions the committee has made while drafting
this document.

* The Department of Elections does not have the expertise to conduct the
  day-to-day management of the development and certification of an open
  source voting system.
* The Department of Elections has [expressed a
  preference][directors-report-march-2017] for the GNU General Public License
  version 3 (GPLv3). This is consistent with the copyleft preference stated
  in the Elections Commission’s Open Source Voting Systems Resolution

[directors-report-march-2017]: http://sfgov.org/electionscommission/sites/default/files/Documents/meetings/2017/2017-03-15-commission/March%202017%20Director%20Report.pdf


## 4. Resources

This section contains links to other resources and documents that may be
useful for the project.

1. San Francisco
   * The San Francisco Department of Elections' RFP for the planning phase:
     [REG RFP #2017‑01][rfp-business-case-page] ("Preparing a Business Case
     for Developing an Accessible, Open Source Voting System"). In
     particular, see the list of links in Section I.A. starting on page 5 of
     the [RFP PDF][rfp-business-case-pdf].

2. Procurement
   * U.S. Digital Services' [TechFAR Handbook][techfar-handbook]
   * 18F's [Modular Contracting][18f-modular-contracting] page

3. Related Software Projects for US Government Elections
   * [ColoradoRLA][colorado-rla-home], (Risk Limiting Audit) Project. Colorado Secretary of State.
     Software to upload electronic CVRs (cast-vote-records), randomly
     select ballots to audit, then hand check hand selected paper ballots
     against stored CVRs or re-scanned paper ballots.

     Contractor for open-source software is [Free & Fair][free-and-fair]
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
     Used by NH in 2016 for accessible voting (ballot marking device). Allows
     home computer or phone to prepare QR code. \[[git][prime-iii-repo]\]

   * [STAR-Vote][star-vote], Travis County, TX
     PDF paper and slides for presentation on Travis County TX proposed system.
     Uses off the shelf tablet to produce printed ballot with only choices
     made. Scanner only reads IDs of ballots placed in box to record which
     ballots printed are cast. Electronic records separate. (No mail ballots.)
     Voters can check receipt with QR code.
     [Demo/prototype implementation by Free & Fair][prime-iii-faf-repo].

4. Open Source Voting Organizations
   * [OSET Foundation][oset-foundation] 501c umbrella nonprofit to support [Trust the Vote][trust-the-vote],
     site with actual software. \[Currently, mostly Ruby-On-Rails in ruby
     using IEEE 1622 data models.\]

     Useful diagrams of voting software architecture: ([PDF][oset-arch-pdf], [broken interactive HTML][oset-arch-html]),
     Simpler [diagram of modules][oset-modules].

   * [Open Voting Consortium][open-voting-consortium] Inactive (since 2011)
     prior effort to develop open source software. Efforts moved to CAVO.

   * [California Association of Voting Officials][cavo] (CAVO)
     Nonprofit organization to promote open source voting. Election officials
     from several California counties are members, as well as other groups.

   * [Verified Voting Foundation][verified-voting-foundation],
     nonprofit to provide resources on election systems and equipment.
     Has links and information on voting equipment and usage across the US.

5. Election Data Standards & Organizations
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

   * [Election Assistance Commission][eac] established by the
     Help America Vote Act of 2002 (HAVA) to develop guidance on HAVA
     requirements. Works with NIST to sponsor Technical Guidelines
     Development Committee (TGDC) working groups.
     Result will be [Voluntary Voting Systems Guidelines][eac-vvsg].
     Also works to implement Military and Overseas Voting.

   * [Voting Information Project][vip-project] Google/Pew effort to develop
     election data interchange standards, originally based on EML.
     Project includes collecting data from election officials nationwide.
     Used for Google's Civic API and third parties using Civic API.
     In 2016, California Secretary of State collected data from all CA counties.
     \[2016 original contributed data is not public/open--
     private to Google/Pew except by special arrangement.\]
     The VIP spec allows contest definitions, but in practice,
     only used for poll lookup. [git][vip-repo]

6. Additional Links
   * [GitHub][github]
   * [Open Source Initiative][osi] (OSI)
   * [OpenCount][open-count]


## 5. Recommendations


### 5.1. Interim Voting System

* The contract for the interim system (i.e. the system to be used after 2018)
  should permit all possible combinations of phasing in an open-source system
  alongside it. Examples of possible combinations include:

  * using open-source components to scan vote-by-mail ballots and the interim
    system to scan precinct ballots, or vice versa;

  * using an open-source accessible voting device in conjunction with the
    interim system’s precinct-based scanner, or vice versa;

  * scanning the ballots of the interim system using an open-source scanner;

  * tabulating ballots scanned by an open-source scanner using the interim
    system’s tabulation software;

  * using an open-source reporting and/or tabulation system with the output
    from the interim system’s scanners;

  * using open-source components alongside the interim system in some subset
    of precincts (e.g. for a pilot rollout); or

  * using open-source components alongside the interim system in all
    precincts (e.g. for an incremental roll-out of the open source system).

* The requirements for the interim system should include interoperability
  with other systems, and the interoperability formats should be documented
  so they don’t need to be reverse-engineered.


### 5.2. Incremental Approach

To reduce project risk, complexity, and initial costs, it is important to
have a strategy to break the open source voting system project up into
smaller, independent deliverables that can be developed and used in real
elections before the full system is completed.

This is part of an agile approach and has several advantages. It would let
the City start getting real value from the project earlier. It would let the
City get confirmation earlier that the project is “on the right track”
without necessarily having to commit funds for the entire project. It also
builds in a way for the City to take corrective action (e.g. if a vendor
developing a particular component isn’t performing to expectation). Finally,
it eliminates the need to come up with an accurate estimate for the entire
project before starting work.

For example, instead of committing $8 million up front for a single project
to develop a full voting system, the City could instead start out by spending
$2 million on three deliverables: one for $1.5 million and two for $250,000.
Based on the success or progress of the initial projects, the City could
decide to move forward with additional sub-projects, or change its approach
(even before the three deliverables are completed). In this way, the City
limits its financial exposure to risk.

This section recommends some approaches to achieve this. The purpose of this
section is not to serve as an actual plan, but rather to provide concrete
suggestions for how the Department can proceed incrementally in developing
and deploying an open source voting system.


#### 5.2.1. Possible First Components

The Committee suggests the following as components to start work on and
deliver first (see the “Voting System” section for brief descriptions of
these components):

1. Results Reporter (Software)
2. Vote Totaler (Software)
3. Ballot Image Interpreter (Software)
4. Central Ballot Scanner (Hardware & Software)

These components can be developed in parallel. Their development can also be
staggered in conjunction with other deliverables. For example, development on
other components can be started before these are finished.


##### 5.2.1.1. Deployment Strategy

The components above could be deployed and used in conjunction with a
non-open-source interim system. For example, the results reporter could be
used to report the election results of the interim system. The vote totaler
could be used to compute the results of an election run with the interim
system.

There are a number of possibilities for an open-source central ballot scanner
to be used in conjunction with a non-open-source interim system. For example—

1. Open-source central ballots scanners could be responsible for scanning all
vote-by-mail ballots, while the interim system could be responsible for
counting in-precinct ballots. In addition, the interim system could even be
used as a fail-safe backup in the first use in case of an unexpected issue in
the open-source system.

2. Before (1), open-source scanners could be responsible for scanning some of
the vote-by-mail ballots (e.g. in a pilot of the open-source scanners that
precedes a full-scale rollout). This option could possibly be done prior to
certifying the scanners, by taking advantage of California bill [SB 360
(2013-2014)][bill-sb-360-2013].

3. Finally, before (2), open-source scanners could be used to scan
vote-by-mail ballots in addition to the interim system scanning them. This
could be used both to check or audit the interim system, as well as test the
open-source scanners. This final option can likely even be done prior to
certifying the scanners.


##### 5.2.1.2. Rationale

Below are some reasons for selecting the components above:

* Each component has relatively few dependencies.

* The components are on the easier side to implement.

* The components are independently useful and so can help prove the value of
open source.

* The components can be worked on in parallel.

* The components support incremental deployment. Each component can be
deployed and used in conjunction with a non-open-source interim system
relatively easily: replacing individual components of an interim system and
working in conjunction with other components of the interim system via import
and export processes.

* In each case, there is open-source code that already exists that
development of the components might be able to start from, or at least learn
from.

* Working on the components will help to work through and resolve core issues
that need to be worked out anyways

For the Results Reporter:

* The results reporter is probably the “easiest” component to implement and
has the least amount of risk, since it is responsible merely for formatting
and presenting information. In this way, it would be a good warm-up project.

* Since many members of the public view the Department’s election results
pages online, it would nevertheless be a highly visible use of open-source
software.

* It could also be a good public outreach / educational tool around open
source and the open source voting project. The Department could solicit
feedback from the public on how the results pages could look or be improved,
and the Department could implement the best suggestions (since the reporter
would be open source).

* Making the reporter open-source would also be inherently useful because it
would give the Department the ability to customize and improve the current
format, and accept contributions from the public.

For the Vote Totaler:

* This component is also one of the easiest components and so would be good
to start with.

* This is also a component that other jurisdictions would be able to use and
benefit from relatively easily (e.g. jurisdictions using RCV would be able to
use the RCV algorithm functionality). In this way, other jurisdictions could
start to understand the benefits of open source.

For the Ballot Image Interpreter:

* This is a core software component that would be used in a number of
different components, so it is natural to start working on it first.

* Even in the absence of deployed open-source hardware components, it could
be used by members of the public to “check” the scanning done by the interim
system, provided the digital images are made public.

* The open-source software OpenCount might go a long way towards implementing
this component.

For the Central Ballot Scanner:

* This is probably the “easiest” hardware component to work on and implement
first, for reasons that will be described below.

* Deploying this component alone would result in a majority of votes being
counted by open-source software. For example, in the November 8, 2016
election 63% of ballots were vote-by-mail (263,091 out of 414,528 ballots in
all). In this sense, this component provides the biggest “bang for the buck.”

* This component doesn’t require answering the question of whether to use
vote centers, since vote-by-mail ballots need to be tabulated centrally
whether or not San Francisco moves to a vote-center model.

* Unlike precinct-based hardware components like the accessible voting device
and precinct-based scanners, this hardware component would be operated in a
more controlled environment with more highly trained staff. As a result, it
also doesn't need to meet the same portability, durability, usability, and
transportation requirements as precinct-based equipment (which also might
require a custom casing or shell in the case of precinct equipment).

* Also unlike precinct-based hardware components, fewer units would need to
be purchased or manufactured, so it is probably less costly and expensive to
do this step first. For example, for comparison, San Francisco currently has
four high-speed central scanners, but around 600 precincts.

* Central scanners provide multiple possibilities for incremental rollout,
including using the component alongside and in parallel with the interim
system, which all help to mitigate risk. These approaches are described in
the “Deployment Strategy” section.

* Implementing the central scanner before the precinct scanner also makes
sense from a software dependency perspective. The central scanner includes
most of the software that an in-precinct scanner would need anyway, like
ballot interpretation, understanding election definition and ballot layouts,
etc. However, the central scanner provides a safer and more controlled
environment in which to exercise these code paths for the first time. In
other words, with the exception of the high-speed and high-volume nature of
the hardware, it is a strictly simpler component than the precinct-based
scanner.


##### 5.2.1.3. Component Details

This section lists more details about each of the four components we
suggested above. For each of these deliverables, we provide—

* A rough level of the relative complexity (low / medium / high),

* A brief description (though this already appears for the most part in the
Background section of this document),

* What components the deliverable interacts with,

* Possible interfaces / data formats that might be needed,

* Sub-components,

* Dependencies from a project management perspective (i.e. what might be
needed in advance), and

* Other outcomes / deliverables associated with delivering the component.


###### 5.2.1.3.1. Results Reporter (Software)

**Complexity:** Low

**Description.** This is a software-only component responsible for generating
human-readable reports in various formats from structured results data.

**Interfaces / data formats.** Needs to accept as input:

* the “election definition” data (e.g. contests, candidates, districts, etc.).

* the vote total data for the contests as a whole as well as at the desired
aggregation levels (e.g. neighborhood, precinct, district, election day vs.
vote-by-mail, etc.), including the round-by-round vote totals for RCV
elections.

**Sub-components.** The reporter should be able to generate:

* the Statement of Vote (e.g. in PDF format),

* tables for the Election Certification letter (e.g. in PDF format),

* HTML pages for the Department website, and

* Possibly also reports to facilitate the public observation and carrying out
of post-Election Day audit processes (e.g. vote totals divided by batch or
precinct).

**Other outcomes / deliverables.** The required input data and formats should be
spelled out.

**Possible dependencies / pre-requisites.** Real data from past elections for
proto-typing and testing.


###### 5.2.1.3.2. Vote Totaler (Software)

**Complexity:** Low

**Description.** This is a software-only component responsible for aggregating
vote data and generating election results in a machine-readable format. This
includes running the RCV algorithm to generate round-by-round results.

**Interfaces / data formats.** Needs to accept as input:

* the “election definition” data (e.g. contests, candidates, districts, etc.).

* cast vote records (aka CVR’s) for all ballots.

**Sub-components.**

* the code responsible for running the RCV algorithm could be its own
component.

**Other outcomes / deliverables.** The required input data and formats should be
spelled out.

**Possible dependencies / pre-requisites.** Real data from past elections for
proto-typing and testing.


###### 5.2.1.3.3. Ballot Image Interpreter (Software)

**Complexity:** Medium

**Description.** This is a software-only component responsible for interpreting
ballot images, namely by generating a cast vote record (CVR) given a digital
image of a ballot. The component must support ballots from “third-parties”
(e.g. the interim voting system) to support incremental roll-outs like pilot
and hybrid rollouts. The open-source software OpenCount developed at UC
Berkeley could be a foundation for this.

**Applicability.** This component can possibly be used in the following
components:

* precinct ballot scanners

* central ballot scanner

* software application for adjudicating or auditing ballots using their
digital images, independent of a hardware scanner.

**Interfaces / data formats.** Needs to accept as input:

* the “election definition” data (e.g. contests, candidates, districts, etc.).

* the “ballot layout” data (e.g. where contests are located on each ballot
card for each ballot type, etc.).

Needs to output for each ballot:

* a cast vote record (CVR) of the markings on the ballot.

**Sub-components.** This component can possibly have the following sub-component:

* a “contest-unaware” interpreter that accepts a digital image of a ballot
and ballot layout data and outputs what markings are on the ballot (e.g. what
bubbles are filled in, independent of their contest or candidate meaning).

**Other outcomes / deliverables.** The required input data and formats should be
spelled out.

**Possible dependencies / pre-requisites.** Real data from past elections for
proto-typing and testing.


###### 5.2.1.3.4. Central Ballot Scanner (Hardware & Software)

**Complexity:** High

**Description.** This is a hardware component responsible for high-speed,
high-volume ballot scanning in a controlled environment under staff
supervision (e.g. vote-by-mail ballots). It should be capable of (1)
exporting CVR’s and digital images of the ballots it scans, (2)
“out-stacking” ballots that require manual inspection or handling, and (3)
possibly printing unique identifiers on each ballot when scanning to support
the auditing of individual ballots.

**Interfaces / data formats.**

* Same as for the Ballot Image Interpreter.

* Also needs to store digital images of ballots in a defined image format.

**Sub-components.**

* Device drivers (software API’s to control low-level scanner functionality
and, if present, the printer).

* Ballot image interpreter (see component description above).

* High-level software to orchestrate calls between the device drivers and the
ballot image interpreter.

* Printer component to print unique identifiers (possibly required).

**Other outcomes / deliverables.** The required input data and formats should be
spelled out.

**Possible dependencies / pre-requisites.** Real data from past elections for
proto-typing and testing. Samples of ballots from past elections and/or the
interim voting system.


### 5.3. Requirements-gathering

This section contains recommendations related to gathering requirements. For
committee recommendations of specific requirements, see the Requirements
section below.


#### 5.3.1. Key Decisions

The following are some key decisions about requirements that need to be made
at some point when designing and developing the voting system.


##### 5.3.1.1. Vote Centers

California [SB 450][bill-sb-450-2015] ("Elections: vote by mail voting and
mail ballot elections") authorizes counties to conduct elections using vote
centers. The Department of Elections should develop a sense as soon as
possible of the likelihood of using vote centers because that could affect
the requirements and design of the system. Making this decision earlier could
decrease costs since the design and development wouldn’t have to cover
multiple scenarios.


##### 5.3.1.1. Pre-printed versus on-demand ballots, including how selections are marked

For in-person voting, the question of pre-printed ballots versus on-demand
ballots, combined with how ballots are marked (for both accessible voting and
not-necessarily-accessible voting) will greatly affect what type of precinct
hardware needs to be developed. It also greatly affects how many units would
need to be purchased and deployed per precinct.

This decision needs to be made separately for accessible voting and
not-necessarily-accessible voting. However, the decisions for the two
scenarios are not independent. They are related.

For not-necessarily-accessible voting, options include—

1. Pre-printed ballots with selections marked by hand

2. On-demand ballots printed without selections and marked by hand

3. On-demand ballots printed together with selections using an accessible
device

For accessible voting, options include—

1. Pre-printed ballots marked using an accessible device (e.g. by inserting
the ballot)

2. On-demand ballots printed without selections and marked using an
accessible device

3. On-demand ballots printed together with selections using an accessible
device

Some considerations include—

1. The more that the accessible and not-necessarily-accessible scenarios are
similar to one another, the more consistent the voter experience will be. The
most similar would be if both scenarios are conducted with option (3),
“on-demand ballots printed together with selections using an accessible
device.” Different but still similar would be if both groups use pre-printed
ballots or on-demand ballots printed without selections, with the only
difference being how the ballot is marked (by hand versus using an accessible
device). The least similar would be, for example, option (1) for
not-necessarily-accessible voting and option (3) for accessible voting. The
latter happens to be how San Francisco conducts its elections today.

2. To preserve ballot secrecy during the count, it is preferable if the voted
ballots “look” the same across the accessible and not-necessarily-accessible
methods. An example of the ballots looking different would be if accessible
voting results in voted ballots that contain only the voters’ selections and
not other ballot choices, whereas the not-necessarily-accessible approach
results in voted ballots containing all ballot choices but with the voters’
selections marked.

3. Requiring ballots to be printed on-demand for all voters (either with or
without selections) would require using a printer for every voter in the
polling place. This would likely require more electronic devices at each
polling place, which in turn would increase costs, complexity, and the
possibility of something breaking or going wrong. These printing requirements
would be even greater for the case of printing not just blank ballots for all
voters, but ballots with their selections for all voters. This is because
voters would likely need to be occupying a machine while they are making
their selections.

4. Using pre-printed ballots allows voters without disabilities to vote using
the “low-tech” solution of only using a marker or pen (with the exception of
the precinct ballot scanner that normally scans and counts the ballot). This
would reduce the polling place’s overall dependency on technology and
possible things that can go wrong (e.g. power outages, one or more machines
breaking, etc.).

5. Using pre-printed ballots results in increased paper usage and printing
costs, since the Department needs to prepare extras of every ballot type
(including every language, party preference, and combination thereof).

6. Printing ballots on-demand would theoretically allow voters to get the
correct ballot type even if they go to the wrong precinct. Currently, a voter
going to the wrong precinct can only choose among the ballot types
pre-printed and made available at that precinct.

7. If ballots are printed on-demand, poll workers would not have to keep
track of all the different ballot types (e.g. different languages, the
various party ballots, etc.). It would instead automatically be taken care of
by the ballot printer.

8. If the accessible device is a ballot-marking device, the device will be
harder to use because each ballot card would need to be inserted individually
into the device. Conversely, if the accessible device prints the ballot with
selections, fewer physical cards would be required.


##### 5.3.1.2. Printing unique identifiers on ballots at scan-time

One key decision is whether a unique identifier should be printed on every
ballot while it is being scanned.

Pros:

* This would permit more sophisticated auditing approaches that involve
  selecting individual ballots at random, which could reduce time and costs
  (e.g. risk-limiting audits). Without this feature, auditing needs to be
  done in larger “batches,” or ballots need to be kept in careful order to
  allow accessing individual ballots.

Cons:

* It is not clear if COTS scanners support the feature of printing while
  scanning.

* The scanner hardware would become more complicated since there would be
  another “moving part” that can break.


##### 5.3.1.3. End-to-end verifiability

It should be determined how much additional work would need to be done to
make the voting process end-to-end verifiable, and whether and which designs
are more compatible (e.g. among approaches listed in section 5.3.1.1.
“pre-printed versus on-demand ballots”). Also, is this something that could
be incorporated later on in the process, or does it need to be incorporated
from the beginning?


### 5.4. Requirements

This section lists some of the requirements the system should satisfy.


### 5.4.1. Accessibility

* In addition to an audio component and touchscreen, the voting system should
  support accessible features including, but not limited to: sip and puff
  input, a keyboard for write-in votes, voice activation, synchronized audio
  and video, joystick input, Tecla switch, and tactile buttons. These
  [two letters][disability-rights-ca-letters] from Mr. Fred Nisen
  (Supervising Attorney for Voting Rights, Disability Rights California)
  provide more detail.


### 5.4.2. Other

* [TODO: should we recommend (1) supporting manually marked ballots in the
  polling place, or (2) requiring the use of a computer ballot-marking and/or
  ballot-printing device?]

* [TODO: should we recommend (1) pre-printed ballots at polling places, or
  (2) printing ballots on-demand?]

* [TODO: should we recommend for or against end-to-end verifiability?]


### 5.5. Project Management

* As soon as possible, the Department should
  develop and publicize a rough project plan and timeline for the development
  and certification of an open source system, for the case that the project
  is funded. It is okay for this plan to be tentative. It can be refined over
  time as more information becomes available. Articulating even a tentative
  plan would also help in crafting an RFP for the interim system.

* For deliverables, favor smaller deliverables that can be tested
  independently of other components. For example, if developing a software
  application, it may make sense for one or more of the underlying libraries
  to be delivered separately and/or earlier, rather than the application as a
  whole being the only software deliverable.

* [TODO: think about the division of responsibilities between the City and
  vendor. For example, who should be responsible for project management—the
  City or a vendor?]

* [TODO: brainstorm and document various incremental / phased roll-out
  possibilities, and possibly recommend preferred options.]

* [TODO: provide specific recommendations around agile.]


### 5.6. Open Source

This section covers topics related to open source.

* Each software component being developed should be licensed under an
  [OSI-approved][osi-approved-licenses] software license (see also the
  Assumptions section).

* All software development should occur in public (e.g. on GitHub), rather
  than, for example, waiting for the software to reach a certain level of
  completion before becoming public.

* All software being developed in public should have an open source license
  when development first starts, rather than, for example, adding a license
  file later on. This would eliminate any confusion and uncertainty from
  members of the public as to whether the software will really be open
  source. This would encourage members of the public to start contributing to
  the project as early as possible.

* All software being developed should be developed using an open-source
  programming language. For programming languages, any OSI-approved license
  should be okay. The programming language itself need not be copyleft.

* The software "stack" should be open source as much as possible, including
  things like the operating system, database (if any), web server, etc.

* In addition to the software being open source, project documentation
  should be openly licensed. This includes things like design documents,
  installation and setup documents, user manuals, and testing documents.
  [TODO: recommend particular licenses for documentation?]

* [TODO: provide recommendations related to managing community feedback and
  contributions during project development. Also think about whether
  [contributor license agreements][cla] (CLA’s) should be required.]


### 5.7. Procurement

[TODO]


### 5.8. Software architecture and design

* When defining software components to develop, favor designs that promote
  reusing components. For example, a software library that can read a ballot
  image and return the marked “votes” (what we are calling a “ballot image
  interpreter” component) can be used in both precinct scanners and central
  scanners (as well as software applications for adjudication or auditing).
  Favoring component reuse can mean having less code to write and test, which
  in turn can reduce required time and costs.


### 5.9. Software development

* The project should not depend on volunteers for the successful completion
  or security of the project. However, useful volunteer contributions should
  be encouraged and not turned away.


### 5.10. Hardware design

[TODO]


### 5.11. Documentation

[TODO]


### 5.12. Security

[TODO]


### 5.13. Testing

* Datasets of real election data (e.g. a couple past elections in San
  Francisco of different types) should be compiled in a structured format for
  product prototyping and testing. This includes not just vote totals but
  also candidate and contest data. This will help in establishing
  requirements and designing the system.


### 5.14. Certification

[TODO]


### 5.15. Hardware manufacturing or assembly

[TODO]


### 5.16. Deployment

[TODO]


### 5.17. Software maintenance

[TODO]


### 5.18. Hardware maintenance

* The City should prefer professional, commercial support for the operating
  systems the software is running on (even if the operating system is open
  source) over "in-house" maintenance. This will make it easier, for example,
  to ensure that security patches are applied on a timely basis. An example
  of such a provider is [Red Hat](https://www.redhat.com).


[18f-modular-contracting]: https://modularcontracting.18f.gov/
[bill-ab-2252-2015]: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201520160AB2252
[bill-sb-360-2013]: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201320140SB360
[bill-sb-450-2015]: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201520160SB450
[board-of-supervisors]: http://sfbos.org/
[bos-ordinance-vstf]: files/BOS_Ordinance_268-08_VSTF.pdf
[bos-open-source-voting-res]: files/BOS_Resolution_460-14_Open_Source_Voting.pdf
[cavo]: http://www.cavo-us.org/index.html
[cla]: https://en.wikipedia.org/wiki/Contributor_License_Agreement
[colorado-rla-home]: http://bcn.boulder.co.us/~neal/elections/corla/
[colorado-rla-repo]: https://github.com/FreeAndFair/ColoradoRLA
[commission-osvtac]: http://sfgov.org/electionscommission/osvtac
[commission-resolutions]: http://sfgov.org/electionscommission/motions-and-resolutions
[coit]: http://sfcoit.org/
[disability-rights-ca-letters]: files/Disability_Rights_Letters_Nisen.pdf
[eac]: https://www.eac.gov/
[eac-vvsg]: https://www.eac.gov/voting-equipment/voluntary-voting-system-guidelines/
[elections-commission]: http://sfgov.org/electionscommission
[eml-wikipedia]: https://en.wikipedia.org/wiki/Election_Markup_Language
[eml-specs]: http://docs.oasis-open.org/election/eml/v7.0/eml-v7.0.html
[free-and-fair]: http://freeandfair.us/blog/open-free-election-technology/
[github]: https://github.com/
[ict-plan-2008]: files/SF_ICT_Plan_2018-22.pdf
[ieee-1622]: http://grouper.ieee.org/groups/1622/
[la-vsap]: http://vsap.lavote.net/
[lafco]: http://sfgov.org/lafco/
[lafco-report]: files/LAFCo_Report_Open_Source_Voting.pdf
[mayor-budget-press-release]: http://sfmayor.org/article/mayor-lee-signs-citys-balanced-budget-fiscal-years-2016-17-2017-18
[nist-voting]: http://collaborate.nist.gov/voting/bin/view/Voting/WebHome
[nist-itl]: https://www.nist.gov/itl/voting
[nist-vvsg-principles]: http://collaborate.nist.gov/voting/bin/view/Voting/VVSGPrinciplesAndGuidelines
[open-count]: https://github.com/FreeAndFair/OpenCount
[open-count-pres]: https://www.usenix.org/conference/evtwote12/workshop-program/presentation/wang_kai
[open-rla-repo]: https://github.com/FreeAndFair/OpenRLA
[open-voting-consortium]: http://www.openvotingconsortium.org
[oset-arch-html]: https://trustthevote.org/our-work/framework/
[oset-arch-pdf]: http://www.dubberly.com/wp-content/uploads/2014/09/TTV_Framework_Book.pdf
[oset-foundation]: http://www.osetfoundation.org/
[oset-modules]: https://trustthevote.org/our-work/overview-2/
[osi]: https://opensource.org/
[osi-approved-licenses]: https://opensource.org/licenses
[osvtac]: https://osvtac.github.io
[osvtac-about-recs]: https://osvtac.github.io/about#project-recommendations
[prime-iii]: http://www.primevotingsystem.com/
[prime-iii-repo]: https://github.com/HXRL/Prime-III
[prime-iii-faf-repo]: https://github.com/FreeAndFair/STAR-Vote
[proposed-budget-2016]: files/SF_Mayor_Proposed_Budget_2016-18.pdf
[rfp-business-case-page]: http://mission.sfgov.org/OCABidPublication/BidDetail.aspx?K=12141
[rfp-business-case-pdf]: files/SF_Business_Case_RFP_FINAL.pdf
[sf-digital-services]: https://digitalservices.sfgov.org/
[star-vote]: https://www.usenix.org/conference/evtwote13/workshop-program/presentation/bell
[techfar-handbook]: https://playbook.cio.gov/techfar/
[trust-the-vote]: https://trustthevote.org
[verified-voting-foundation]: https://www.verifiedvoting.org/
[vip-repo]: https://github.com/votinginfoproject
[vip-project]: https://votinginfoproject.org/
[vstf]: http://sfgov.org/ccsfgsa/voting-systems-task-force
[vstf-report]: files/VSTF_Report.pdf
