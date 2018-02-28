## 5. Recommendations


### 5.1. Interim Voting System

* The contract for the interim system (i.e. the system to be used after 2018)
  should permit all possible combinations of phasing in an open source system
  alongside it. Examples of possible combinations include:

  * using open source components to scan vote-by-mail ballots and the interim
    system to scan precinct ballots, or vice versa;

  * using an open source accessible voting device in conjunction with the
    interim system’s precinct-based scanner, or vice versa;

  * scanning the ballots of the interim system using an open source scanner;

  * tabulating ballots scanned by an open source scanner using the interim
    system’s tabulation software;

  * using an open source reporting and/or tabulation system with the output
    from the interim system’s scanners;

  * using open source components alongside the interim system in some subset
    of precincts (e.g. for a pilot rollout); or

  * using open source components alongside the interim system in all
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
it eliminates the need to come up with accurate cost and time estimates for
the entire project before starting work.

For example, instead of committing $8 million up front for a single project
to develop a full voting system, the City could instead start out by spending
$2 million on three deliverables, say: one for $1.5 million and two for $250,000.
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
most of these components):

1. Results Reporter (Software)
2. Vote Totaler (Software)
3. Ballot Picture Interpreter (Software)
4. Central Ballot Scanner (Hardware & Software)
5. Ballot Layout Analyzer (Software)
6. Ballot Batch Management (Software)
7. Ballot Tabulation Audit Support (Software)

Choosing the above as first components seems to mirror the approach that Los
Angeles County is taking in its VSAP project. In particular, Los Angeles
County developed and submitted its "Tally System" for certification even
before its in-precinct Ballot Marking Device was engineered and manufactured.
Los Angeles County's "RFP Phase 1: #17-008" defines its Tally System on page
48 as--

> A system of hardware and software that reads and captures the vote
selections on ballots, applies required business rules and adjudications,
tabulates the totals of votes, ballots cast, and other metrics, and publishes
the results the election. The tally system also supports transparent auditing
processes to ensure the accuracy and integrity of the election tally results.

This seems to encompass the functionality of the four components listed above.

Los Angeles County submitted its VSAP Tally Version 1.0 to the California
Secretary of State for certification on September 19, 2017. Section 3.3
(pages 25-28) of its Phase 1 RFP provides more detail on the completion of
Los Angeles County's Tally System in relation to other components like their
Ballot Marking Device.


#### 5.2.2. Rationale

Below are some reasons for selecting the components above:

* Each component has relatively few dependencies.

* The components are on the easier side to implement.

* The components are independently useful and so can help prove the value of
open source.

* The components can be worked on in parallel. Their development can also be
staggered in conjunction with other deliverables. For example, development on
other components can be started before these are finished.

* In each case, there is open source code that already exists that
development of the components might be able to start from, or at least learn
from.

* Working on the components will help to work through and resolve core issues
that need to be worked out anyways

* Each of these components supports incremental deployment. Each component
  can be deployed and used by replacing the corresponding component of a
  non-open source interim system, and then interoperating with the other
  components of the voting system (interim or not). This is true even without
  requiring anything extra of the interim system. See the "Deployment
  Strategies" sub-section below for further details.

  In contrast, an example of a component that probably _wouldn't_ support
  incremental deployment as easily is the ballot layout software application.
  This is because an interim system's scanners probably can't be guaranteed
  to scan ballots created by a third-party.

  Similarly, it is probably more difficult to design an accessible
  ballot-marking device that can mark another vendor's ballot than it is to
  design a scanner that can interpret another vendor's ballot. This is
  because marking a ballot is a harder problem to solve than interpreting a
  ballot. While the latter is primarily a software problem (which would be
  addressed by the ballot image interpreter component), the former leans more
  towards being a hardware problem.

For the Results Reporter:

* The results reporter is probably the “easiest” component to implement and
has the least amount of risk, since it is responsible merely for formatting
and presenting information. In this way, it would be a good warm-up project.

* Since many members of the public view the Department’s election results
pages online, it would nevertheless be a highly visible use of open source
software.

* It could also be a good public outreach / educational tool around open
source and the open source voting project. The Department could solicit
feedback from the public on how the results pages could look or be improved,
and the Department could implement the best suggestions (since the reporter
would be open source).

* Making the reporter open source would also be inherently useful because it
would give the Department the ability to customize and improve the current
format, and accept contributions from the public.

For the Vote Totaler:

* This component is also one of the easiest components and so would be good
to start with.

* This is also a component that other jurisdictions would be able to use and
benefit from relatively easily (e.g. jurisdictions using RCV would be able to
use the RCV algorithm functionality). In this way, other jurisdictions could
start to understand the benefits of open source.

For the Ballot Picture Interpreter:

* This is a core software component that would be used in a number of
different components, so it is natural to start working on it first.

* Even in the absence of deployed open source hardware components, it could
be used by members of the public to “check” the scanning done by the interim
system, provided the digital ballot pictures are made public. The visually impaired
could use a ballot picture interpreter on their device with a speech synthesis
application to validate/check a home printed or marked ballot.

  _[Paragraph edited: Jan. 18, 2018 meeting.]_

