# Open Source Voting System Project Recommendations

(Approved by OSVTAC on August 30, 2017.)

Last update: September 5, 2017

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
document, view the "Project Recommendations" section of the [Documents
page][osvtac-documents] of the committee's website.


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

**Scope**

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

**Priorities**

* This document should prioritize high-level recommendations over low-level
  recommendations.

* This document should prioritize recommendations that are needed sooner
  rather than later.

**Non-goals**

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
   * [ColoradoRLA][colorado-rla-repo], Free & Fair
   * [Voting Systems Assessment Project][la-vsap] (VSAP), Los Angeles County
   * [Prime III][prime-iii], Dr. Juan E. Gilbert
   * [STAR-Vote][star-vote], Travis County, TX

4. Additional Links
   * [GitHub][github]
   * National Institute of Standards and Technology (NIST)
     - [NIST Voting Public Working Groups][nist-voting]
     - [VVSG Principles and Guidelines][nist-vvsg-principles]
   * [Open Source Initiative][osi] (OSI)
   * [OpenCount][open-count]


## 5. Recommendations

**Interim Voting System**

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

**Requirements-gathering**

This section contains recommendations about gathering requirements. For
recommendations in relation to specific requirements, see the Requirements
section below.

[TODO]

**Requirements**

This section relates to specific requirements rather than the process of
gathering or articulating requirements.

* California [SB 450][bill-sb-450-2015] ("Elections: vote by mail voting and
  mail ballot elections") authorizes counties to conduct elections using vote
  centers. The Department of Elections should develop a sense as soon as
  possible of the likelihood of using vote centers because that could affect
  the requirements and design of the system. Making this decision earlier
  could decrease costs since the design and development wouldn’t have to
  cover multiple scenarios.

* [TODO: think about ballot-marking device vs. manually marked ballots, and
  ballot on-demand vs. pre-printed ballots.]

* [TODO: should end-to-end verifiability be a requirement?]

**Project Management**

* As soon as possible, the Department should
  develop and publicize a rough project plan and timeline for the development
  and certification of an open source system, for the case that the project
  is funded. It is okay for this plan to be tentative. It can be refined over
  time as more information becomes available. Articulating even a tentative
  plan would also help in crafting an RFP for the interim system.

* [TODO: think about the division of responsibilities between the City and
  vendor. For example, who should be responsible for project management—the
  City or a vendor?]

* [TODO: brainstorm and document various incremental / phased roll-out
  possibilities, and possibly recommend preferred options.]

* [TODO: provide specific recommendations around agile.]

**Open Source**

This section covers topics related to open source.

* The development of the software should be done in public from the first day
  of development.

* All software should be licensed under an
  [OSI-approved][osi-approved-licenses] software license from the first day
  of development.

* In addition to the software being open source, project documentation
  should be openly licensed. This includes things like design documents,
  installation and setup documents, user manuals, and testing documents.
  [TODO: recommend particular licenses for documentation?]

* [TODO: provide recommendations related to managing community feedback and
  contributions during project development. Also think about whether
  [contributor license agreements][cla] (CLA’s) should be required.]

**Procurement**

[TODO]

**Software architecture and design**

[TODO]

**Software development**

[TODO]

**Hardware design**

[TODO]

**Documentation**

[TODO]

**Security**

[TODO]

**Testing**

[TODO]

**Certification**

[TODO]

**Hardware manufacturing or assembly**

[TODO]

**Deployment**

[TODO]

**Software maintenance**

[TODO]

**Hardware maintenance**

[TODO]


[18f-modular-contracting]: https://modularcontracting.18f.gov/
[bill-ab-2252-2015]: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201520160AB2252
[bill-sb-450-2015]: http://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201520160SB450
[board-of-supervisors]: http://sfbos.org/
[bos-ordinance-vstf]: files/BOS_Ordinance_268-08_VSTF.pdf
[bos-open-source-voting-res]: files/BOS_Resolution_460-14_Open_Source_Voting.pdf
[cla]: https://en.wikipedia.org/wiki/Contributor_License_Agreement
[colorado-rla-repo]: https://github.com/FreeAndFair/ColoradoRLA
[commission-osvtac]: http://sfgov.org/electionscommission/osvtac
[commission-resolutions]: http://sfgov.org/electionscommission/motions-and-resolutions
[coit]: http://sfcoit.org/
[elections-commission]: http://sfgov.org/electionscommission
[github]: https://github.com/
[ict-plan-2008]: files/SF_ICT_Plan_2018-22.pdf
[la-vsap]: http://vsap.lavote.net/
[lafco]: http://sfgov.org/lafco/
[lafco-report]: files/LAFCo_Report_Open_Source_Voting.pdf
[mayor-budget-press-release]: http://sfmayor.org/article/mayor-lee-signs-citys-balanced-budget-fiscal-years-2016-17-2017-18
[nist-voting]: http://collaborate.nist.gov/voting/bin/view/Voting/WebHome
[nist-vvsg-principles]: http://collaborate.nist.gov/voting/bin/view/Voting/VVSGPrinciplesAndGuidelines
[open-count]: https://github.com/FreeAndFair/OpenCount
[osi]: https://opensource.org/
[osi-approved-licenses]: https://opensource.org/licenses
[osvtac]: https://osvtac.github.io
[osvtac-documents]: /documents
[prime-iii]: http://www.primevotingsystem.com/
[proposed-budget-2016]: files/SF_Mayor_Proposed_Budget_2016-18.pdf
[rfp-business-case-page]: http://mission.sfgov.org/OCABidPublication/BidDetail.aspx?K=12141
[rfp-business-case-pdf]: files/SF_Business_Case_RFP_FINAL.pdf
[sf-digital-services]: https://digitalservices.sfgov.org/
[star-vote]: https://www.usenix.org/conference/evtwote13/workshop-program/presentation/bell
[techfar-handbook]: https://playbook.cio.gov/techfar/
[vstf]: http://sfgov.org/ccsfgsa/voting-systems-task-force
[vstf-report]: files/VSTF_Report.pdf
