## 6. FAQ

**1. Is open source software more or less secure than proprietary
software?**

Independent studies have shown that, in general, open source software is
neither more secure nor less secure than proprietary software (see for
example Synopsys's ["Coverity® Scan Open Source Report
2014"][coverity-report-2014]). Both secure and insecure open source software
can be written. Similarly, both secure and insecure proprietary software can
be written.

A key difference though is that, because it is publicly viewable, claims
about the security of open source software can be _independently verified_,
and by _anyone_ (provided they have the necessary skills and time). With
proprietary code, such claims can be based only on trusting those who are
able to view the code.

The security of a given piece of software is primarily a function of how well
the software is written. It does not (and should not) depend on keeping the
code secret. The idea that software can be made secure by keeping it secret
is an idea known as "security by obscurity" and is widely rejected in the
security community.

Open source is already heavily used and relied upon throughout the world for
security-critical applications. For example, much of the code that allows
the secure transmission of information over the internet is open source.

**2. How can members of the public be sure that the open source code is
what is actually running on the machine?**

The short answer is that there is no way to be certain that the code
running on a particular device or computer is what one expects it to be
(whether the software is open source or not). This is true even if very
careful measures are taken. This is an extremely hard problem to solve and
is an active area of research. One reason is that there is no way to be
sure that the computer hardware itself can be trusted.

Having said that, good auditing practices that involve randomly checking
computer results by hand against the original paper ballots are an adequate
countermeasure, provided the audits are done correctly. This is why good
audit procedures are important when computers are used to count ballots.

_[Answer added: Dec. 14, 2017 meeting.]_

**3. How much of the code must be open source for the voting system to
be considered open source?**

Whether something is open source or not is best answered not as a yes or
no question but as a matter of degree.  For example, a hardware device could
be 99% open source except for one small bit of proprietary firmware.

In general, our committee recommends the approach of trying to maximize
the amount of open source -- i.e. the more open source, the better.
There is no fundamental reason why the entire voting system can't be open
source. However, if some portion isn't open source, it is better if that
portion is as small as possible and if it's for optional functionality
rather than required functionality.

Also, if the eventual system does contain any non-open source code, in
the spirit of agile, one could work to replace that code with an open source
equivalent in later versions of the system.

_[Answer added: Dec. 14, 2017 meeting.]_
