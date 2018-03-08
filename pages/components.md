## 5. Components

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
in this section. They were made partly because they reflect how San
Francisco's voting system works today. However, they should not be construed
in any way as recommendations of the Committee or to constrain the type of
voting system that San Francisco should develop. See the "Key Decisions"
section below for how this list of components could change depending on
certain choices.

The components in this particular list are not necessarily independent. They
may overlap or contain one another. For example, the precinct ballot scanner
hardware component contains a scanner device driver, the ballot picture
interpreter, and the high-level scanner software components.

Finally, note that there are many possible ways to divide a given voting
system into components. For example, the granularity at which one views the
system affects the number of components. We chose a mid-level granularity for
this list. This lets us show how some software components are used in more
than one hardware component. Differences can also result from where the
“boundaries” are drawn between components (e.g. what functionalities one
assigns to different components).


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


##### 3.2.2.1. Hardware Components

Each of the hardware components below also needs software to function. In
most cases, we list this software in the “Software Components” section.

**1\. Accessible Ballot-Marking Device**

A device used in polling places that lets people with disabilities vote
independently. It supports different accessible interfaces like audio,
sip-and-puff, etc. If the computer is COTS, it may also need a custom casing
or shell to increase durability and assist with polling-place transport and
setup.

For a Remote Accessible Vote By Mail system (required by 2020), the
hardware used would likely be the voter's personal electronic
device and printer.

_[Item edited: Jan. 18, 2018 meeting.]_

**2\. Central Ballot Scanner**

A device responsible for high-speed, high-volume ballot scanning (e.g. for
vote-by-mail ballots). The scanning with these machines is done in a
controlled environment under staff supervision.

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


**3\. Precinct Ballot Scanner**

A device used in polling places to scan and tabulate ballots cast in person.
It has features like returning the ballot to the voter for possible
correction if the ballot contains an overvote. Similar to the accessible
device, this device may also need a custom casing or shell for durability and
to facilitate polling-place use.

**4\. Standard laptop or desktop computers**

Standard computers will also be needed for administrative tasks like ballot
layout, adjudicating digital pictures of ballots, aggregating and totaling
votes, and generating results reports.


##### 3.2.2.2. Software Components

**1\. Voting System Database / Management**

Central store (e.g. file system and/or database) and software application
providing access to the voting-system information needed to conduct an
election. This can include things like contest and ballot definitions,
digital ballot pictures, cast vote records, and election results.

A management interface can let staff perform
tasks like importing and exporting data in open data formats, adjudicating
ballots that require manual inspection (e.g. ballots with write-in candidates
or borderline marks)—but from the digital ballot picture rather than from
the physical paper—and performing other
functions needed during the canvass. This software could perhaps also
provide an interface to running other software components and functions
like the EIMS integration, tabulation, and results reporting.


**2\. Ballot Batch Management**

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


**2\. EIMS® Integration.**

This component is responsible for interfacing with the Department's EIMS®
software. It pulls or takes election definition information exported from
EIMS and imports it into the voting system database. This information can
include things like what offices and candidates are on the ballot, and
in what precincts, districts, and ballot styles, etc.

**3\. Ballot Layout**

This is a software application that lets staff generate paper-ballot layouts
from the election definition for each ballot type in automated or
semi-automated fashion, including support for multiple languages.


**4\. Ballot Layout Analyzer**

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


**4\. Accessible Ballot-Marking Device Software**

This is the software corresponding to the Accessible Ballot-Marking Device
hardware component.

A Remote Accessible Vote By Mail system would likely rely on a reasonably
updated web browser rather than requiring installation of OS-specific
software installation. Text to speech capabilities could be either the
voter's own accessibility software or a web browser component provided
with the ballot.

_[Item edited: Jan. 18, 2018 meeting.]_

**5\. Ballot Picture Interpreter**

This is a software library responsible for interpreting digital ballot pictures. It
generates a cast vote record (CVR) from a digital picture of a ballot. This
software component could potentially be used in all of the precinct scanners,
the central scanners, and a software-only ballot adjudication application.

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


**6\. Scanner Device Drivers (one for precinct and one for central)**

This is low-level software needed on both precinct and central ballot
scanners that provides a software API to the basic hardware functionality of
a ballot scanner (e.g. out-stacking a ballot, returning a ballot, advancing a
ballot, etc.). This might come with COTS hardware. Separate versions are
likely needed for the precinct and central scanners.

**7\. Central Ballot Scanner Software**

This is high-level software controlling the central ballot
scanner. It interacts with the scanner device driver and ballot picture
interpreter components and is responsible for things like scanning and
storing digital ballot pictures, detecting the ballot layout, interpreting and
tabulating ballot markings, controlling the scanner in response to the
markings on a ballot, and exporting ballot data after scanning is complete.

**8\. Precinct Ballot Scanner Software**

This component is similar to the central ballot scanner software component
above and can likely share much software with it. However, it's different
because it is for the case of an individual voter rather than for high-volume
scanning. For example, unlike the central ballot scanner, this software will
need to support returning a ballot back to the voter in the case of errors
like an overvote. For the central scanner, such ballots might simply be
outstacked.

**8\. Vote Totaler**

Aggregates and counts all vote totals and generates the results in an open
data format. Includes the RCV tabulation algorithm.

**Complexity:** Low

**Description.** This is a software-only component responsible for
aggregating vote data and generating election results in a machine-readable
format. This includes running the RCV algorithm to generate round-by-round
results. Normally votes have subtotals reported by consolidated precinct, and
may separate election-day precinct voting and vote-by-mail ballot subtotals.

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


**9\. Results Reporter**

Generates human-readable results reports from the results data from the vote
totaler (e.g. printable results and results posted on the Department website).

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


**13\. Ballot Tabulation Audit Support**

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