* The open source software OpenCount might go a long way towards implementing
this component.

For the Central Ballot Scanner:

* This is probably the “easiest” hardware component to work on and implement
first, for reasons that will be described below.

* Deploying this component alone would result in a majority of votes being
counted by open source software. For example, in the November 8, 2016
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


#### 5.2.3. Component Details

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


##### 5.2.3.1. Results Reporter (Software)

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

* computer-readable equivalent to the Statement of Vote (e.g. in spreadsheet (xls),
delimited text (tsv), and NIST-SP1500-100 (xml) formats),

  _[Paragraph added: Jan. 18, 2018 meeting.]_

* HTML pages for the Department website, and

* Possibly also reports to facilitate the public observation and carrying out
of post-Election Day audit processes (e.g. vote totals divided by batch or
precinct).

**Other outcomes / deliverables.** The required input data and formats should be
spelled out.

**Possible dependencies / pre-requisites.** Real data from past elections for
prototyping and testing.


##### 5.2.3.2. Vote Totaler (Software)

**Complexity:** Low

**Description.** This is a software-only component responsible for aggregating
vote data and generating election results in a machine-readable format. This
includes running the RCV algorithm to generate round-by-round results. Normally
votes have subtotals reported by consolidated precinct, and may separate
election-day precinct voting and vote-by-mail ballot subtotals.

_[Paragraph edited: Jan. 18, 2018 meeting.]_

**Interfaces / data formats.** Needs to accept as input:

* the “election definition” data (e.g. contests, candidates, districts, etc.).

* cast vote records (aka CVR’s) for all ballots.

**Sub-components.**

* the code responsible for running the RCV algorithm could be its own
component.

**Other outcomes / deliverables.** The required input data and formats should be
spelled out.

**Possible dependencies / pre-requisites.** Real data from past elections for
prototyping and testing.


##### 5.2.3.3. Ballot Picture Interpreter (Software)

**Complexity:** Medium

**Description.** This is a software-only component responsible for interpreting
digital ballot pictures, namely by generating a cast vote record (CVR) given a digital
picture of a ballot. The component must support ballots from “third-parties”
(e.g. the interim voting system) to support incremental roll-outs like pilot
and hybrid rollouts, and possibly to support home-printed
"remote accessible vote by mail"
ballots. The open source software OpenCount developed at UC
Berkeley could be a foundation for this.

The picture interpreter should be able to identify and remove the base
printing and watermarks so any remaining extraneous marks can be identified.
The presence of a significant amount of extraneous marks might require
that ballot be identified for adjudication. Likewise, marks clearly not
present or not fully marked must be identified for adjudication.

_[Paragraph added: Jan. 18, 2018 meeting.]_

**Applicability.** This component can possibly be used in the following
components:

* precinct ballot scanners

* central ballot scanner

* software application for adjudicating or auditing ballots using their
digital pictures, independent of a hardware scanner.

**Interfaces / data formats.** Needs to accept as input:

* the “election definition” data (e.g. contests, candidates, districts, etc.).

* the “ballot layout” data (e.g. where contests are located on each ballot
card for each ballot type, etc.).

* the digital ballot pictures themselves.

* batch header/footer pages and/or box label codes

  _[Item added: Jan. 18, 2018 meeting.]_

Needs to output for each ballot:

* a cast vote record (CVR) of the markings on the ballot.

* a report of extraneous or ambiguous marks requiring adjudication,
  with a data file referencing the CVR, ballot picture, and contest
  selections.

  _[Item added: Jan. 18, 2018 meeting.]_

**Sub-components.** This component can possibly have the following sub-component:

* a “contest-unaware” interpreter that accepts a digital picture of a ballot
and ballot layout data and outputs what markings are on the ballot (e.g. what
bubbles are filled in, independent of their contest or candidate meaning).

**Other outcomes / deliverables.** The required input data and formats should be
spelled out.

**Possible dependencies / pre-requisites.** Real data from past elections for
prototyping and testing.


##### 5.2.3.4. Central Ballot Scanner (Hardware & Software)

**Complexity:** High

**Description.** This is a hardware component responsible for high-speed,
high-volume ballot scanning in a controlled environment under staff
supervision (e.g. vote-by-mail ballots). It should be capable of (1)
exporting CVR’s and digital pictures of the ballots it scans, (2)
“out-stacking” ballots that require manual inspection or handling, and (3)
possibly printing unique identifiers on each ballot when scanning to support
the auditing of individual ballots.

**Interfaces / data formats.**

* Same as for the Ballot Picture Interpreter.

* Also needs to store digital pictures of ballots in a defined image format.

**Sub-components.**

* Device drivers (software API’s to control low-level scanner functionality
and, if present, the printer).

* Ballot picture interpreter (see component description above).

* High-level software to orchestrate calls between the device drivers and the
ballot picture interpreter.

* Printer component to print unique identifiers (possibly required).

**Other outcomes / deliverables.** The required input data and formats should be
spelled out.

