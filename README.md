# BrewerLean
BrewerLean is a commercial brewery production operations and tracking tool.  As brewery owners, we are confronted with the reality that there is a lot of software ABOUT brewing but there's not a lot of software FOR brewing.  Existing commercial packages tend to focus primarily on regulatory compliance or business-focused issues and have an overly strict view of the brewing "process" as it is generically defined.  This makes the software and features very valuable for management-level team members, but potentially bloated and confusing for the team members who are on the production floor.  Those team members don't care about the intricacies of "expressing" production orders or if a particular package's workflow doesn't entirely mesh with theirs reality.  Those team members are also the keepers of the kingdon when it comes to accurate understanding of the state of a beer production facility at any point in time, so their point of view is critical.

#### Data Compliance
Data compliance is the key to all process improvement in manufacturing settings.  You have to get data in a timely, accurate fashion.  We've heard frequently that if you just train your employees to use whatever software system that's good enough.  We don't think that's the case.  It isn't about training them to use a thing, it's about getting them to care since getting employees to care drives buy-in and compliance.  A brewery operations system can't just be valuable up the management chain.  It has to be a core resource for *every* member of the team.  Systems that purport to be the "one-stop-shop" or the "single source of truth" just aren't real, and by their very nature waste time, energy, and effort.  There is no single workflow that works for every person in every brewery, and in any case teams need the flexibility to continually improve their processes with having to shoehorn their work into a system.   We believe the way forward is to create a bottom-up system that focuses on data collection and compliance, and to use that to drive development for other concerns.  No business runs on a single system.  Decoupling of concerns is critical and allows better choices to be made.  It is perfectly okay for management team members to have different systems and different concerns, but that these concerns should ultimately come together in a cohesive (but not singular) way.

#### Why Lean?
We call the system BrewerLean because we are advocates for, and experts in, Lean process methods in a brewery manufacturing setting.  The Lean method is about reduction of waste, and we feel that existing brewery software packages are repositories of waste simply because they are by their nature process-additive.  They try to be everything for everyone.  Waiting time, over processing, and unutilized talent are all core wastes that current brewery management systems don't reduce, and may in fact increase.  Information must be supplied and provided at the moment when it is available or when it is needed.  No extra clicks, no extra process understanding.  This isn't software *about* your brewery.  This is software *for* your brewery.

BrewerLean is not a one-stop-shop.  BrewerLean is not for workflow enforcement since you must be free to adapt and improve processes and workflows as you see fit.  BrewerLean is intended to let you pick and choose what you need, and to be a complement to whatever other ystems you may want to use.  BrewerLean is not complete.  It's a work-in-progress that we hope will be found valuable by other members of the brewing community.  We hope that others will support us and support the project with further development.

## Roadmap
The current BrewerLean system focuses on data gathering as a foundational element.  No process improvement can take place until data gathering procedures are widely adopted.  So, at the moment we have three functional modules:
* EBS = 'Electronic Brew Sheets', which is a simple easy-to-use tool for tracking common brew sheet information, but with care to avoid any specific workflow preferences.  We've done our best to abstrct this to encompass things that most breweries will have in common.
* CRM = 'Customer Relationship Management', which was build specifically for the self-distribution business to help track sales calls and the outcomes of those sales calls.  It does not process orders or create invoices, but rather is pared down to the minmum amount of data required to analyze calls to conversion, reduce calls that don't convert, and feedback basic information to production.
* Delivery = Tracks van load out and deliveries from the perspective of the driver.  Various aspects of start/finish mileage, start/finish times, load out quantities are all entered.  Again, without preference to individual brewery workflows, this data allows for reporting on miles driven, miles per unit delivered, miles per stop, etc., as a way of understanding delivery efficiency, transport, and routing waste.

### There are three modules currently being created
* Yeast = tracking of yeast usage, generations, counts
* Formulations = uploading of formulations.  The only reason to do this is to track formulation needs separately from the vagaries of inventory control in more strict systems (where you may not inventory whirlfloc tablets, for example), and to short-circuit the EBS process of entering raw material usage.  Significant work here will need to be done to generalize this sufficiently without committing to an inventory-everything process.
* Reporting = creating a reporting framework that's easy to modify to create new reports.

### Our holy grail
The holy grail of our development is predictive scheduling.  We find the greatest deficiencies in existing brewery operations packages to be scheduling.  Dealing with schedule disruptions is part and parcel of brewery management.  However, current systems require manual adjustments and don't understand interconnections outside of their chosen workflows.  This means even minor adjustments (like, re-ordering brew days in a week or a fermentation that's a day delayed) can produce myriad side effects that must be manually reconciled.  We understand that scheduling is a difficult problem, with many factors involved (including unavoidable human factors).  But, we also feel that breweries *have* all the information that is needed to make smarter, more helpful scheduling software.  That's why we've built things in the order that we have.  Data collection is key, and will ultimately inform the development of our schedule management system.  

## Documentation TOC
Documentation is an on-going project, so please file issue for
anything you think is missing.

* [Installation](INSTALLATION.md)
* [Setup](SETUP.md)

## History
BrewerLean came out of an in-house project at The Alementary Brewing Co. to replace our clipboards and paper with an "electronic brew sheet" so we could all have ready access to the data without having to be at the brewery or without having to get a laptop to open a thick-client, use non-mobile-friendly web application, or use a mobile application that was not fit-for-purpose.

Aside from that, we were generally displeased with the state of scheduling as it exists in current well-known systems, and we have a bottom-up scheduling concept that requires seamless real-time data and high employee compliance before we can build it.  We're working on that currently, and it will be open sourced as part of the BrewerLean project as soon as we get a release candidate.

## Comparison to other systems
The BrewerLean system is not created to disparage the work of Orchestrated, Ekos, Beer30, or any other brewery management system.  The Alementary itself operates formally using Orchestrated.  We simply needed a production floor system that was faster and more reliable with a less constrained view of brewery operations.  We 100% welcome integration work with existing, more expansive systems.

## Support
BrewerLean is free software following the GPLv3 license.  We want people to use it freely without fear of increasing costs.  Your data is always yours, and you have no fear of losing history or having a complicated migration should you decide BrewerLean is not for you.  If you are so inclined you can always use the system for free.
#### The Patreon
We struggled mightily with the right way to do this, since we are an active production brewery first and foremost and don't have the resources to hire full-time support staff.  So, we created a [patreon here](https://www.patreon.com/alementary).  If you would like formal support, we ask that you sign up for one of our Patreon tiers.  We've purposefully made this inexpensive.  Even if you'd just like to support the project so you can monitor where it goes over the next year, we encourage you to throw in some bucks.  As an open source project, we will need a way to prioritize development going forward, and a lot of those priorities will come from our Patreon.  

## Contributions
BrewerLean is licensed GPLv3, so contributions are definitely welcome.  We only ask that before submitting a contribution please create a GitHub issue in the BrewerLean repository so we can know what you're up to and discuss it so that the vision is maintained.

## Who is doing this?
The Alementary is a production brewery in Hackensack, NJ.  We run several different businesses, from producing our own brands to contract brewing to consulting.  The principals include Blake Crawford, who was the principal systems architect at Viacom before leaving in 2016 to open the brewery.  Blake is the creator and lead developer for the BrewerLean system.



