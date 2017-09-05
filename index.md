# Open Source Voting System Project Recommendations

(Approved by OSVTAC on August 30, 2017.)

Last update: September 4, 2017

**Note: these recommendations are a work in progress and not yet complete.**

This document contains the recommendations of San Francisco's [Open Source
Voting System Technical Advisory Committee][osvtac] (OSVTAC, or TAC) for
the City and County of San Francisco's open source voting system project, as
of the version date that appears above.

The committee started this document on August 30, 2017 and will continue
to work on it over time.

Substantive updates to this document occur by a vote of the committee at a
committee meeting. Meetings occur approximately once a month. To learn more
about the committee, visit the committee's website at
[https://osvtac.github.io][osvtac]. To learn how to suggest changes to this
document, view the [README][osvtac-recommendations-repo] document in the
GitHub repository containing the source files for these recommendations.


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

In May 2017, the Department of Elections [issued an RFP][rfp-business-case]
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
  system do not include the responsibilities of a voter registration system
  (e.g. the Department’s election management system, or EMS). However, the
  voting system should be able to interoperate with the EMS. If the ballots
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

[TODO]


## 5. Recommendations

**Interim Voting System**

[TODO]

**Requirements-gathering**

This section contains recommendations about gathering requirements. For
recommendations in relation to specific requirements, see the Requirements
section below.

[TODO]

**Requirements**

[TODO]

**Project Management**

[TODO]

**Open Source**

[TODO]

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


[bill-ab-2252-2015]: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201520160AB2252
[bill-sb-450-2015]: http://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201520160SB450
[board-of-supervisors]: http://sfbos.org/
[bos-ordinance-vstf]: files/BOS_Ordinance_268-08_VSTF.pdf
[bos-open-source-voting-res]: files/BOS_Resolution_460-14_Open_Source_Voting.pdf
[commission-osvtac]: http://sfgov.org/electionscommission/osvtac
[commission-resolutions]: http://sfgov.org/electionscommission/motions-and-resolutions
[coit]: http://sfcoit.org/
[elections-commission]: http://sfgov.org/electionscommission
[ict-plan-2008]: files/SF_ICT_Plan_2018-22.pdf
[lafco]: http://sfgov.org/lafco/
[lafco-report]: files/LAFCo_Report_Open_Source_Voting.pdf
[mayor-budget-press-release]: http://sfmayor.org/article/mayor-lee-signs-citys-balanced-budget-fiscal-years-2016-17-2017-18
[osvtac]: https://osvtac.github.io
[osvtac-recommendations-repo]: https://github.com/OSVTAC/project-recommendations
[proposed-budget-2016]: files/SF_Mayor_Proposed_Budget_2016-18.pdf
[rfp-business-case]: http://mission.sfgov.org/OCABidPublication/BidDetail.aspx?K=12141
[sf-digital-services]: https://digitalservices.sfgov.org/
[vstf]: http://sfgov.org/ccsfgsa/voting-systems-task-force
[vstf-report]: files/VSTF_Report.pdf
