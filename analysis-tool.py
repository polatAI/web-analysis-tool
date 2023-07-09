import requests

def detailed_analysis(domain):
    url = "https://api.similarweb.com/v1/website/{}/lead-enrichment/all".format(domain)
    params = {
        "api_key": "Add your API key here",
        "start_date": "2023-01",
        "end_date": "2023-03",
        "country": "ae,af,am,az,bd,bh,bn,bt,cn,ge,hk,id,il,in,iq,ir,jo,jp,kg,kh,kr,kw,kz,la,lk,lb,mm,mn,my,np,om,ph,pk,ps,qa,ru,sd,sg,th,tj,tl,tm,tr,tw,tz,uz,vn,ye",
        "main_domain_only": False,
        "format": "json",
        "show_verified": False
    }
    headers = {"accept": "application/json"}
    response = requests.get(url, params=params, headers=headers)
    return response.text

def subdomain_detection(domain):
    url = "https://api.similarweb.com/v4/website/{}/website-content-subdomains/subdomains".format(domain)
    params = {
        "api_key": "Add your API key here",
        "start_date": "2023-01",
        "end_date": "2023-03",
        "country": "ae,af,am,az,bd,bh,bn,bt,cn,ge,hk,id,il,in,iq,ir,jo,jp,kg,kh,kr,kw,kz,la,lk,lb,mm,mn,my,np,om,ph,pk,ps,qa,ru,sd,sg,th,tj,tl,tm,tr,tw,tz,uz,vn,ye",
        "main_domain_only": False,
        "format": "json",
        "limit": 100
    }
    headers = {"accept": "application/json"}
    response = requests.get(url, params=params, headers=headers)
    return response.text

def website_traffic(domain):
    url = f"https://api.similarweb.com/v2/website/{domain}/mobile-web/visits"
    params = {
        "api_key": "Add your API key here",
        "start_date": "2023-01",
        "end_date": "2023-03",
        "country": "ae,af,am,az,bd,bh,bn,bt,cn,ge,hk,id,il,in,iq,ir,jo,jp,kg,kh,kr,kw,kz,la,lk,lb,mm,mn,my,np,om,ph,pk,ps,qa,ru,sd,sg,th,tj,tl,tm,tr,tw,tz,uz,vn,ye",
        "granularity": "monthly",
        "main_domain_only": False,
        "format": "json",
        "show_verified": False,
        "mtd": False
    }
    headers = {"accept": "application/json"}
    response = requests.get(url, params=params, headers=headers)
    return response.text


domain_list_file = input("Please enter the domain list filename: ")

analysis_results = []
subdomain_results = []
traffic_results = []

with open(domain_list_file, "r", encoding="UTF-8") as file:
    domain_list = file.read().splitlines()
    for domain in domain_list:
        print(f"\nPerforming detailed analysis for {domain}...")
        
        analysis_result = detailed_analysis(domain.strip())
        
        print(f"Detailed analysis result:\n{analysis_result}\n")
        analysis_results.append(analysis_result)
        
        print(f"Detecting subdomains for {domain}...")
        subdomain_result = subdomain_detection(domain.strip())
        
        print(f"Subdomain detection result:\n{subdomain_result}\n")
        subdomain_results.append(subdomain_result)
        
        with open(f"{domain}_subdomain.txt", "w", encoding="UTF-8") as file:
            file.write(subdomain_result)
        
        print(f"Performing website traffic analysis for {domain}...")
        traffic_result = website_traffic(domain.strip())
        
        print(f"Website traffic result:\n{traffic_result}\n")
        traffic_results.append(traffic_result)

print("\nOperation completed.")

for i, domain in enumerate(domain_list):
    with open(f"{domain}_analysis.txt", "w", encoding="UTF-8") as file:
        file.write(analysis_results[i])
    
    with open(f"{domain}_traffic.txt", "w", encoding="UTF-8") as file:
        file.write(traffic_results[i])
