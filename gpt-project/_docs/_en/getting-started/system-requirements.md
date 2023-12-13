---
title: System requirements
description: Browser and desktop requirements for integrations, agents, and planner workstations.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/browser-setup.md
---

injixo is a browser-based workforce management SaaS software, available in multiple [WFM plans](https://www.injixo.com/pricing): injixo Essential WFM, injixo Advanced WFM, and injixo Enterprise WFM.

## Browser requirements

injixo supports the two latest versions of the following browsers:

- Microsoft Edge
- Google Chrome
- Mozilla Firefox
- Apple Safari

## Pop-up blocker

injixo uses pop-ups to display additional dialog boxes. To allow pop-ups for injixo, proceed as follows:

- Turn off your pop-up blocker in [Microsoft Edge](https://support.microsoft.com/en-us/microsoft-edge/block-pop-ups-in-microsoft-edge-1d8ba4f8-f385-9a0b-e944-aa47339b6bb5).
- Set a pop-up blocker exception in [Google Chrome](https://support.google.com/chrome/answer/95472?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Callow-pop-ups-and-redirects-from-a-site), [Mozilla Firefox](https://support.mozilla.org/en-US/kb/pop-blocker-settings-exceptions-troubleshooting), and [Apple Safari](https://support.apple.com/guide/safari/block-pop-ups-sfri40696/mac).

## Microsoft Edge in Internet Explorer (IE) mode

ActiveX-based features in WFM require {% link_new Microsoft Edge in IE mode | support/faq/configure-edge-internet-explorer-mode.md %}. To configure the IE mode, you need a [site list XML file](https://learn.microsoft.com/en-us/deployedge/edge-ie-mode-local-site-list).

<style>
table {
  width: 100%;
}
table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

| WFM plan                               | Microsoft Edge in IE mode required         |
| -------------------------------------- | ------------------------------------------ |
| Essential WFM                          | No                                         |
| Advanced WFM                           | No                                         |
| Enterprise WFM                         | Only when using custom features            |
| Classic <sup>1</sup>                   | Yes                                        |
| Enterprise WFM on-premise <sup>1</sup> | Yes. If not configured, you cannot log in. |

<sup>1</sup> Legacy software (old WFM plans that are currently still in use)

If you use the wrong browser or a wrong IE mode configuration, the IE logo in the WFM navigation identifies the features that require IE mode (Classic/Enterprise WFM).

{% link_new injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} works with any listed browser, on computers, smartphones, and tablets.

## injixo client software

ActiveX-based features in the WFM require the {% link_new injixo client | getting-started/browser-setup.md %}.

You can find the operating system requirements in the download description under [downloads.injixo.com](https://downloads.injixo.com).

| WFM plan                  | injixo client required                    |
| ------------------------- | ----------------------------------------- |
| Essential WFM             | No                                        |
| Advanced WFM              | No                                        |
| Enterprise WFM            | Only when using custom features           |
| Classic                   | Yes                                       |
| Enterprise WFM on-premise | Yes. If not installed, you cannot log in. |

If the injixo client is not installed, the IE logo in the left navigation identifies the features that require IE mode (Classic/Enterprise WFM).

{% link_new injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} does not require the injixo client.

## Firewall exceptions

To access the injixo web pages, allow web traffic to and from \*.injixo.com via port 443.

If you use ActiveX-based features or custom SDK applications, add another firewall exception. These applications use port 45054 for outgoing traffic (port 80 for injixo hosts prior to 2019) and require direct Internet access over Transmission Control Protocol (TCP). Proxy servers configured in the browser are not supported.

To get the address for the firewall exception, click _WFM_{:.menu-item} and use the name of your injixo host that is visible in the browser address bar, e.g. wfm-123abc.injixo.com.

To learn more about firewall exceptions in Windows, see [Microsoft documentation](https://support.microsoft.com/en-us/windows/add-an-exclusion-to-windows-security-811816c0-4dfd-af4a-47e4-c301afe13b26#:~:text=Go%20to%20Start%20%3E%20Settings%20%3E%20Update,%2C%20file%20types%2C%20or%20process).

### Share URLs for WebSockets

injixo uses WebSockets to send real-time updates to users in Shift Center, Schedules, and Real-Time Adherence. 

The TCP-based secure WebSocket protocol allows faster transmissions than HTTP through port&nbsp;443. The browser upgrades a standard HTTP connection to a WebSocket connection. If successful, the browser’s dev tools will show the corresponding HTTP 101 (Switching Protocols) status code when you load the page.

Shift Center requires WebSockets to work at maximum speed. If WebSockets are not available, AJAX polling is used instead. The other pages do not provide a fallback mechanism and show error messages or reconnection attempts if the WebSocket connection cannot be established. 

To allow WebSockets connections, add the following URLs to the allowlist of your firewall:

- https://shiftcenter.injixo.com
- wss:// shiftcenter.injixo.com
- https://www.injixo.com
- wss://ws.injixo.com

### WebSockets and proxy servers

WebSockets rely on a persistent TCP connection. Unlike traditional HTTP requests, a WebSocket connection remains open once established. Make sure that your proxy server does not terminate such TCP connections. Popular proxy servers like Nginx or Apache have specific modules or directives to support WebSocket connections. 

## Network bandwidth requirements

injixo is designed and optimized for high performance and low resource consumption. During the first access, graphics are downloaded and stored locally in temporary files. Afterward, only basic information is transferred securely to the desktop.

A contact center with 200 seats can expect around 25-50 MB of hourly data transfer when all users are logged in.

## Integration requirements

Set up {% link_new integrations | features/acd-integration/cloud/how-integrations-work.md %} to allow injixo to import and process contact data and agent status data from external systems, such as automatic call distributors (ACD) or customer relationship management (CRM) systems.
injixo supports a wide range of cloud and on-premise integrations.

Install {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %} to regularly import data from on-premise and CSV integrations.

Data requests do not interfere with the main functions of communication software, such as telephony or email platforms.

Requests for real-time agent status information may use a direct socket feed. These feeds only transfer activity changes of agents (including a timestamp, an agent ID, and a status code) and are approximately 1kB each.

## Data center and security provisions

injixo operates from data centers in the Amazon EC2 infrastructure. [Amazon’s security policies](https://aws.amazon.com/security/) therefore apply to injixo, e.g. SOC 1 Type 2, ISO 27001 and PCI DSS Level 1.

All data is stored within the EU (European customers) and in the USA (US-based customers). injixo complies with all relevant data protection legislation, including GDPR in Europe. Read more about [injixo's cloud security and compliance](https://www.injixo.com/uk/security/).
