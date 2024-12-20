# Cloudflare-Bulk-DNS-Delete
This repository contains a Python script to permanently delete all DNS records for a certain zone on CloudFlare. 

As one website can have hundreds to thousands of DNS zones, the deletion of those DNS records cannot be manually completed in an efficient way on CloudFlare.com, as each DNS record must be selected and manually deleted online. The only other way to delete all records is to delete the entire website from your CloudFlare account, potentially losing other configurations.

This tool leverages CloudFlare's API to delete all DNS records from a certain website/zone from your CloudFlare account. It will attempt authorization before prompting for total deletion. This can be useful when reworking website DNS configurations or migrating servers.
> [!TIP]
> Fill in the Zone ID and API Key within the script with your own info. If you create a restricted API key on CloudFlare, it **must have DNS read & write permissions. (``Zone.DNS``)**

[How do I create an API key/token on Cloudflare?](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)

[How do I find my website zone ID?](https://developers.cloudflare.com/fundamentals/get-started/basic-tasks/find-account-and-zone-ids/)

> [!CAUTION]
> Deletion deletes ALL records; it cannot be undone. For contingency measures, is recommended to export all website DNS records before using this script. [Learn more here.](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/)
