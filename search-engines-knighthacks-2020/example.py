import pprint
# Crawl the web here
# It returns a Python Dict
# Dict is just like a hashtable
example_dict = {"keys": "values", 0: "turtles", 2.2: 1} 

websites = {
    "site1": "The the cow goes moo",
    "site2": "All hail the lord of cow for the moo bringeth",
    "site3": "Ducks 101 now offered at University of Central Florida",
    "site4": "KnightHacks is awesome"
}


# Create your index
inverted_index = {}
tuples_example = ("url", "whats on the site")

for website_url, website_content in websites.items():
    sentence = website_content.split()

    for word in sentence:
        if word not in inverted_index:
            inverted_index[word] = set()
        
        inverted_index[word].add(website_url)

# Display our inverted index
print("==========================")
print(inverted_index)
print("==========================")

# Lets search our index!
search_query = "What is pie"
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
