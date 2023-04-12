# Cloudflare-Bulk-DNS-Delete
This repository contains a python script to delete all DNS records for a certain zone on CloudFlare. 

As one website can have several hundred to thousand different DNS zones, the deletion of these DNS records cannot be manually completed in an efficient way on CloudFlare, as each DNS record must be selected and manually deleted. The only other way to delete records is to delete the entire website from your CloudFlare account, potentially losing other configurations.

This tool allows you to use CloudFlare's API to delete all DNS records from a certain website/zone from your CloudFlare account. It will attempt authorization before prompting total deletion.

> :warning: Fill in the Zone ID and API Key in the script with your own info. If you create a restricted API key on CloudFlare, it **must have DNS read/write permissions.**

[How to create an API Key on CloudFlare](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)

[How to find my Website Zone ID](https://developers.cloudflare.com/fundamentals/get-started/basic-tasks/find-account-and-zone-ids/)


