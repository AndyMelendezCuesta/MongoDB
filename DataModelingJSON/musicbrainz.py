# To experiment with this code freely you will have to run this code locally.
# Take a look at the main() function for an example of how to use the code.
# We have provided example json output in the other code editor tabs for you to
# look at, but you will not be able to run any queries through our UI.
import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    # This is the main function for making queries to the musicbrainz API.
    # A json document should be returned by the query.
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    # This adds an artist name to the query parameters before making
    # an API call to the function above.
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    # After we get our output, we can format it to be more readable
    # by using this function.
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():
    # results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    # pretty_print(results)

    # artist_id = results["artists"][1]["id"]
    # print "\nARTIST:"
    # pretty_print(results["artists"][1])

    # artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    # releases = artist_data["releases"]
    # print "\nONE RELEASE:"
    # pretty_print(releases[0], indent=2)
    # release_titles = [r["title"] for r in releases]

    # print "\nALL TITLES:"
    # for t in release_titles:
    #     print t

    # Question 1: How many bands named "First Aid Kit"?
    results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
    # pretty_print(results)
    count_FAK = 0

    for artist in results["artists"]:
        # pretty_print(artist)

        if artist["name"] == "First Aid Kit":
            count_FAK += 1

    print "There are {0} bands named First Aid Kit".format(count_FAK)        

    # Question 2: Begin_area name for Queen?
    results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
    # pretty_print(results)

    Queen = results["artists"][0]

    print "The begin-area name for Queen is " + Queen["begin-area"]["name"]

    # Question 3: Spanish alias for The Beatles?
    results = query_by_name(ARTIST_URL, query_type["simple"], "The Beatles")
    # pretty_print(results)

    for alias in results["artists"][0]["aliases"]:
        if alias["locale"] == "es":
            print "The Spanish alias for The Beatles is " + alias["name"]

    # Question 4: Nirvana disambiguation?
    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    # pretty_print(results)

    print "The disambiguation for Nirvana is " + results["artists"][0]["disambiguation"]

    # Question 5: Where was One Direction formed?
    results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
    # pretty_print(results)

    print "One Direction was formed in " + results["artists"][0]["life-span"]["begin"]



if __name__ == '__main__':
    main()

# Andreas-MacBook-Pro-2:Desktop andreamelendezcuesta$ cd Desktop
# Andreas-MacBook-Pro-2:Desktop andreamelendezcuesta$ python musicbrainz.py
# requesting http://musicbrainz.org/ws/2/artist/?query=artist%3AFirst+Aid+Kit&fmt=json
# There are 2 bands named First Aid Kit
# requesting http://musicbrainz.org/ws/2/artist/?query=artist%3AQueen&fmt=json
# The begin-area name for Queen is London
# requesting http://musicbrainz.org/ws/2/artist/?query=artist%3AThe+Beatles&fmt=json
# The Spanish alias for The Beatles is Los Beatles
# requesting http://musicbrainz.org/ws/2/artist/?query=artist%3ANirvana&fmt=json
# The disambiguation for Nirvana is 90s US grunge band
# requesting http://musicbrainz.org/ws/2/artist/?query=artist%3AOne+Direction&fmt=json
# One Direction was formed in 2010-07