**Possible dependencies / pre-requisites.** Real data from past elections for
prototyping and testing. Samples of ballots from past elections and/or the
interim voting system.


##### 5.2.3.5. Ballot Layout Analyzer (Hardware & Software)

**Complexity:** Medium

**Description.** This is a software component to let one "reverse engineer"
structured ballot layout data from existing paper ballots from another vendor.
This component may be needed during a possible interim phase in which
open source components are used for scanning and interpreting ballots that are
generated by a different vendor (i.e. the City's vendor during the time
when the open source system is being developed).  This component will be
needed if that vendor is not able to provide structured ballot layout data
along with the paper ballots.  It is likely that this component will
not be completely automated, but rather will be semi-automated.

**Interfaces / data formats.** Needs to accept as input:

* the “election definition” data (e.g. contests, candidates, districts, etc.).

* the digital ballot pictures (scanned images or PDF)

Needs to output for each ballot type:

* the “ballot layout” data (e.g. where contests are located on each ballot
card for each ballot type, etc.) that will be used as input to the Ballot
Picture Interpreter component.

**Other outcomes / deliverables.** The required input and output data and
formats should be spelled out.

**Possible dependencies / pre-requisites.** Real data from past elections for
prototyping and testing. Samples of ballots from past elections and/or the
interim voting system.

_[Section added: Dec. 14, 2017 meeting.]_


##### 5.2.3.6. Ballot Batch Management (Software)

**Complexity:** Low

**Description.** This is a software component that allows boxes of ballots
to be organized into batches for scanning and auditing. Labels may be
printed to be attached to ballot boxes collected, transported, and stored.
Batches of ballots might include a scannable header page, marking the
beginning of a batch of ballots, and a scannable footer page, marking the
end of the batch. The header/footer pages mark the consolidated precinct
and other information identifying the ballot batch, and might also include
signatures from poll workers, and digital audit information, e.g.
IDs, temporary digital signatures and keys, starting and ending hash chain
codes from a precinct scanner. An additional header/footer page might be
created to wrap and identify outstacked ballots.

The batch management system would be used to:

* create box labels and header/footer pages,

* provide a database of batch IDs with associated precinct and grouping
  IDs,

* provide a means to scan box labels and log departure/arrival of ballot boxes
  transported or stored/retrieved,

* provide the input to the ballot picture interpreter identifying the
  batch being processed, and associated information (e.g. precinct ID),

* organize scan batches to associate CVR (Cast Vote Record) data
  with ballot box storage ID and location, and

* track progress of scanning, adjudication, and auditing of ballot batches.

**Interfaces / data formats.** Needs to accept as input:

* a definition of precincts, precinct consolidation, and ballot type
  by precinct, used to organize batch collections.

* bar code scans of box labels used for tracking

* scans of batch header/footer pages

Needs to output:

* data files with batch IDs and associated precinct/group information

* printable labels and header/footer pages

* data with batch scan/audit status and transport logs

**Other outcomes / deliverables.** The required input and output data and
formats should be spelled out.

**Possible dependencies / pre-requisites.** Batch management procedures
need to be defined so batch IDs can be included with the Ballot Picture
Interpreter output CVRs and used with the Vote Totaler.

_[Subsection added: Jan. 18, 2018 meeting.]_


##### 5.2.3.7. Ballot Tabulation Audit Support (Software)

**Complexity:** Medium

**Description.** This is a software component that manages an audit
process that includes a manual count. A precinct-based audit might
be performed, where all ballots in randomly selected precincts are
hand-counted, or a RLA (Risk Limiting Audit) might be performed,
where a randomly selected set of ballots among all precincts are
selected for a hand-count. The number of ballot selected in an
RLA is based on a statistical formula depending on the closeness of
votes between top contenders.

More general election auditing (like chain of custody) is outside
the scope of this component.

Audit support software could include the following:

* Save manually generated random input (e.g. dice roll) for precinct selections
  or RLA random number seed.

* For an RLA, a public high-quality random number generator is used to randomly
  select ballots to be pulled.

* For ballots selected by order within a batch (does not have a printed
  and sorted ID), a scanner might be used to sheet feed ballots, stopping
  where a ballot needs to be pulled.

* If the order in a stored ballot batch does not match the order on stored
  CVRs (cast vote records) and no ballot IDs are available, a new central scan
  and picture image analysis might be required.

* Retrieve the CVRs for selected ballots and pass them to the vote totaler.

* Enter hand-count results and compare totals with the official precinct
  totals or the totaled CVR selection.

**Interfaces / data formats.** Needs to accept as input:

* the “election definition” data (e.g. contests, candidates, districts, etc.).

* a definition of batches with precincts, precinct consolidation, and ballot type.

* results of the vote totaler.

* random number seed

* Cast Vote Records (for an RLA)

* Hand-count results

Needs to output:

* for an RLA, the randomly selected ballots with either ID or sequence in
  a batch.

* comparison of hand counts and machine counts

* scanner controls if used to pull RLA selected ballots

