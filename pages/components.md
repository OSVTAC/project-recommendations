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

**9\. Results Reporter**

Generates human-readable results reports from the results data from the vote
totaler (e.g. printable results and results posted on the Department website).
