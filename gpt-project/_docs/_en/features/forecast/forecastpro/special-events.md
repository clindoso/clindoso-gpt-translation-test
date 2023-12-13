---
title: Consider special events
product_label:
  - on-premise
---

Special events, such as public holidays, often result in deviating daily or weekly curves. In the following we will show you possible solutions, how you can consider different deviations in your forecast:

## Effect of the Event

As an introduction to dealing with events, it should be considered in advance what influence the event has on the daily curve compared to a normal day.

- `Steady daily curve` (with different volume):
  The daily curve is constant over the course of a normal day, only the volume differs in percentage. Example: With a hotline, a 25% lower call volume occurs on a public holiday with the same distribution over the day.
- `Divergent daily curve`:
  The daily curve differs significantly from a normal day. Example: With a hotline, on a public holiday there is a considerably lower call volume in the morning, but this increases drastically in the course of the afternoon compared to a normal day.

## Constant Day Curve

If the daily curve remains the same and the volume is different, it is advisable to process the event after the forecast - but before calculating the requirement. This procedure saves you the effort of creating event types and user-defined daily and weekly curves.

In the first step, you carry out the forecast as usual for the period in which your event type lies. Then you use the possibility to edit daily curves (_Forecasting > ForecastPro > Edit Daily Distribution Curves_{:.breadcrumbs}):

- Select your queue from the parameters.
- Select your value type from the parameters.
  Note: The calculation has to be done per value type of the forecast, by default 'incoming calls' and 'average call duration'.
- Select `Forecast` as version, so that you do not overwrite the historical data.
- Select the day on which the event falls as the start and end date.
- Call the forecast values by clicking on _Apply_{:.doc-button}.
- In the table that appears, select the day in question.
- Now select the option `Day` under the `Calculation` and enter your desired serve or discount and execute it by clicking on _Apply_{:.doc-button}.
- Save the change in the forecast under the parameters. Click _Save_{:.doc-button}.

The different volume is saved for the day and the forecast can be completed as usual by calculating the requirement.

## Deviating Day Curve

### Recurring event with the same day of the week

For example, the event is a public holiday that always falls on the same weekday, such as Whit Monday always falls on a Monday. In our example, we assume a forecast and planning period of four weeks.

#### 1. Create and assign event type

- Under _Administration > Forecasting > Event Types_{:.breadcrumbs} you will find the weekdays Monday to Sunday which are predefined by the system.
- Create a new event type via the action bar. Assign a `name` and a `short name`. "Factors" are not necessary in this scenario and can therefore be ignored.
- In the next step, under _Administration > Forecasting > Queues_{:.breadcrumbs}, you assign the event type to the desired queue(s). To do this, select a queue and add the type in the processing mask under Event Types and store the corresponding opening time.
- To link the event to a date, go to _Administration > Forecasting > Forecast Calendar_{:.breadcrumbs}. Select a queue to which the event has been assigned. Click _Apply_{:.doc-button} to confirm your selection. Select the event type from the options on the right. Then, click a day cell in the calendar. This adds the event type to the date.

> Tip
>
> To be able to include the event in the forecast on the basis of historical data, it makes sense at this point to store the event retrospectively in the forecast calendar. In our example, it is advisable to enter Whit Monday for the current year as well as for the past 2-3 years (depending on how far your historical data goes back).

- With the creation and assignment of the event types to queues and the forecast calendar, the necessary preparatory work is completed and we can switch to the forecast process.

#### 2. Create typical daily curve

- Call _Forecasting > ForecastPro > Typical Day Distribution Curve_{:.breadcrumbs}. The procedure for the day curve is as usual - call the queue and value types with the event type over the corresponding date. In our example this would be for the year 2016 a start and end date on 16.05.2016 as well as "Whit Monday" as event type.
- By calling and saving further historical data on the event type (in the example Whit Monday 2015, 2014, etc.), the typical daily curve for the event type becomes even more accurate.

> Note
>
> Identical to the general procedure for day curves, care should be taken whether a `day curve saved` in black color already exists. If this is not the case, it should be deactivated - remove the check mark `active` under the `day curve stored`. Rule of thumb: At the first call and save no day curve is stored yet.