**Other outcomes / deliverables.** The required input and output data and
formats should be spelled out.

**Possible dependencies / pre-requisites.** If an RLA audit is performed
and stored ballots might not match ordered CVRs, then the central ballot
scan and picture interpreter would be required to perform an electronic
recount of all ballots and generate matching CVRs. If the picture interpreter
can run at the speed of the scanner, regenerating CVRs (for an electronic
recount) adds no extra cost.

_[Subsection added: Jan. 18, 2018 meeting.]_


#### 5.2.4. Deployment Strategies

The components listed above can be deployed and used in conjunction with a
non-open source interim system even before a full open source voting system
is ready. This section provides more details about how this could be done.

For example, an open source results reporter could be used to report the
election results of the non-open source interim system. It would simply need
to take in the aggregate, numeric results from the interim system. The output
would not need to interact with the interim system.

Similarly, an open source vote totaler could be used to compute the numeric
results of an election run with the interim system. It would only require
taking in the non-aggregated numeric results from the interim system, and
then feeding the aggregate results into the results reporter.


##### 5.2.4.1. Central Ballot Scanner Phases

For the central ballot scanner, there are a number of options for
incrementally phasing in an open source version.

In chronological order, some of these possible phases are--

1. Even before the scanner hardware is ready to be tested, the software-only
ballot image interpreter component could be used to check the vote counts of
the interim system from the information of the digital ballot pictures. In
addition, if the pictures are made public during the canvass (along with the
ballot image interpreter software), even members of the public could perform
this "check."

2. When the open source central scanners are ready enough to test, the
scanners could be used to scan vote-by-mail ballots _in addition_ to the
interim system scanning them. This could be used both to check or audit the
interim system, as well as to test the open source scanners. This can likely
be done even without certifying the scanners. This is essentially what the
Humboldt County Elections Transparency Project did in the late 2000's.

3. Once we have enough confidence in the open source scanners, they could be
used as the primary scanner for _some_ of the vote-by-mail ballots (e.g. in a
pilot of the open source scanners that precedes a full-scale rollout). This
option could possibly be done prior to certifying the scanners, by taking
advantage of California bill [SB 360 (2013-2014)][bill-sb-360-2013].

4. Finally, once the open source central scanners are certified, they could
be used to scan _all_ of the vote-by-mail ballots (while the interim system
could be responsible for counting in-precinct ballots). In this scenario, the
interim system could perhaps even be used as a fail-safe backup in case of an
unexpected issue with the open source system (or else as a check, in the
same way that the open source scanners were used as a check in bullet point
(2) above).


### 5.3. Requirements-gathering

This section contains recommendations related to gathering requirements. For
committee recommendations of specific requirements, see the Requirements
section below.


#### 5.3.1. Key Decisions

The following are some key decisions about requirements that need to be made
at some point when designing and developing the voting system. Some pro and
con tradeoffs are included.

At this point, the intent here is to just present options with some
discussion, not a particular recommendation.

**Assumptions:**

* Votes are cast (recorded, submitted, and stored) on paper in a human-readable form.

* An electronic representation of ballots made either by voting machines or scanners serves only as a copy of the official paper ballot.

* Ballots marked are on paper that meets the California regulations for printing (counterfeit resistance).

* By 2020, CA [AB973][bill-ab-973-2017] requires support of _Remote Accessible
Vote By Mail_ ballots ([AB2252][bill-ab-2252-2015]) for voters with disabilities
or overseas and military voters. Home computers are used to print ballots on
ordinary paper, but returned via special mail envelopes.

* Voting types to be considered:
  + Vote by mail (preprinted and special accessible/overseas)
  + Vote on election day at a polling location (precinct voting)
  + Vote prior to election day at an early vote center
  + Vote by people with disabilities requiring special equipment (ballot marking device)
  + Vote with Provisional Ballots (enclosed in a special envelope for later qualification)


##### 5.3.1.1. Will Vote Centers be used for early and/or election day voting?

