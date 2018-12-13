## 8. Equipment (“Product”) Decisions

The following are some key decisions about system requirements that need to be made
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
  + Vote by people preferring or needing an accessible option (e.g. ballot
    marking device), like people with disabilities
  + Vote with Provisional Ballots (enclosed in a special envelope for later
    qualification)

_[Assumptions added: Feb. 8, 2018 meeting.]_


### 8.1. Will vote centers be used for early and/or election day voting?

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

Vote centers could be used for:
   1. Early voting only
   2. Election day voting at selected locations
   3. All election day polling locations

_[Answer edited: Feb. 8, 2018 meeting.]_


### 8.2. Should precinct polling and vote centers use the same paper ballots as those used in vote-by-mail?

  Background: If a voting machine is used to prepare ballots for printing, the
paper ballots marked could use the same printing and layout as a vote-by mail
ballot, or could have a simpler and shorter format listing just the contests and
selected choices (called _paper cast vote record_ (CVR) in California Election Code).
The shorter format could be on smaller paper, possibly only a single sheet, vs a
larger multipage scanned mail ballot. Voting machines (ballot marking devices)
at a precinct or vote center could be used only for the purposes of providing
an accessible option, while voters not requiring an accessible option could
use a normal mail ballot, or all voters at a precinct or vote center could
use voting machines with printed ballots.

Mail-Only Format Pros:

* Only one style of ballot printing is required
* No need for precinct voters to use voting machines-- voters not
    requiring an accessible option can use a "low-tech" solution of only
    a marker or pen
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


### 8.3. Should ballots to be hand-marked be preprinted or printed on demand?

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


### 8.4. Should voting at a precinct or vote center be primarily based on paper ballots hand-marked with a pen, or voting machine with a printer?

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
* Eliminates errors like overvotes and ambiguous marks requiring adjudication.
* Ranked Choice contests can have rankings for all candidates, vs a limit
on paper ballots, eliminating exhausted ballots (except from undervotes), while paper ballots typically have limits.
* Eliminates ambiguous marks that would otherwise require adjudication.
* Machines could read a QR code from a vote at home app to print a ballot
  immediately.
* A separate non-mail ballot format from voting machines would be the same
  for ordinary voters and those with special needs.
* It will be easier to ensure that all voters have the same level and
  quality of experience if all voters use the same process.
* Extra machines provide redundancy vs a single accessible machine.
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

_[Question & answer edited: April 12, 2018 meeting.]_


### 8.5. If voters use machines to mark ballots, should the machine store CVRs of the marked selections?

Background: When a machine is used by voters to select choices that are
then printed on a voter verified ballot, the machine could save the
printed choices as a Cast Vote Record. CVRs could then be used as an audit record
or for unofficial election night results. (Actually the machine might
store vote records with uncertain cast status, so they would need to be linked
to a scan of an ID for a ballot when cast and inserted into the ballot box.)

The recommendation is for the voter-verified paper ballot to be the
official record counted. However, machine-stored CVRs could be used as
official data if validated by a 100% scan of the cast paper record, or
else a reliable audit of the paper record.

Voting machine stored CVRs Pros:
* Provides a separate audit record created on election day
* Digital signatures can prove data was created by that machine on election day
* Preliminary results can be obtained without needing to scan ballots
* Combining electronic and paper records is more secure, because they authenticate each other

Voting machine stored CVRs Cons:
* Need ballot ID scan to distinguish a cast CVR from discarded CVR
* Need to collect data from each machine, possible extra hardware
* Extra high-sensitivity software might be needed
* More digital security required; not storing CVRs would mean not having to digitally secure them

_[Question added: May 9, 2018 meeting.]_


### 8.6. Should a machine-marked ballot contain a bar code with a digital signature and/or CVR?

Background: Machines that record voter selections and print a ballot can
easily add a bar code (e.g. 2D QR code) that could contain a digital
signature of the electronic representation of the printed choices,
possibly with the electronic CVR. A digital signature would function
as a check for accurate interpretation of a scanned ballot, and also
could validate the printout as being created on a particular machine
on election day (or early voting period). The signature prevents anyone
from replacing the paper ballot with a substitute, provided appropriate
digital signature protocols are implemented.

The electronic CVR could be printed as a bar code as well, either as
a separate check or to assist the optical scan interpretation.

\[Note, a digital signature could be printed as text, e.g. base64 letters
and numbers, but a pile of numbers is no more human readable than a bar code.]

Ballots with digital signature bar codes Pros:
* Prevents tampering of paper ballots, either alterations or substitution
* Proves this paper was printed by a particular machine on particular day(s)

Ballots with digital signature bar codes Cons:
* Some people dislike (do not trust) printing that is not human readable and verifiable

_[Question added: May 9, 2018 meeting.]_


### 8.7. If voting machines are used at a precinct, should there be one printer per voting station?

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


### 8.8. If voters at precincts use hand-marked ballots, should ballots be scanned centrally or at the precinct/vote center?

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


### 8.9. If a precinct scanner is used, does the scanner need to be integrated with a ballot collection bin?

  Background: Custom-built precinct ballot scanners sold by election vendors
usually include a ballot collection bin within same box containing the scanner.
The scanner feeds the ballot into the collection box, or else reverses the paper
feed in case of an error detected. Scanners may need multiple collection bins
in case of ambiguous marks or write-in votes. An integrated device likely
means custom hardware vs COTS equipment.

_[Question added: Feb. 8, 2018 meeting.]_


### 8.10. If a precinct scanner (or central scanner) is used, does it need to include an imprinter to record a ballot/scan ID?

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