#### 3. Create user-defined week curve

- The next step is to create a typical weekly curve containing the event types. So that our `standard week curve` is not influenced, we create a user-defined week curve.
- Under _Forecasting > ForecastPro > Typical Week Curve_{:.breadcrumbs} you select the desired queue and value types and specify the length as well as the start and end date. In our example for Whit Monday 2016 a `length of the week curve` with 1 as well as the `start and end date` from 16.05.2016 to 22.05.2016. The event type does not have to be selected here, because the system already knows the date through the `Forecast Calendar`.
- Call via _Apply_{:.doc-button} button opens the weekly curve accordingly, causing the _New_{:.doc-button} button to appear at the level of the _Weekly curve selection_{:.doc-button}. Now use the button to create a user-defined weekly curve. Then save the week curve as usual.
- By calling up and saving further historical weeks in which the event type is located (Whit Monday week 2015, 2014, etc.), the typical weekly curve for the event type becomes even more accurate.

#### 4. Forecast

- The forecast procedure is the same as usual, except that the event type must be taken into account when selecting the forecast period.
- This can be seen in our example. Here our forecast period is four weeks. 2017 Whit Monday falls on the
  05.06.2017, so in our forecast period from 29.05. until
  25.06.2017. Thus we have the following situation in forecast weeks:
  1st week = normal week
  2nd week = alternative week with event type Whit Monday
  3rd week = normal week
  4th week = normal week
- For this reason we recommend in the first step as usual to make the forecast for the 4 weeks with the standard weekly curve. Then the forecast is only made for the deviating week with the user-defined weekly curve and thus overwrites this one-week period (in the example the 2nd week).

### Recurring event on a different day of the week

The event is, for example, a public holiday which, due to its fixed date, falls on different weekdays each year, such as the 'day of work' on the first of May. In our example, we assume a forecast and planning period of four weeks. The following steps are described in detail below:

The first two steps [1. Create and assign event type] and [ 2. Create typical day curve] are identical to the procedure described above.

#### 3. Create user-defined weekly curve

- The next step is to create a typical weekly curve containing the event type. So that our "standard week curve" is not influenced, we create a user-defined week curve.
- Under _Forecasting > ForecastPro > Typical Week Curve_{:.breadcrumbs} select the desired `Queue` and `Value Types` and enter the length as well as the `Start and End Date`. In our example for the day of work 2016 this is a "length of the week curve" with 1 as well as the start and end date from 25.04.2016 to 01.05.2016. The `Event Type` does not have to be selected here, because the system already knows the date from the forecast calendar.
- Call the weekly curve via _Apply_{:.doc-button} accordingly, whereby the button _New_{:.doc-button} appears at the level of the _Weekly curve selection_{:.doc-button}. Now use the button to create a user-defined weekly curve. Make sure to deactivate the `Saved Week Curve` in black color (uncheck `Active` under the `Saved Day Curve`). This is necessary, otherwise the event will be falsified by the stored average!

- By calling up and saving further historical weeks in which the event type is located (day of the working week 2015, 2014, etc.), the typical weekly curve for the event type becomes even more accurate (also do not consider the average here).

#### 4. Forecast

- The forecast procedure is the same as usual, except that the event type must be taken into account when selecting the forecast period.
- This can be seen in our example. Here our forecast period is four weeks. In our forecast period from 01.05. to 28.05.2017. Thus we have the following situation in forecast weeks:
  1st week = different week with event type Workday
  2nd week = normal week
  3rd week = normal week
  4th week = normal week
- For this reason we recommend in the first step as usual to make the forecast for the 4 weeks with the standard weekly curve. Then the forecast is only made for the deviating week with the user-defined weekly curve and thus overwrites this one-week period (in the example the 1st week).

### Event series of several events within a forecast period

In an event series, several events occur within a forecast period, such as Easter with Good Friday, Easter Sunday and Easter Monday. The procedure is the same as for the cases described above.

Only with the `User-defined weekly curves` it has to be considered in which period the individual event types fall. This event series, in our case Good Friday, Easter Sunday and Easter Monday, should be stored in a single user-defined weekly curve. For our example, this should be stored in a two-week typical weekly curve.
