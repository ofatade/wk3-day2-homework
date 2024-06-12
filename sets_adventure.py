# Task 1: Flight Route Comparison 

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_dest = our_routes.intersection(competitor_routes)
print(common_dest)

print('='*75)

unique_dest = our_routes.difference(competitor_routes)
print(unique_dest)

print('='*75)

non_similar_dest = our_routes.symmetric_difference(competitor_routes)
print(non_similar_dest)