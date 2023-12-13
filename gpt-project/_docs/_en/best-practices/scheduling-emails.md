---
title: Schedule emails
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to schedule emails.
promote-service: what-if-scenario
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-examples.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

<!-- not sure about multiactivty and essential -->

If you want to use injixo to schedule emails in addition to telephony and wonder how it works? In this article, we explain how this works.

## Create a separate activity

1. Create {% link_new a new activity | features/administration/activities.md %} of type _Presence_.
2. Check the _Plannable_, _Paid_ and _Comply with Rest Period_ checkboxes.
3. Assign this activity to the Planning Unit in which you want to schedule emails.

If not all employees can or should process emails, you need a skill for the email activity. Read more about {% link_new skills | features/administration/work-with-skills.md %}.

To forecast email traffic, incoming emails ideally should be imported into injixo on an interval basis from your ACD or email tool so that they are available in a {% link_new workload | features/forecast/injixo-forecast/manage-workloads.md %} or {% link_new queue | features/forecast/forecastpro/administration/queues.md %} for a separate forecast.
As with a 'phone call' forecast, use the forecast values for the email volume to generate a separate employee requirement for the email Activity.
Configure a Constant requirement script for emails, e.g. 2 people per interval in the morning and 3 per interval in the afternoon.

The scheduling then takes place using day models with present Activities, so that the job optimization or the AutoScheduler can replace 'Present' in each case either with blocks of phone calls or emails. Of course, you can define fixed email blocks in the day model to schedule emails without employee requirements or only in certain periods.

## Multiactivity

To schedule people who are skilled for both emails and phone, you can create a multiactivity and add phone and email as subactivities.

1. Create {% link_new a new activity | features/administration/activities.md %} of type _Presence_ and give it a name, e.g. Multi-Phone-Mail.
2. Check the _Plannable_, _Paid_ and _Comply with rest period_ checkboxes.
3. Create an email activity named 'Email' and if not already available, an additional activity called on-phones.
4. Assign these activities to the planning unit in which you want to schedule emails.
5. Add Email and on-phones to the Multi-Phone-Mail activity to create a multiactivity.

This scheduling approach only works with the AutoScheduler. When calculating the requirement it is important to make sure that different Erlang C Service Level parameters apply to the email activity than to the telephony (e.g 80% in 20 seconds).
