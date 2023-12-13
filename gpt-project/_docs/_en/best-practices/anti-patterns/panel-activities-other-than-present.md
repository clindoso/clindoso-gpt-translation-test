... are used like this:

<img src="/assets/img/en/best-practices/schedule-anti-patterns/image-1.png" width="50%" alt="wrong day model">

#### Did you know...?

This means that this day model can only be used for that specific activity, and you cannot replace the base activity, you need to recreate the day model.

#### What you should do is...?

Always use ‘Present’ as the first activity when creating a day model. The ‘Present’ activity works as a placeholder; if it is marked as replaceable, it will be replaced during a job optimization or full optimization by a plannable activity with a forecasted requirement.

**Tip:** Add other presence and absence activities to the base activity using the {% icon plus %}. Each additional presence and absence activity is placed on top of the base activity. This allows you to place fixed activity blocks in flexible day models. The duration of all other activities must not exceed the duration of the base activity. As example, you can set a fixed telephony or back office activity in a particular time within the day model to cover a constant requirement.

**Example:**  
Create a Day Model with the base activity 'Present' and add 'Web Chat' as a sub Activity between 9am and 2pm. If you set the duration of 2 hours and an interval of 15 minutes, Web Chat will be scheduled (if needed) for a 2 hour block during that time.

<img src="/assets/img/en/best-practices/schedule-anti-patterns/image-2.png" width="50%" alt="correct day model">
