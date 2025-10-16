# Sending emails

The [emails](/guides/emails) guide covered creating email templates and sending them. This guide covers setting up the rest of the infrastructure.

!!! note
    Commercial services mentionned here are chosen for their quality. No commercial affiliation.

## Using a cloud provider

There are many available providers. Below we list some of the most popular ones. As many offer a free plan, it is good to have 2 setup with one as backup in case of outages.

| Name | Location | Price |
| --- | --- | --- |
| [Mailgun](https://www.mailgun.com/) | US, EU | 100 emails/day for free, 10k emails for 15$/month in the base plan
| [Brevo](https://www.brevo.com) | EU | 300 emails/month for free, 5k emails for 7€/month in the base plan
| [Postmark](https://postmarkapp.com/) | US | 100 emails/month for free, 10k emails for 15$/month in the base plan
| [Sendgrid](https://sendgrid.com) | US (EU available for extra) | 20$/month for 50k+ emails in the base plan
| [Amazon SES](https://aws.amazon.com/ses/) | US, EU, Asia, ... | 0.10 USD / 1000 emails

To use one of these services with hyperflask, retrieve the SMTP connection settings from your account and configure your app accordingly.

Remember to properly configure SPF, DKIM and DMARC to guarantee delivery.

## Self-hosting an SMTP server

We do not recommand self-hosting your SMTP server as delivery guarantee is tough for unknown servers.

If you wish to go this route, simply installing `postfix` and properly configuring your DNS will get you started.