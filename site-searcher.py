import requests


def collect_similar_sites(domain_list):
    with open("similar_sites.txt", "w", encoding="utf-8") as f:
        for domain in domain_list:
            url = "https://api.similarweb.com/v4/website/{}/similar-sites/similarsites?api_key=Add_Your_API_KEY&format=json&limit=40".format(domain)
            headers = {"accept": "application/json"}
            response = requests.get(url, headers=headers)
            data = response.json()
            for site in data["sites"]:
                print(site["name"])
                f.write(site["name"] + "\n")
            print("---------------")


def keyword_search(keyword_list):
    with open("keyword_results.txt", "w", encoding="utf-8") as f:
        for keyword in keyword_list:
            url = "https://api.similarweb.com/v4/keywords/{}/analysis/organic-competitors?api_key=Add_Your_API_KEY&start_date=2023-01&end_date=2023-03&country=us&metrics=traffic%2Corganic-vs-paid%2Cvolume%2Ccpc&format=json&limit=100".format(keyword)
            headers = {"accept": "application/json"}
            response = requests.get(url, headers=headers)
            data = response.json()
            for competitor in data["competitors"]:
                print(competitor["site"])
                f.write(competitor["site"] + "\n")
            print("---------------")


while True:
    print("Options:")
    print("1 - Get 40 similar sites based on domain")
    print("2 - Get sites based on keywords")
    choice = input("Please select '1' or '2': ")

    if choice == "1":
        domain_list = input("Please enter comma-separated domain list: ").split(",")
        collect_similar_sites(domain_list)
        break
    elif choice == "2":
        keyword_list = input("Please enter comma-separated keyword list: ").split(",")
        keyword_search(keyword_list)
        break
    else:
        print("You have selected an invalid option. Please try again.")

print("Operation completed.")