California [SB 450][bill-sb-450-2015] ("Elections: vote by mail voting and
mail ballot elections") authorizes counties to conduct elections using vote
centers. The Department of Elections should develop a sense as soon as
possible of the likelihood of using vote centers because that could affect
the requirements and design of the system. Making this decision earlier could
decrease costs since the design and development wouldn’t have to cover
multiple scenarios.

While voters can be assigned to the traditional election-day precinct polling
site, with the right equipment, each poll site could have the full features of
a vote center, i.e. allow voters from any precinct to vote at that site.

Vote Centers could be used for:
   1. Early voting only
   2. Election day voting at selected locations
   3. All election day polling locations


##### 5.3.1.2. Should precinct polling and vote centers use the same paper ballots as those used in vote-by-mail?

  Background: If a voting machine is used to prepare ballots for printing, the
paper ballots marked could use the same printing and layout as a vote-by mail
ballot, or could have a simpler and shorter format listing just the contests and
selected choices (called _paper cast vote record_ (CVR) in California Election Code).
The shorter format could be on smaller paper, possibly only a single sheet, vs a
larger multipage scanned mail ballot. Voting machines (ballot marking devices)
could be used only by voters with disabilities, while most voters at a precinct
or vote center uses a normal mail ballot, or all voters there could use voting
machines with printed ballots.

Mail-Only Format Pros:

* Only one style of ballot printing is required
* No need for precinct voters to use voting machines-- voters without
    disabilities can use a "low-tech" solution of only a marker or pen
* Central storage and recounting has all the same ballot size/type
* Better ballot secrecy because all ballots look the same.
* Reduced requirements for printers and possible problems with printer malfunction and paper jams.
* Voting with hand-marked ballots could be done with no electric power.

Mail-Only Format Cons:
* Printing on large mail ballot paper, usually double sided,  requires
    special, possibly nonstandard, equipment. Sheets might need to be
    hand-inserted individually.


##### 5.3.1.3. Should ballots to be hand-marked be preprinted or printed on demand?

  Background: If precinct voting is based on the low-tech paper ballot marked
with a pen, pads of preprinted paper ballots could be used. However, separate
pads are required for each ballot type, party preference and language preference
used at that precinct. A vote center might need to store ballots for all ballot
types in the county, each in all languages. An alternative is to use blank
ballot card stock with a printer to create any desired ballot type and language
preference, known as "ballot on demand" (BOD).

Ballot on Demand Pros:
* Reduced printing cost and paper use: no need to stock extra preprinted
    ballots in case all voters show up.
* Easier to accommodate multiple languages
* Allows any poll site to be a vote-center. Eliminates the problem of people
    at the wrong poll site casting provisional ballots with an incorrect
    ballot type.

Ballot on Demand Cons:
* On site printers can fail and probably require AC power, stopping voting.
* Printing on large mail ballot paper, usually double sided requires special, possibly nonstandard, equipment.


##### 5.3.1.4. Should voting at a precinct or vote center be primarily based on paper ballots hand-marked with a pen, or voting machine with a printer?

Background: After voters check in at a precinct, they could be given a
paper ballot (similar or the same as a mail ballot) and pen to mark it.
Alternatively, they could be given a blank ballot sheet and sent to
a voting machine (e.g. computer/tablet) where choices can be entered and
reviewed. To access the correct ballot type, voters may be given a
_token_ containing the ballot type or else the blank ballot sheet could have
a ballot type code preprinted. When voters complete their selections, the
paper is inserted into a printer, then they check the final printed ballot
prior to casting into a ballot box.


Machines used by all non-mail voters Pros:
* Paper+Electronic CVR has the highest security/integrity. Digital signatures can be printed on ballots to authenticate paper.
* Time to vote can be less than marking.
* Mistakes can be undone without needing another ballot to mark.
* Machines could read a QR code from a vote at home app to print a ballot immediately.
* A separate non-mail ballot format from voting machines would be the same for ordinary voters and those with special needs.
* Extra machines provide redundancy vs a single disability-access machine.
* Vote centers could handle all ballot types without the need for a ballot on demand system.
* Election-day machines could only allow authorized write-ins to be recorded, simplifying write-in voting and enabling end of day totals that include write-ins.
* A full precinct scanner is not required-- just a simple bar code scanner
    to track paper cast by entering into a ballot box. (The bar code is matched
    against the electronic CVR.)
* Voting machines have the same effect as precinct scanners with
stored electronic CVRs and end of day totals available.

Machines used by all non-mail voters Cons:
* Requires more equipment, with increased cost, complexity, and the possibility
    of something going wrong. May require backup power.
* More possible problems with paper jams and printer malfunction.
* Voters need to be occupying a machine while voting.
* Mail ballot processing is still a separate sizable operation.


##### 5.3.1.5. If voting machines are used at a precinct, should there be one printer per voting station?

Background: Each electronic voting station could be configured with a
printer to create the ballots to be cast. Alternatively, there could be
many voting stations (e.g. just a tablet computer), then a separate
printing station would be used to print completed ballots. With separate
printing stations, a _token_ is required to be scanned to identify the
ballot completed at a voting station.

Voters using a home computer or phone to record personal ballot choices
could bring a QR code printed or saved in a smartphone and go directly
to the printing station. A token might be required to verify the ballot
type.

Note: a _token_ could simply be a bar code with ballot type and unique
random number printed on the outside of a privacy folder. The number has
no association with a voter-- just a way to associate the ballot entered
at a voting station with the ballot to be printed. Another form of token
in use is an RFID chip.

##### 5.3.1.5. If voters at precincts use hand-marked ballots, should ballots be scanned centrally or at the precinct/vote center?

Precinct ballot scanner Pros:
* Overvotes/Undervotes and invalid or ambiguous marks can be reported by the
    scanner prior to submitting
* Precinct vote counts are available immediately at the end of the day
* Reduces the need for central scanning equipment

Precinct ballot scanner Cons:
* More equipment is required than central-only scanners
* If the scanner and ballot collection is integrated (the scanner feeds
    into a ballot collection bin), custom equipment may be required.
* Not required if all ballots are printed by a voting machine


##### 5.3.1.6. If a precinct scanner is used, does the scanner need to be integrated with a ballot collection bin?

  Background: Custom-built precinct ballot scanners sold by election vendors
usually include a ballot collection bin within same box containing the scanner.
The scanner feeds the ballot into the collection box, or else reverses the paper
feed in case of an error detected. Scanners may need multiple collection bins
in case of ambiguous marks or write-in votes. An integrated device likely means custom hardware vs COTS equipment.


##### 5.3.1.7. If a precinct scanner (or central scanner) is used, does it need to include an imprinter to record a ballot/scan ID?

  Background: To match a specific paper ballot in a ballot box with a scanned
CVR, either the order of insertion must be maintained, or a unique identifier
associated with the scan needs to be added to the ballot. Alternatively, ordered
ballots could be rescanned centrally during a recount or audit and matched as a
batch with the original scan.

Scanner Imprinter Pros:

* This would permit more sophisticated auditing approaches that involve
  selecting individual ballots at random, which could reduce time and costs
  (e.g. risk-limiting audits). Without this feature, auditing needs to be
  done in larger “batches,” or ballots need to be kept in careful order to
  allow accessing individual ballots.

Scanner Imprinter Cons:

* It is not clear if COTS scanners support the feature of printing while
  scanning. Available imprinters are expensive and might reduce scan speed.

* The scanner hardware would become more complicated since there would be
  another “moving part” that can break, and may require consumables, e.g.
  printer ink or ribbon changes.


##### 5.3.1.8. If a voting machine is used to print ballots, does the ballot collection box need to have an integrated scanner?

  Background: Using a voting machine with voter-verified ballot does not
constitute casting a ballot-- the act of submitting the ballot after
verification is the cast ballot. Voters might choose to discard a ballot and
revote, so a simple bar-code scanner is useful to match the electronic CVR with
paper ballots submitted (i.e. exclude discarded ballots). Discarded ballots
could be scanned instead, but a voter could still walk off with a ballot, or a
ballot might not print correctly.

Additional ballot box scanner Pros: [TODO]

Additional ballot box scanner Cons: [TODO]


##### 5.3.1.9. Is voting equipment required to run off a battery (without outside AC power) for a set outage duration or all day?

No outside power Pros:
* Eliminates extension cords and possible special power requirements.
* Voting can continue in a power outage.
* Some equipment (tablets and laptops) has a built in battery that can work during a power outage.

No outside power Cons:
* Limits the type of equipment used
* Might require special external batteries and power conversion


##### 5.3.1.10. What kind of printing technology should be used at a poll site or vote center?

Background: [TODO]

Options Include:

* Laser Printer (single/double sided)

    Pros:
    + High quality, durable printing
    + Toner lasts for a large number of pages
    + Fast printing

    Cons:
    + Requires AC power (limited life on backup power)
    + Tracking/replacing toner cartridges is required

* Ink Jet (single/double sided)

    Pros:
    + Low power
    + Available as portable battery powered COTS

    Cons:
    + Ink cartridges drain quickly and dry out between elections
    + Ink can smear before drying
    + Head cleaning might be required

* Direct Thermal (on special paper)

    Pros:
    + Low power
    + No consumables that need monitoring and reloading

    Cons:
    + Requires special paper
    + Limited life - disappearing ink
    + Temperature sensitive
    + Lower resolution

* Thermal Transfer (uses a ribbon)
    Pros:
    + Low power
    + High quality printing

    Cons:
    + Ribbon usage needs to be tracked and replaced
    + Not normally used for letter size printers


##### 5.3.1.11. What size paper should be used for precinct voting and vote by mail?

Background: Vote-by-mail ballots are typically printed on wide paper
stock (sometimes 11"x17") folded to fit within a mailing envelope.
Precinct voting with a scanner does not need to be folded, and could
be a different size than mailed ballot.

With a larger paper size, more columns could be used, larger fonts, and
fewer sheets. With a smaller paper size (8.5"x11" or 8.5"x14"),
standard printers and scanners could be used. LA County published
a [usability study][la-vsap-vbm-study] of mail ballot design including
2 paper sizes (8.5x11" and 10.5x17").

If voting machines are used to print a _paper cast vote record_, then
only the selections made are shown, so a single sheet could be used.


##### 5.3.1.12. What options should be provided to people with disabilities?

Accessible voting could be accomplished with:

* Voting machines (BMD) at all precincts
* Voting machines at selected precincts or vote centers with transportation provided
* Vote by mail using home computer and printer


##### 5.3.1.13. Should "remote accessible vote-by-mail" (RAVBM) printing used by voters with disabilities to vote by mail using home computers also be used for disability-access precinct voting?

  Background: California Election code specifies that remote accessible vote by
mail capability should be provided by 2020 for people with disabilities and
military and overseas voters. Software to prepare these RAVBM ballots could in
principle be used at a precinct poll site or early vote center. Some states have
used a similar system (e.g. Prime-III) for disability access voting at
precincts.

RAVBM used in precincts Pros: [TODO]

RAVBM used in precincts Cons: [TODO]


##### 5.3.1.14. Does ballot collection order or CVR recordings need to be randomized to protect voter privacy (be disassociated by order of appearance at a precinct)?

Background: To protect voter privacy, either the time and order of appearance
of a voter must not be recorded, or else the order of scanned or submitted
ballots must be randomized. Otherwise voter order and ballot order could
be correlated and secrecy compromized. If ballot box order must be randomized,
then poll workers might need to shuffle ballots.

Scanned ballots imprinted with an ID could have sequential number assigned,
could simplify pulling ballots with a specific ID, e.g. for a ballot
requiring adjudication, or in an audit. Otherwise, a randomly assigned
unique ID could be imprinted, and stored electronic cast vote records
could have order randomized.


##### 5.3.1.14. Should scanned ballot images or compiled CVRs be an open public record, possibly electronically accessible?

In the interest of making the election process transparent, the electronic
records of scanned ballots and/or CVRs could be made public (vs sealed
paper ballot storage containers). Is open ballot data possible within the
legal requirements of privacy and not being able to identify and prove a vote?
Would open ballot data be part of end-end verifiability or mutually exclusive
to it?

Ranked Choice Voting (RCV) might require a public set of cast vote records (CVR)
to fully disclose voter choices and validate the elimination rounds.

##### 5.3.1.15. End-to-end verifiability

[TODO: Introduction - why we want it ...]

It should be determined how much additional work would need to be done to
make the voting process end-to-end verifiable, and whether and which designs
are more compatible (e.g. among approaches listed above, hand-marked vs
machine-printed ballots). Also, is this something that could
be incorporated later on in the process, or does it need to be incorporated
from the beginning?

Is it possible to have end-end verifiability without also being able to
prove how one voted?

[TODO: List current research on E2E voting.]

### 5.4. Requirements

This section lists some of the requirements the system should satisfy.


#### 5.4.1. Accessibility

* In addition to an audio component and touchscreen, the voting system should
  support accessible features including, but not limited to: sip and puff
  input, a keyboard for write-in votes, voice activation, synchronized audio
  and video, joystick input, Tecla switch, and tactile buttons. These
  [two letters][disability-rights-ca-letters] from Mr. Fred Nisen
  (Supervising Attorney for Voting Rights, Disability Rights California)
  provide more detail.


#### 5.4.2. Other

* [TODO: should we recommend (1) supporting manually marked ballots in the
  polling place, or (2) requiring the use of a computer ballot-marking and/or
  ballot-printing device?]

* [TODO: should we recommend (1) pre-printed ballots at polling places, or
  (2) printing ballots on-demand?]

* [TODO: should we recommend for or against end-to-end verifiability?]


### 5.5. Project Management

* The Department should align itself with other efforts within the City to
  use agile procurement and methods, and it should seek assistance where
  possible. Notable parts of San Francisco government beginning to use agile
  methods include the San Francisco [Mayor’s Office of Civic
  Innovation][sf-moci] (MOCI) and the San Francisco [Digital Services
  Team][sf-dst]. See also San Francisco's [_Digital Services
  Strategy_][sf-digital-services-strategy] (PDF).

  _[Item added: Dec. 14, 2017 meeting.]_

