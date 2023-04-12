import requests

print("Attempting Authentication with Provided Token...")

# Set the required parameters
zone_id = "<ENTER ZONE ID HERE. FIND THIS ON YOUR SITE OVERVIEW WINDOW ON CLOUDFLARE.>"
api_key = "<ENTER THE API KEY FOR YOUR ACCOUNT>"

auth_url = "https://api.cloudflare.com/client/v4/user/tokens/verify"

auth_headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

auth_response = requests.get(auth_url, headers=auth_headers)

if auth_response.status_code == 200:

    do_delete = input("Authenticated! Are you sure you want to delete ALL dns records? This action cannot be reversed! [y/n]: ")
    if(do_delete != "y"):
        print("Aborting!")
        quit() 

    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    delCount = 0

    if response.status_code == 200:
        data = response.json()
        for record in data["result"]:
            record_id = record["id"]
            delete_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
            delete_response = requests.delete(delete_url, headers=headers)
            if delete_response.status_code == 200:
                print(f"Record {record['name']} deleted successfully.")
                delCount += 1
            else:
                print(f"Failed to delete record {record['name']}.")
                print(delete_response.json())

        print("Done! Deleted a total of " + str(delCount) + " DNS records!")
    else:
        print("Failed to fetch DNS records.")
        print(response.json())
else:
    print("Authentication failed.")
    print(auth_response.json())
