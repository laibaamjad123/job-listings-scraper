from playwright.sync_api import sync_playwright
import csv

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://realpython.github.io/fake-jobs/")
    
    page.wait_for_selector(".card")
    
    jobs = page.query_selector_all(".card")
    
    with open("C:/Users/dell/Desktop/jobs.csv", "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Location"])
        
        for job in jobs:
            title = job.query_selector("h2").inner_text()
            company = job.query_selector("h3").inner_text()
            location = job.query_selector("p.location").inner_text()
            writer.writerow([title, company, location])
    
    print("Done! jobs.csv created!")
    
    browser.close()