### 8.11. If a voting machine is used to print all precinct ballots and possibly save CVRs, does the ballot collection box need to have an integrated scanner?

Background: Using a voting machine with voter-verified ballot does not
constitute casting a ballot-- the act of submitting the ballot after
verification is the cast ballot. Voters might choose to discard a ballot and
revote, so a simple bar-code scanner is useful to match the electronic CVR with
paper ballots submitted (i.e. exclude discarded ballots). Discarded ballots
could be scanned instead, but a voter could still walk off with a ballot, or a
ballot might not print correctly.

(The LA County VSAP integrates the voting machine, printer, and ballot collection bin. The printer has a bar code scanner to read the ballot type on blank ballot paper and to re-read the ballot ID (to match with a CVR) as it enters the integrated ballot box.)

Whether or not an electronic CVR exists within the voting machine, it may still be
useful to have a full scanner at the precinct, so all CVRs are derived from
the scanned paper read by the voter, and scanned images are available immediately
at the end of election day. However, without a full precinct scanner, vote
totals would still be available at the end of the day, and a central scanner
could be used after the election for a 100% audit of paper ballots (paper CVRs).

If only machine-printed ballots are collected (no undervote/overvote/ambiguous
mark detection is required), then a simple plain COTS scanner could be used
to feed the ballot paper in the collection bin, only recording the ballot images.

Additional ballot box scanner Pros:

* CVRs are derived from the paper verified by voters, not an indirect stored CVR (one criticism of "Voter Verified Paper Audit Trail" is that the human-read paper record is typically not 100% checked)

* Scanned ballot images can be recorded during the election and available
immediately afterwards.

* Voting machines and scanners could use independent equipment and software,
increasing security.

* Precinct scanners for casting voting-machine printed ballots could also be
used to scan vote-by-mail (hand-marked) ballots.

* A precinct scanner could be used with text-to-speech to read back a ballot
for the visually impaired.

Additional ballot box scanner Cons:

* Additional equipment is required which is in theory, unnecessary.

* A full scanner capable of error detection on hand-marked ballots might
require custom hardware (not COTS) for integration with a collection bin.
A simplified scanner that only can feed into the ballot box could be COTS.

_[Question & answer edited: April 12, 2018 meeting.]_


### 8.12. Is voting equipment required to run off a battery (without outside AC power) for a set outage duration or all day?

No outside power Pros:
* Eliminates extension cords and possible special power requirements.
* Voting can continue in a power outage.
* Some equipment (tablets and laptops) has a built in battery that can work
  during a power outage.

No outside power Cons:
* Limits the type of equipment used
* Might require special external batteries and power conversion

_[Question added: Feb. 8, 2018 meeting.]_


### 8.13. What kind of printing technology should be used at a poll site or vote center?

Background: There are many options for COTS and custom printers, including
several options for printing technology. Each option has different tradeoffs
in power requirements, consumables (ink, toner, etc.), an types of paper
supported.

There is not necessarily a requirement that the printing technology be the
same across all locations. For example, a vote center might use a laser printer
for printing ballots on demand whereas a voting machine at a precinct might
use a thermal printer running off a battery.

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

_[Question added: Feb. 8, 2018 meeting; edited April 12, 2018 meeting.]_


### 8.14. What size paper should be used for precinct voting and vote by mail?

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


### 8.15. What options should be provided to people with disabilities?

Accessible voting could be accomplished with:

* Voting machines (BMD) at all precincts (or vote centers) and early
  voting stations
* Voting machines at selected precincts or vote centers with transportation
  provided (Question: is this really permitted?)
* Vote by mail using home computer and printer

_[Question added: Feb. 8, 2018 meeting.]_


### 8.16. Should "remote accessible vote-by-mail" (RAVBM) printing used by voters with disabilities to vote by mail using home computers also be used for accessible precinct voting?

  Background: California Election code specifies that remote accessible vote by
mail capability should be provided by 2020 for people with disabilities and
military and overseas voters. Software to prepare these RAVBM ballots could in
principle be used at a precinct poll site or early vote center. Some states have
used a similar system (e.g. Prime-III) for disability access voting at
precincts.

RAVBM used in precincts Pros:

* Simplifies the software-- a single accessible voting software system is required
both for accessible vote-by-mail and precinct voting. Likewise scanner software for
reading RAVBM ballot paper would be reused for precinct voting.

* An RAVBM system must be usable with home COTS hardware, so only COTS hardware
would be needed to implement accessible precinct voting.

RAVBM used in precincts Cons:

* The hardware and software used by RAVBM would probably not be considered as secure as smaller and more specialized software running on a secure microcomputer.

* RAVBM ballots might require a paper size different from other precinct ballots. (Although Prime-III as modified by NH could print on hand-marked ballot paper.)

_[Question added: Feb. 8, 2018 meeting; edited April 12, 2018 meeting.]_


### 8.17. Does ballot collection order or CVR recordings need to be randomized to protect voter privacy (be disassociated by order of appearance at a precinct)?

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


### 8.18. Should scanned ballot images or compiled CVRs be an open public record, possibly electronically accessible?

In the interest of making the election process transparent, the electronic
records of scanned ballots and/or CVRs could be made public (vs sealed
paper ballot storage containers). Is open ballot data possible within the
legal requirements of privacy and not being able to identify and prove a vote?
Would open ballot data be part of end-end verifiability or mutually exclusive
to it?

Ranked Choice Voting (RCV) might require a public set of cast vote records (CVR)
to fully disclose voter choices and validate the elimination rounds.

_[Question added: Feb. 8, 2018 meeting.]_


### 8.19. End-to-end verifiability

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
