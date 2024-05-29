---
title: Notifications
product_label:
  - advanced
  - enterprise
description: Learn how injixo uses notifications and how to configure them.
redirect_from: /push-notifications/
redirect_reason: used in injixo UI and mailing
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-notify-scheduling-changes.md
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md
---

injixo can send email notifications and browser push notifications.

By default, injixo sends notifications to inform people about events in the scheduling process:

- Published schedules
- Schedule changes
- Shift swap requests

Email notifications are sent to each person's login email address. Browser push notifications appear as clickable pop-up notifications if you are logged in to injixo in at least one browser tab. If you click a notification, your browser will display injixo.

## Configure notifications

Users with admin access can turn off specific notifications:

1. Go to _Account > Notifications_{:.breadcrumbs}.
2. Click a tab to change the notification category.
   > Note
   >
   > If you deactivate email notifications for Me, people will not be able to invite colleagues to swap shifts in injixo Me.
3. Check or uncheck the **Email** or **Browser Push** checkboxes as required.

The notification settings are saved automatically. The selected settings affect all users.

## Allow browser push notifications

If notifications are not already set through group policies in the operating system, individual users can activate them for the current browser in their user profile:

1. Click your **username** at the top right to open your user profile.
2. In the **Notifications** section, click _Allow injixo notifications_{:.doc-button}.
3. A pop-up window will open in your browser where you can permanently allow browser push notifications.

## Fix browser push notifications issues

Browser push notifications are delivered by the browser and the operating system, and both must allow sending notifications. Do Not Disturb modes and focus settings (e.g. alarms and priority) can prevent notifications. Also, ensure that your browser is up-to-date. Clear browser cache and cookies if needed.

Learn how to fix notification issues in different browsers and operating systems:

- Chrome: [Google Chrome Support](https://support.google.com/chrome/answer/3220216?hl=en-GB)
- Firefox: [Mozilla Firefox Support](https://support.mozilla.org/en-US/kb/push-notifications-firefox)
- Safari: [Safari Support](https://support.apple.com/en-gb/guide/safari/sfri40734/15.1/mac/12.0)
- Windows: [Microsoft Windows Support](https://support.microsoft.com/en-us/windows/change-notification-settings-in-windows-8942c744-6198-fe56-4639-34320cf9444e#WindowsVersion=Windows_10)
- Android: [Android Support](https://support.google.com/android/answer/9079661?hl=en)
- Mac: [Apple macOS Support](https://support.apple.com/en-us/HT204079)
- iOS: [Apple iOS Support](https://support.apple.com/en-us/HT201925)

## Test browser push notifications

To test if browser push notifications work on your device and with your chosen browser,
go to <https://www.bennish.net/web-notifications.html/>.
