---
title: Set up shift bidding
product_label:
  - advanced
  - enterprise
description: Generate shifts for the shift bidding process, invite people to bid on them, run a lottery, and publish the schedule (Schedules).
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/edit-or-delete-staff-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/view-approve-shift-swap-requests.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/notifications.md
---

Shift bidding allows people to take part in the scheduling process by bidding on shifts. To get started, set up a scheduling period and generate shifts.

## Shift bidding process

Before you start the shift bidding process, you need to {% link_new calculate staff requirements | features/forecast/injixo-forecast/calculate-staff-requirements.md %} and optionally {% link_new insert shift sequences | features/scheduling/schedules/schedules-insert-shift-sequences.md %}.

1. In Schedules, create a {% link_new Scheduling period | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md | #create-scheduling-periods %} with the status Unpublished.
2. Enter [minimum and maximum values](#specify-your-shift-mix) for each day model in the shift requirement table.
3. [Generate the shifts](#generate-shifts).
4. Invite people to [bid on shifts in injixo Me](#invite-people-to-bid-on-shifts).
5. If the bidding period is over, run the [lottery](#run-the-shift-lottery) and [assign the remaining shifts](#assign-remaining-shifts) that have not been requested before.
6. [Optimize activities and breaks and publish the schedule](#optimize-and-publish-the-schedule).

## Specify your shift mix

Before you create the shifts that will be available for bidding, determine what types of shifts you want in the mix. You must adjust the values for each new scheduling period before you start the shift generation. Otherwise, injixo will not create the correct shifts to cover the staff requirements.

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click _Scheduling periods_{:.doc-button}.
3. To adjust the shift requirement, hover over the **Scheduling period**, then click the {% icon ellipsis_v %} on the right.
4. Select _Adjust shift generation_{:.doc-button} from the overflow menu.
5. In the shift requirement table, {% link_new enter **Min** and **Max** values | features/scheduling/schedules/schedules-shift-requirement.md | #enter-required-shifts-into-the-table %} for your day models.

## Generate shifts

The shift generation process creates shifts for each day of the scheduling period. injixo considers both existing shifts in the schedule and staff requirements to generate the best possible coverage.

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click _Scheduling periods_{:.doc-button}.
3. Hover over the **Scheduling period** for which you want to generate shifts and click {% icon ellipsis_v %} on the right.
4. Select _Generate shifts_{:.doc-button} from the overflow menu.
   {{ 2 | image: 'Scheduling Periods with Shift Functions', '80%' }}
5. (Optional) Change the **Shift generation requirement** value.

   - Option **of the employee requirement**: With a value of 100%, injixo will cover staff requirements exactly by 100%. A value greater than 100% will lead to more shifts than specified by the requirement. A value smaller than 100% will lead to fewer shifts (useful if the number of available staff is too low to cover the requirement).
   - Option **of the contractual hours**: With a value of 100%, injixo will make sure all people can reach their contractual hours with the generated shifts.

6. To start the shift generation, click _Generate shifts_{:.doc-button}.
   When the shift generation has finished, you can access a results report in the JobProcessor that contains information about input data and the result.

   {{ 3 | image: 'Parameter window for shift generation', '50%' }}

Note: In Shift Center, you can overwrite the shift generation result by {% link_new changing the number of shifts generated for a single day | features/scheduling/edit-or-delete-staff-requirements.md %}, e.g. to modify a single day for testing.

The Shift Center displays key figures related to the shift generation. You find them in the {% link_new parameter window | features/scheduling/shiftcenter/shift-center-overview.md | #parameter-window %} at the bottom of the page:

- Requirement (under the Day Models tab): number of generated shifts for each individual day model
- Staffing According to Shift Requirement (under the Activities tab): number of generated shifts with the selected activity
  <!-- You can also rate the quality of a shift generation, as you can see here how the employee requirement would be covered if all generated shifts were staffed. -->
- Coverage According to Shift Requirement (under the Activities tab): difference between required and generated shifts

## Invite people to bid on shifts

After you have generated shifts, do the following:

1. Change the **status** of the {% link_new scheduling period | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md | #status %} to Shift bidding enabled.  
   People will receive a [notification](#email-and-browser-push-notifications).
2. (Optional) Add a **deadline** to set a date by which people can submit shift bids.  
   People place a first and a second bid on each day. Everyone can bid on the same shift.  
   To estimate the probability of getting a shift and, if necessary, find alternative shifts, people can see how many shifts are needed, and how often a certain shift has already been requested.

   > Bids in injxo Me are limited to a maximum of 100 days in advance (for scheduling periods > 100 days).

3. When the bidding period is over (or the deadline has passed), set the scheduling period back to **status** Unpublished.

To see peoples' bids, go to Schedules or Shift Center and add level Request (first bids) or Alternative Request (second bids) to your view. Learn more on how to add the level in {% link_new Shift Center | features/scheduling/shiftcenter/shift-center-overview.md | #choose-the-time-range-and-levels %} and {% link_new Schedules | features/scheduling/schedules/schedules-overview.md | #level-column %}.

## Run the shift lottery

When the bidding period is over, schedule the people's shift bids using the lottery. This copies the requested shifts from the levels Request and Alternative Request into level Schedule.

> Before you re-run the shift generation, {% link_new backup all shift requests | features/scheduling/schedules/schedules-copy-level-content.md %} in an unused level, e.g. Version 1.
>
> A new shift generation deletes all previously submitted requests from the Request and Alternative Request levels.

Tip: If certain team members should have a higher chance of getting the requested shifts, run the lottery based on selections. Rotate the order of selections in each scheduling period to ensure a fair distribution in the long run.

To run a lottery, follow the below steps:

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click _Scheduling periods_{:.doc-button}.
3. Hover over the **Scheduling period** for which you want to start the lottery and click {% icon ellipsis_v %} on the right.
4. Select _Start shift lottery_{:.doc-button} from the overflow menu.
5. (Optional) Activate the option **Consider average start time of other shifts** and enter a **Tolerance** value (hh:mm format).
   - If activated, injixo considers the (average) shift start time. Learn more about [how the tolerance setting works](#choose-the-right-tolerance-setting).
   - If not activated, people can get shifts with random start times.
     {{ 4 | image: 'Parameter window lottery', '45%' }}
6. To select all people, check the **checkbox** on top. You can filter the list based on selections or employee filters and select individual people.
7. Click _Start shift lottery_{:.doc-button}.  
   When the lottery has been finished, you can access the Lottery Log in the JobProcessor. The report includes the reasons why a bid has not been scheduled, as well as daily and total lottery quotas in %.

## Assign remaining shifts

After the lottery has scheduled shifts, there are often some shifts that have not been assigned because they have not been requested by anyone. In this step, shifts will be assigned to people who received no or not enough shifts.

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click _Scheduling periods_{:.doc-button}.
3. Hover over the **Scheduling period** for which you want to assign shifts and click {% icon ellipsis_v %} on the right.
4. Select _Assign shifts_{:.doc-button} from the overflow menu.
5. (Optional) Activate the option **Consider average start time of other shifts** and enter a **Tolerance** value (hh:mm format).
   - If activated, injixo considers the (average) shift start time. Learn more about [how the tolerance setting works](#choose-the-right-tolerance-setting).
   - If not activated, people can get shifts with random start times.
     {{ 5 | image: 'Parameter assign shifts', '45%' }}
6. To select all people, check the **checkbox** on top. Optionally, you can filter the list by Selections or Employee filters and select individual persons.
7. Click _Assign shifts_{:.doc-button}.  
   When the shift has been assigned, you can access a report under _WFM > Administration > System > JobProcessor_{:.breadcrumbs} that lists all assigned and unassigned shifts.

Note that the schedule may still be incomplete when the process has finished, e.g. if there are not enough people, people without the necessary skills for shifts, or assigning a shift would cause a scheduling rule violation. You can change your configuration and re-run the process or manually change your schedule.

Tip: Instead of assigning shifts, you can also use {% link_new Create optimized schedule | features/scheduling/schedules/schedules-optimized-schedules.md %} to assign more shifts that complete the schedule.

### Choose the right tolerance setting

The shift start time calculation based on the Tolerance value works differently with or without already scheduled shifts (e.g. from shift sequences):

- With shifts: injixo calculates an average shift start time and then assigns shifts within the tolerance window. As an example, if existing shifts start at 8:00 and 12:00, the average is 10:00. When you set a tolerance value to 1 hour, the other shifts can start between 9:00 and 11:00.
- Without shifts: The first assigned shift determines the shift start time. For example, if the first shift starts at 9:00, and you set the tolerance value to 1 hour, the other shifts will start between 8:00 and 10:00.

## Optimize and publish the schedule

To optimize scheduled activities and break positions, run the {% link_new Job optimization | features/scheduling/schedules/schedules-job-optimization.md %} for the scheduling period.

To {% link_new publish the schedule | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %} and to allow agents to swap shifts, set the {% link_new scheduling period | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md | #status %} **status** to Published. If you have configured {% link_new shift swaps | features/scheduling/view-approve-shift-swap-requests.md %}, people can view their own shifts and {% link_new swap them with others | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}.

## Email and browser push notifications

If you change the status of a scheduling period, injixo will sent email and browser push notifications to inform people in the respective planning unit about date changes and to remind them to start bidding on shifts.

Users need to activate {% link_new browser push notifications | getting-started/notifications.md %} in their browsers. By default, your tenant will send both email and browser push notifications.
