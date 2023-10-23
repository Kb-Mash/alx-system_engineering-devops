#!/usr/bin/python3
""" Python script to export data in the JSON format. """
from json import dump
import requests
from sys import argv

if __name__ == "__main__":

    def make_request(resource, param=None):
        '''Script that exports an employee TODO tasks to a json file
        Parameters:
        employee_id: Is an interger representing an employee id.
    '''
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if param:
            url += ('?' + param[0] + '=' + param[1])

        # make request
        r = requests.get(url)

        # extract json response
        r = r.json()
        return r

    user = make_request('users', ('id', argv[1]))[0]
    tasks = make_request('todos', ('userId', argv[1]))

    # format before exporting
    user_id = user['id']
    export = {user_id: []}
    for task in tasks:
        export[user_id].append({'task': task['title'],
                                'completed': task['completed'],
                                'username': user['username']})

    filename = argv[1] + '.json'
    with open(filename, mode='w') as f:
        dump(export, f)
