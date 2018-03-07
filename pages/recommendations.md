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

* An electronic representation of ballots made either by voting machines or
  scanners serves only as a copy of the official paper ballot.

* Ballots marked are on paper that meets the California regulations for
  printing (counterfeit resistance).

* By 2020, CA [AB973][bill-ab-973-2017] requires support of _Remote Accessible
Vote By Mail_ ballots ([AB2252][bill-ab-2252-2015]) for voters with disabilities
or overseas and military voters. Home computers are used to print ballots on
ordinary paper, but returned via special mail envelopes.

* Voting types to be considered:
  + Vote by mail (preprinted and special accessible/overseas)
  + Vote on election day at a polling location (precinct voting)
  + Vote prior to election day at an early vote center
  + Vote by people with disabilities requiring special equipment (ballot
    marking device)
  + Vote with Provisional Ballots (enclosed in a special envelope for later
    qualification)

_[Assumptions added: Feb. 8, 2018 meeting.]_


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

_[Answer edited: Feb. 8, 2018 meeting.]_


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
* Reduced requirements for printers and possible problems with printer
  malfunction and paper jams.
* Voting with hand-marked ballots could be done with no electric power.

Mail-Only Format Cons:
* Printing on large mail ballot paper, usually double sided,  requires
    special, possibly nonstandard, equipment. Sheets might need to be
    hand-inserted individually.

_[Question added: Feb. 8, 2018 meeting.]_


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
* Printing on large mail ballot paper, usually double sided requires special,
  possibly nonstandard, equipment.

_[Question & answer edited: Feb. 8, 2018 meeting.]_


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
* Paper+Electronic CVR has the highest security/integrity. Digital signatures
  can be printed on ballots to authenticate paper.
* Time to vote can be less than marking.
* Mistakes can be undone without needing another ballot to mark.
* Machines could read a QR code from a vote at home app to print a ballot
  immediately.
* A separate non-mail ballot format from voting machines would be the same
  for ordinary voters and those with special needs.
* Extra machines provide redundancy vs a single disability-access machine.
* Vote centers could handle all ballot types without the need for a ballot
  on demand system.
* Election-day machines could only allow authorized write-ins to be recorded,
  simplifying write-in voting and enabling end of day totals that include
  write-ins.
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

_[Question & answer edited: Feb. 8, 2018 meeting.]_


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

_[Question added: Feb. 8, 2018 meeting.]_


##### 5.3.1.6. If voters at precincts use hand-marked ballots, should ballots be scanned centrally or at the precinct/vote center?

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

_[Question added: Feb. 8, 2018 meeting.]_


##### 5.3.1.7. If a precinct scanner is used, does the scanner need to be integrated with a ballot collection bin?

  Background: Custom-built precinct ballot scanners sold by election vendors
usually include a ballot collection bin within same box containing the scanner.
The scanner feeds the ballot into the collection box, or else reverses the paper
feed in case of an error detected. Scanners may need multiple collection bins
in case of ambiguous marks or write-in votes. An integrated device likely
means custom hardware vs COTS equipment.

_[Question added: Feb. 8, 2018 meeting.]_


##### 5.3.1.8. If a precinct scanner (or central scanner) is used, does it need to include an imprinter to record a ballot/scan ID?

  Background: To match a specific paper ballot in a ballot box with a scanned
CVR, either the order of insertion must be maintained, or a unique identifier
associated with the scan needs to be added to the ballot. Alternatively,
ordered ballots could be rescanned centrally during a recount or audit and
matched as a batch with the original scan.

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

_[Question & answer edited: Feb. 8, 2018 meeting.]_


##### 5.3.1.9. If a voting machine is used to print ballots, does the ballot collection box need to have an integrated scanner?

  Background: Using a voting machine with voter-verified ballot does not
constitute casting a ballot-- the act of submitting the ballot after
verification is the cast ballot. Voters might choose to discard a ballot and
revote, so a simple bar-code scanner is useful to match the electronic CVR with
paper ballots submitted (i.e. exclude discarded ballots). Discarded ballots
could be scanned instead, but a voter could still walk off with a ballot, or a
ballot might not print correctly.

Additional ballot box scanner Pros: [TODO]

Additional ballot box scanner Cons: [TODO]

_[Question added: Feb. 8, 2018 meeting.]_


##### 5.3.1.10. Is voting equipment required to run off a battery (without outside AC power) for a set outage duration or all day?

No outside power Pros:
* Eliminates extension cords and possible special power requirements.
* Voting can continue in a power outage.
* Some equipment (tablets and laptops) has a built in battery that can work
  during a power outage.

No outside power Cons:
* Limits the type of equipment used
* Might require special external batteries and power conversion

_[Question added: Feb. 8, 2018 meeting.]_


##### 5.3.1.11. What kind of printing technology should be used at a poll site or vote center?

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

_[Question added: Feb. 8, 2018 meeting.]_


##### 5.3.1.12. What size paper should be used for precinct voting and vote by mail?

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

_[Question added: Feb. 8, 2018 meeting.]_


##### 5.3.1.13. What options should be provided to people with disabilities?

Accessible voting could be accomplished with:

* Voting machines (BMD) at all precincts
* Voting machines at selected precincts or vote centers with transportation provided
* Vote by mail using home computer and printer

_[Question added: Feb. 8, 2018 meeting.]_


##### 5.3.1.14. Should "remote accessible vote-by-mail" (RAVBM) printing used by voters with disabilities to vote by mail using home computers also be used for disability-access precinct voting?

  Background: California Election code specifies that remote accessible vote by
mail capability should be provided by 2020 for people with disabilities and
military and overseas voters. Software to prepare these RAVBM ballots could in
principle be used at a precinct poll site or early vote center. Some states have
used a similar system (e.g. Prime-III) for disability access voting at
precincts.

RAVBM used in precincts Pros: [TODO]

RAVBM used in precincts Cons: [TODO]

_[Question added: Feb. 8, 2018 meeting.]_


##### 5.3.1.15. Does ballot collection order or CVR recordings need to be randomized to protect voter privacy (be disassociated by order of appearance at a precinct)?

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

_[Question added: Feb. 8, 2018 meeting.]_


##### 5.3.1.16. Should scanned ballot images or compiled CVRs be an open public record, possibly electronically accessible?

In the interest of making the election process transparent, the electronic
records of scanned ballots and/or CVRs could be made public (vs sealed
paper ballot storage containers). Is open ballot data possible within the
legal requirements of privacy and not being able to identify and prove a vote?
Would open ballot data be part of end-end verifiability or mutually exclusive
to it?

Ranked Choice Voting (RCV) might require a public set of cast vote records (CVR)
to fully disclose voter choices and validate the elimination rounds.

_[Question added: Feb. 8, 2018 meeting.]_


##### 5.3.1.17. End-to-end verifiability

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

_[Question & answer edited: Feb. 8, 2018 meeting.]_


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
  programming language and toolchain. This means an open source compiler or
  runtime should be available for the language(s) used, and it should be
  possible to build and run the software from source using only open source
  tools. For programming languages and build tools, any OSI-approved license
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
