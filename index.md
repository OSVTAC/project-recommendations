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


## 1. Background

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


## 2. Goals

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
[cavo]: http://www.cavo-us.org/index.html
[cla]: https://en.wikipedia.org/wiki/Contributor_License_Agreement
[colorado-rla-home]: http://bcn.boulder.co.us/~neal/elections/corla/
[colorado-rla-repo]: https://github.com/FreeAndFair/ColoradoRLA
[commission-osvtac]: http://sfgov.org/electionscommission/osvtac
[commission-resolutions]: http://sfgov.org/electionscommission/motions-and-resolutions
[coit]: http://sfcoit.org/
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
[osvtac-documents]: /documents
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
