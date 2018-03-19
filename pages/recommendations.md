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

[TODO]


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
  [Open Source Voting Systems Resolution (PDF)][commission-res-pdf-local].)

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
  [Open Source Voting Systems Resolution (PDF)][commission-res-pdf-local].)

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
  [Open Source Voting Systems Resolution (PDF)][commission-res-pdf-local].)

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
