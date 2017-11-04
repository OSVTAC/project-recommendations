# Open Source Voting System Project Recommendations

(Approved by OSVTAC on October 19, 2017.)

Last update: November 4, 2017


**Note: these recommendations are a work in progress and not yet complete.**

This document contains the recommendations of San Francisco's [Open Source
Voting System Technical Advisory Committee][osvtac] (OSVTAC, or TAC) for
the City and County of San Francisco's open source voting system project, as
of the version date that appears above.

The committee started this document on August 30, 2017 and will continue to
work on it over time. Substantive updates to this document occur by a vote of
the committee at a committee meeting. Meetings occur approximately once a
month.

To learn more about the committee, visit the committee's website at
[https://osvtac.github.io][osvtac]. To learn how to suggest changes to this
document, view the "Project Recommendations" section of the [About
page][osvtac-about-recs] of the committee's website.


* [Single-page version](single-page) (long, can be used for printing)

## Contents

* [1. Goals](goals#1-goals)
  * [1.1. Scope](goals#11-scope)
  * [1.2. Priorities](goals#12-priorities)
  * [1.3. Non-goals](goals#13-non-goals)
* [2. Background](background#2-background)
  * [2.1. History of Open Source Voting in San Francisco](background#21-history-of-open-source-voting-in-san-francisco)
  * [2.2. Voting System](background#22-voting-system)
  * [2.3. Other Voting System Projects](background#23-other-voting-system-projects)
  * [2.4. Resources](background#24-resources)
* [3. Facts & Assumptions](facts-assumptions#3-facts--assumptions)
  * [3.1. Facts](facts-assumptions#31-facts)
  * [3.2. Assumptions](facts-assumptions#32-assumptions)
* [4. Recommendations](recommendations#4-recommendations)
  * [4.1. Interim Voting System](recommendations#41-interim-voting-system)
  * [4.2. Incremental Approach](recommendations#42-incremental-approach)
  * [4.3. Requirements-gathering](recommendations#43-requirements-gathering)
  * [4.4. Requirements](recommendations#44-requirements)
  * [4.5. Project Management](recommendations#45-project-management)
  * [4.6. Open Source](recommendations#46-open-source)
  * [4.7. Procurement](recommendations#47-procurement)
  * [4.8. Software architecture and design](recommendations#48-software-architecture-and-design)
  * [4.9. Software development](recommendations#49-software-development)
  * [4.10. Hardware design](recommendations#410-hardware-design)
  * [4.11. Documentation](recommendations#411-documentation)
  * [4.12. Security](recommendations#412-security)
  * [4.13. Testing](recommendations#413-testing)
  * [4.14. Certification](recommendations#414-certification)
  * [4.15. Hardware manufacturing or assembly](recommendations#415-hardware-manufacturing-or-assembly)
  * [4.16. Deployment](recommendations#416-deployment)
  * [4.17. Software maintenance](recommendations#417-software-maintenance)
  * [4.18. Hardware maintenance](recommendations#418-hardware-maintenance)
* [5. FAQ](faq#5-faq)
* [6. Glossary](glossary#6-glossary)


[18f-modular-contracting]: https://modularcontracting.18f.gov/
[bill-ab-2252-2015]: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201520160AB2252
[bill-sb-360-2013]: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201320140SB360
[bill-sb-450-2015]: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201520160SB450
[board-of-supervisors]: http://sfbos.org/
[bos-open-source-voting-res]: files/BOS_Resolution_460-14_Open_Source_Voting.pdf
[bos-ordinance-vstf]: files/BOS_Ordinance_268-08_VSTF.pdf
[cavo]: http://www.cavo-us.org/index.html
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[cla]: https://en.wikipedia.org/wiki/Contributor_License_Agreement
[coit]: http://sfcoit.org/
[colorado-rla-home]: http://bcn.boulder.co.us/~neal/elections/corla/
[colorado-rla-repo]: https://github.com/FreeAndFair/ColoradoRLA
[commission-osvtac]: http://sfgov.org/electionscommission/osvtac
[commission-resolution-local]: files/SF_Elections_Comm_Open_Source_Voting_Res.pdf
[commission-resolutions]: http://sfgov.org/electionscommission/motions-and-resolutions
[coverity-report-2014]: http://go.coverity.com/rs/157-LQW-289/images/2014-Coverity-Scan-Report.pdf
[dfm-contract-appendix-a]: files/dfm-contract/DFM_Contract_Appendix_A_Perf_Reqs.pdf
[dfm-contract-appendix-b]: files/dfm-contract/DFM_Contract_Appendix_B_Scope.pdf
[dfm-contract-appendix-c]: files/dfm-contract/DFM_Contract_Appendix_C_Maintenance.pdf
[dfm-contract-appendix-d]: files/dfm-contract/DFM_Contract_Appendix_D_Fee_Schedule.pdf
[dfm-contract-appendix-e]: files/dfm-contract/DFM_Contract_Appendix_E_Hardware_Specs.pdf
[dfm-contract-main]: files/dfm-contract/DFM_Contract_060111.pdf
[directors-report-march-2017-local]: files/SF_Elections_March_2017_Director_Report.pdf
[directors-report-march-2017-original]: http://sfgov.org/electionscommission/sites/default/files/Documents/meetings/2017/2017-03-15-commission/March%202017%20Director%20Report.pdf
[disability-rights-ca-letters]: files/Disability_Rights_Letters_Nisen.pdf
[dominion-costs-2008]: files/Dominion_System_Costs_2008_Jerdonek.pdf
[eac-vvsg]: https://www.eac.gov/voting-equipment/voluntary-voting-system-guidelines/
[eac]: https://www.eac.gov/
[elections-commission]: http://sfgov.org/electionscommission
[eml-specs]: http://docs.oasis-open.org/election/eml/v7.0/eml-v7.0.html
[eml-wikipedia]: https://en.wikipedia.org/wiki/Election_Markup_Language
[free-and-fair]: http://freeandfair.us/blog/open-free-election-technology/
[github]: https://github.com/
[ict-plan-2008]: files/SF_ICT_Plan_2018-22.pdf
[ieee-1622]: http://grouper.ieee.org/groups/1622/
[la-vsap-rfi]: files/la-vsap/LA_RFI_20170524.pdf
[la-vsap-rfp-phase-1]: files/la-vsap/LA_RFP_20170918.pdf
[la-vsap]: http://vsap.lavote.net/
[lafco-report]: files/LAFCo_Report_Open_Source_Voting.pdf
[lafco]: http://sfgov.org/lafco/
[mayor-budget-press-release]: http://sfmayor.org/article/mayor-lee-signs-citys-balanced-budget-fiscal-years-2016-17-2017-18
[nist-itl]: https://www.nist.gov/itl/voting
[nist-voting]: http://collaborate.nist.gov/voting/bin/view/Voting/WebHome
[nist-vvsg-principles]: http://collaborate.nist.gov/voting/bin/view/Voting/VVSGPrinciplesAndGuidelines
[open-count-pres]: https://www.usenix.org/conference/evtwote12/workshop-program/presentation/wang_kai
[open-count]: https://github.com/FreeAndFair/OpenCount
[open-rla-repo]: https://github.com/FreeAndFair/OpenRLA
[open-voting-consortium]: http://www.openvotingconsortium.org
[oset-arch-html]: https://trustthevote.org/our-work/framework/
[oset-arch-pdf]: http://www.dubberly.com/wp-content/uploads/2014/09/TTV_Framework_Book.pdf
[oset-foundation]: http://www.osetfoundation.org/
[oset-modules]: https://trustthevote.org/our-work/overview-2/
[osi-approved-licenses]: https://opensource.org/licenses
[osi]: https://opensource.org/
[osvtac-about-recs]: https://osvtac.github.io/about#project-recommendations
[osvtac]: https://osvtac.github.io
[prime-iii-faf-repo]: https://github.com/FreeAndFair/STAR-Vote
[prime-iii-repo]: https://github.com/HXRL/Prime-III
[prime-iii]: http://www.primevotingsystem.com/
[proposed-budget-2016]: files/SF_Mayor_Proposed_Budget_2016-18.pdf
[rfp-business-case-page]: http://mission.sfgov.org/OCABidPublication/BidDetail.aspx?K=12141
[rfp-business-case-pdf]: files/SF_Business_Case_RFP_FINAL.pdf
[sf-digital-services]: https://digitalservices.sfgov.org/
[slalom-contract-appendix-a]: files/slalom/contract/Business_Case_Appendix_A.pdf
[slalom-contract-appendix-b]: files/slalom/contract/Business_Case_Appendix_B.pdf
[slalom-contract]: files/slalom/contract/Business_Case_Contract.pdf
[slalom-rfp-response]: files/slalom/REG_RFP_2017-01_Slalom_Response.pdf
[star-vote-entity]: files/star-vote/STAR-Vote_Statement_of_Intent.pdf
[star-vote-final-press-release]: http://www.traviscountyclerk.org/eclerk/Content.do?code=star-vote-a-change-of-plans
[star-vote-final-report]: files/star-vote/STAR_Vote_Final_Report.pdf
[star-vote-rfp]: files/star-vote/RFP_STAR-Vote_Unofficial_Copy.pdf
[star-vote-usenix]: https://www.usenix.org/conference/evtwote13/workshop-program/presentation/bell
[techfar-handbook]: https://playbook.cio.gov/techfar/
[trust-the-vote]: https://trustthevote.org
[verified-voting-foundation]: https://www.verifiedvoting.org/
[vip-project]: https://votinginfoproject.org/
[vip-repo]: https://github.com/votinginfoproject
[vstf-report]: files/VSTF_Report.pdf
[vstf]: http://sfgov.org/ccsfgsa/voting-systems-task-force
