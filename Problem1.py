our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_route = our_routes.intersection(competitor_routes)
print(common_route)

unique_route = our_routes.difference(competitor_routes  )
print(unique_route)

difference = our_routes.symmetric_difference(competitor_routes)
print(difference)