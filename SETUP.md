# Initial Setup

Before you can run anything, you'll need to log into the Django
admin console using your selected Django superuser and password.
Once in the admin console, you must setup some initial data so
the system has basic information.

* Batch Sizes: enter the sizes of projects that you brew
* Facilities: enter the locations you use for brewing
* Materials: enter the raw materials that you use according to the supplied categories.  BrewerLean keeps things simple coarse-grained categorizations of Grains, Hops, Yeast, and Other.
* Originators:  Enter the raw material "originators".  You can use this to categories where you buy things from, or for keeping track of the original producer--your choice.
* Partner Types:  If you perform contract brewing, use this to categorize the types of partners for whom you brew.  Otherwise, just create one record with "Internal" for your own brands.
* Partners:  Enter your list of contract brewing partners
* Product Types:  Enter the list of product types you produce.  This can be anything meaningful, but easy product has a type.
* Products: Enter your initial list of products (beers)
* Schedule Patterns: schedule patterns are fundamental in BL.  They specify the number of days offset (estimated) for specific events in the brewing process.  This is used for calculating your planned dates
* Staff:  Enter the names of staff members who are involved in BL.  We're getting away from this.
* Tanks: Enter your production vessels by type and facility

## For 3rd Party Auth
If you want to use GSuite or Google Workplace authentication, you need to
set up your "sites".  Minimally, you'll want one for your production
environment and one for your development or test environment.  You'll
also need to set up your social applications, which for Gsuite will
be the google API.  Setup of 3rd party authentication is beyond the scope
of this documentation, but readily available:
[django-allauth](https://django-allauth.readthedocs.io/en/latest/overview.html)