* Developing user stories is an essential part of an agile development
  process. We recommend that the development team create user stories for
  each of the situations representing voter, Department staff, and other
  activities. These user stories include, among others:

  1. a registered voter voting at an assigned precinct on election day;

  2. a registered voter voting at a vote center or early voting station;

  3. a registered voter voting remotely and mailing in a marked ballot, and;

  4. a registered voter with a disability in need of special accommodation
     (several types).

  In following an agile development process, the implementation team would
  typically break down each user story into smaller stories as needed, and
  handle one of those within a sprint.

  _[Item added: Jan. 18, 2018 meeting.]_

* The Department should hire a staff person to be in charge of managing the
  project. The person should have experience and expertise in managing
  technical projects of a similar size and complexity.

* As soon as possible, the Department should
  develop and publicize a rough project plan and timeline for the development
  and certification of an open source system, for the case that the project
  is funded. It is okay for this plan to be tentative. It can be refined over
  time as more information becomes available. Articulating even a tentative
  plan would also help in crafting an RFP for the interim system.

* For deliverables, favor smaller deliverables that can be tested
  independently of other components. In particular, if developing a software
  application, it may make sense for one or more of the underlying libraries
  to be delivered separately and/or earlier, rather than the application as a
  whole being the only software deliverable.

  One example is an application to tabulate the results of an RCV contest.
  The code responsible for running the algorithm could be delivered and
  tested as a stand-alone library separate from any user-interface.

  Another example is an application to adjudicate ballots. The code for
  automatically interpreting the digital ballot picture could be separated
  out as its own library. Indeed, this corresponds to the Ballot Picture
  Interpreter software component.

  [TODO: add a comment about the vendor providing a UI shim to support
  the testing of software libraries.]

