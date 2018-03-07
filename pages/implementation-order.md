## 7. Recommended Implementation Order

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

**Description.** This is a software-only component responsible for
interpreting digital ballot pictures, namely by generating a cast vote record
(CVR) given a digital picture of a ballot. The component must support ballots
from “third-parties” (e.g. the interim voting system) to support incremental
roll-outs like pilot and hybrid rollouts, and possibly to support
home-printed "remote accessible vote by mail" ballots. The open source
software OpenCount developed at UC Berkeley could be a foundation for this.

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
