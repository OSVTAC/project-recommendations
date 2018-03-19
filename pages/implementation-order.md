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


### 7.1. Recommended First Components

The Committee recommends the following as components to start work on and
deliver first (see the “Components” section for brief descriptions of
most of these components):

1. Results Reporter (Software)
2. Vote Totaler (Software)
3. Ballot Picture Interpreter (Software)
4. Central Ballot Scanner (Hardware & Software)
5. Ballot Layout Encoder (Software)
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


### 7.2. Rationale

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


### 7.3. Results Reporter Rationale

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


### 7.4. Vote Totaler Rationale

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


### 7.5. Central Ballot Scanner Rationale

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


### 7.6. Deployment Strategies

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


### 7.7. Central Ballot Scanner Phases

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