* [TODO: think about the division of responsibilities between the City and
  vendor. For example, who should be responsible for project management—the
  City or a vendor?]

* [TODO: provide specific recommendations around agile.]


### 5.6. Open Source

This section covers topics related to open source.

* Each software component being developed should be licensed under an
  [OSI-approved][osi-approved-licenses] software license, with a copyleft
  license being preferred (see also the Facts & Assumptions section).

* All software development should occur in public (e.g. on GitHub), rather
  than, for example, waiting for the software to reach a certain level of
  completion before becoming public.
  (See also item (b) of the third "resolved" paragraph of the Commission's
  [Open Source Voting Resolution][commission-resolution-local].)

* All software being developed in public should have an open source license
  when development first starts, rather than, for example, adding a license
  file later on. This would eliminate any confusion and uncertainty from
  members of the public as to whether the software will really be open
  source. This would encourage members of the public to start contributing to
  the project as early as possible.

* All software being developed should be developed using an open source
  programming language and toolchain. This means an open source compiler
  or runtime should be available for the language(s) used, and it should
  be possible to build and run the software from source using only open source tools.
  For programming languages and build tools, any OSI-approved license
  should be okay; they need not be copyleft.

* Reuse of existing open source libraries, tools and software is encouraged.
  Any such pre-existing third-party code used should be available under
  an OSI-approved license, but need not be copyleft. If modifications to
  third-party code are developed, and the original third-party code has
  a different license than the main software's license, the modifications
  should be dual-licensed under both licenses, if possible.
  (See also item (e) of the third "resolved" paragraph of the Commission's
  [Open Source Voting Resolution][commission-resolution-local].)

