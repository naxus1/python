def  getMovieTitles(substr):
    list_movies = []
    counter = 1
    try:
        json_list = "https://jsonmock.hackerrank.com/api/movies/search/?Title={}".format(substr)
        user = {'User-Agent': ''}
        my_list = requests.get(json_list, headers=user, params={'limit': 10})
        all_pages = int(my_list.json().get('total_pages'))
        
        while counter <= all_pages:
            json_list = "https://jsonmock.hackerrank.com/api/movies/search/?Title={}&page={}".format(substr, counter)
            user = {'User-Agent': ''}
            my_list = requests.get(json_list, headers=user)
            all_data = my_list.json().get('data')
            for data in all_data:
                list_movies.append(data.get('Title'))
            counter += 1

    except:
        print(None)
    return sorted(list_movies)