# Crawl the web here
websites = {
    "site1": "The cow goes moo",
    "site2": "All hail the lord of cow for the moo bringeth",
    "site3": "Ducks 101 now offered at University of Central Florida"
}


# Create your index
inverted_index = {}
for website_url, website_content in websites.items():
    content = website_content.split()

    for word in content:
        if word not in inverted_index:
            inverted_index[word] = set()
        
        inverted_index[word].add(website_url)


# Lets search our index!
search_query = "duck goes moo"
search_results = set()
for word in search_query.split():
    try:
        results = list(inverted_index[word])
        for result in results:
            search_results.add(result)
    except KeyError:
        print(f"Error! The word {word} is not in our index!")

# Display our results
print("==========================")
print(f"You searched: \"{search_query}\" ")
print("Results: ")
print(results)
print("==========================")