* The aggregate system (including the infrastructure, stack, and services)
  should be open source. This includes but is not limited to things like
  the operating system, database, web server, etc, if present.

* In addition to the software being open source, project documentation
  should be openly licensed. This includes things like design documents,
  installation and setup documents, user manuals, and testing documents.
  The recommended license for documentation is the Creative Commons
  Attribution-ShareAlike 4.0 license ([CC-BY-SA 4.0][cc-by-sa]).
  (See also the reference to ”freely and openly licensed” documentation
  in the Commission's
  [Open Source Voting Resolution][commission-resolution-local].)

* [TODO: provide recommendations related to managing community feedback and
  contributions during project development. Also think about whether
  [contributor license agreements][cla] (CLA’s) should be required.]


### 5.7. Procurement

[TODO]


### 5.8. Software architecture and design

* When defining software components to develop, favor designs that promote
  reusing components. For example, a software library that can read a digital ballot
  picture and return the marked “votes” (what we are calling a “ballot picture
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

1. **Gather real election data.** Datasets of real election data (e.g. a
couple past elections in San Francisco of different types) should be compiled
in a structured format for product prototyping and testing. This includes not
just vote totals but also candidate and contest data. This will help in
establishing requirements and designing the system.

2. **Gather real digital ballot pictures.** Starting with the June 2018
election, during each election the Department should gather and save large
numbers (e.g. thousands) of digital ballot pictures for future testing
purposes. The Director has already expressed a willingness to do this in the
case that the voting system supports it. The Department should do this during
the canvass after each election because it may not be possible to obtain
ballot pictures after the ballots are physically sealed and eventually
destroyed. Having a variety of real-world digital ballot pictures will aid in
developing and testing the ballot picture interpreter component, even if the
ballot design is different from what will eventually be used. Also, using
real ballots can provide test cases that might not be thought of if trying to
construct test cases manually.

   _[Item added: Dec. 14, 2017 meeting.]_

3. **Stand-alone test data.** In the course of developing the open source
voting system, where possible, structure and store test data separate from
the software application (e.g. in separate repositories) and in an
application-agnostic form (e.g. using open data formats). These can be
separate deliverables. The test data
should include both test inputs and, when appropriate, test outputs (aka test
expectations). Doing this allows the test data to be used by other
applications and in particular could help facilitate additional open source
implementations of components. Making the test data independent and more
easily available can also improve the quality and correctness of the test
data, for example by making it easier for others to check or add more test
cases.

   This recommendation makes more sense for higher level end-to-end tests rather
than lower-level tests like unit tests since unit tests are often tied to a
particular implementation. Examples of test cases for higher-level tests
include things like (1) for the ballot picture interpreter component, a
digital ballot picture as the input and the corresponding cast vote record as
the output, and (2) for the RCV tabulator, the cast vote records for an RCV
contest as the input and the round-by-round vote totals as the output.

   _[Item added: Dec. 14, 2017 meeting.]_


### 5.14. Certification

[TODO]


### 5.15. Hardware manufacturing or assembly

[TODO]


### 5.16. Deployment

[TODO]


### 5.17. Software maintenance

[TODO]


### 5.18. Hardware maintenance

* The City should prefer professional, commercial support for
  maintaining the aggregate system (including the operating system, stack,
  and software services, etc.) over “in-house“ maintenance -- even though
  the components are open source. This will make it easier, for example,
  to ensure that security patches are applied on a timely basis. An example
  of such a provider is [Red Hat](https://www.redhat.com).
