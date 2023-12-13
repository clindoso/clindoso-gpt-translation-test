---
title: Work with skills
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how skills in injixo reflect employee skills. Create, edit, and delete skills and skill levels.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/configure-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
redirect_from:
  - /skills/
redirect_reason: Updated filename on 24 July 2023
---

Skills ensure that people are only scheduled for activities for which they are qualified. Skills map people's abilities (e.g. product knowledge, languages, communication channels, etc.) to activities they can work on and that you schedule with injixo.

To configure skills, go to _Plan > Configuration > Skills_{:.breadcrumbs}.

## Create skills

Create at least one skill for each activity that requires a particular ability. When you create a skill, injixo sets the default skill level to 100%. Skill levels reflect how proficient people need to be to work on an activity, e.g. 100% proficient in English but only 50% proficient in Spanish. You can create different skill levels for one skill. 

> If people do not need specific abilities to work on an activity, you do not need to create a skill for it.

1. Click _New skill_{:.doc-button}.
2. Enter a **Name**.
   The abbreviation is auto-generated, but you can edit it.
3. (Optional) Change the default configuration of a skill level.
4. (Optional) Click _Add skill level_{:.doc-button} to add additional skill levels, if you have people who are less proficient at the activity. See also: [Calculate suitability using rating and weighting](#calculate-suitability-using-rating-and-weighting).
5. Click _Create skill_{:.doc-button}.  

 Next, you can [assign a skill level to a person](#assign-skill-levels-to-a-person) and [assign the skill to an activity](#assign-skills-to-activities).

## Duplicate skills

To create a new skill with the same skill levels as an existing skill, follow these steps:

1. In the **Skills** list, click the skill you want to duplicate.
2. Click **Duplicate skill** under the skill name.  
   A **Create new skill** window opens with pre-filled skill levels.
3. Enter a **Name** for the new skill.
4. (Optional) Edit the skill levels.
5. Click _Create skill_{:.doc-button}.

## Edit skills and skill levels

1. Select a skill from the list.
2. Edit the skill or skill level(s).
   To delete a skill level, click the {% icon trash %} next to it.
3. Click _Save changes_{:.doc-button}.

## Delete skills

1. Select a skill from the list.
2. Click _Delete skill_{:.doc-button} and confirm.

## Assign skills to activities

1. Go to _Plan > Configuration > Activities_{:.breadcrumbs}.
2. Select an activity from the list and scroll to the **Skills** section.
3. Select a skill from the drop-down menu.
4. (Optional) Change the **Weighting**. If you only add one skill, keep the default value of 100%.  
   For activities that require more than one skill, you can [use weighting](#calculate-suitability-using-rating-and-weighting) to determine which skill is more important.
7. Click _Save changes_{:.doc-button}.

## Assign skill level(s) to a person

1. Go to _Plan > Configuration > Employees_{:.breadcrumbs}.
2. Select a person from the list and navigate to the **Skill Levels** section.
3. Click the {% icon item-add %} and select one or more skill levels from the list. 
   To select multiple entries, press and hold **Shift** or **Ctrl** while clicking.
4. (Optional) Add a {% link_new validity period | features/administration/set-a-validity-period.md %} for the skill level by selecting **Valid from** and **Valid to** dates.
   You cannot assign different skill levels of the same skill to a person for the same validity period.
 5. Click _OK_{:.doc-button}.  
   The activities that require the skill(s) assigned will appear in the **Activities** section for that person.

An activity can require one or more skills. To work on an activity that requires several skills, the people assigned to it need to have all the skills.

Tip: To assign a skill to several people at once, you can use the {% link_new mass update functionality | features/administration/employee-overview.md | #use-mass-update %}. 

## Calculate suitability using rating and weighting

injixo can calculate a suitability value based on:

- The rating of a person's skill level
- The weighting values when an activity requires several skills

Example: You have a Calls in Spanish activity that requires two skills, Spanish and Calls. The Spanish skill is twice as important as the Calls skill. The weighting values are 100 for Spanish and 50 for Calls.

- Person 1 has the skill levels Spanish 50% and Calls 100%.
- Person 2 has the skill levels Spanish 100% and Calls 50%.

This results in a suitability value of 66.66% for person 1 and 83.33% for person 2.

The suitability value is calculated using this formula: `(Sum(Each skill's weighting * individual's skill level value for that skill) / (Sum of all skills' weighting)`

If an activity requires only one skill, the suitability value equals the person's skill level.

To consider the suitability value in {% link_new optimized scheduling | features/scheduling/schedules/schedules-optimized-schedules.md %} (instead of using the headcount), configure setting _48069_{:.id-label} _Take suitability percentage into account_. In {% link_new Shift Center | features/scheduling/shiftcenter/analyze-coverage-staffing-requirement.md %} and {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %}, coverage and staffing cannot be displayed based on people's suitability. In these cases, coverage and staffing are always displayed as 100% to show the headcount.
