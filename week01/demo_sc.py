import requests
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt

def get_internal_links(url, domain):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all anchor tags with href attribute
        anchors = soup.find_all('a', href=True)
        
        # Extract internal links
        internal_links = [a['href'] for a in anchors if domain in a['href']]
        
        return internal_links
    except:
        return []

def check_for_404(domain):
    visited = set()
    to_visit = [domain]
    error_links = []
    
    start_time = datetime.now()
    
    while to_visit:
        current_url = to_visit.pop()
        if current_url not in visited:
            visited.add(current_url)
            
            try:
                response = requests.get(current_url)
                if response.status_code == 404:
                    error_links.append(current_url)
                else:
                    # Add internal links to the to_visit list
                    to_visit.extend(get_internal_links(current_url, domain))
            except:
                pass
    
    end_time = datetime.now()
    duration = end_time - start_time
    
    report_data = {
        'Total URLs Visited': len(visited),
        'Total 404 URLs': len(error_links),
        '404 URLs': error_links,
        'Duration': str(duration)
    }
    
    return report_data

def generate_report(data):
    print(f"Total URLs Visited: {data['Total URLs Visited']}")
    print(f"Total 404 URLs: {data['Total 404 URLs']}")
    print(f"Duration: {data['Duration']}")
    
    # If there are any 404 URLs, list them
    if data['404 URLs']:
        print("\nList of 404 URLs:")
        for url in data['404 URLs']:
            print(f"- {url}")
    
    # Generating a pie chart for visualization
    labels = ['404 URLs', 'Valid URLs']
    sizes = [data['Total 404 URLs'], data['Total URLs Visited'] - data['Total 404 URLs']]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)
    
    plt.figure(figsize=(10,7))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Distribution of Valid and 404 URLs')
    plt.show()

def main():
    # Execute
    domain = "https://www.msd321.com/"
    data = check_for_404(domain)
    generate_report(data)

if __name__ == "__main__":
    main()
