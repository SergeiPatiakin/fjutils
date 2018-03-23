import http.client
from base64 import b64encode


def bitbucket_create(username, reponame, password):
    """Create a bitbucket repository"""
    # This sets up the https connection
    conn = http.client.HTTPSConnection("api.bitbucket.org")
    # we need to base 64 encode it, then decode to ascii
    user_and_pass = b64encode(
        bytes("{0}:{1}".format(username, password),
              encoding='ISO-8859-1')).decode("ascii")
    headers = {
        'Authorization': 'Basic %s' % user_and_pass,
        'Content-Type': 'application/json',
    }
    body = '{"scm": "git", "is_private": true}'
    # conn.request('GET', '/2.0/repositories/{0}/{1}'.format(username, reponame), headers=headers)
    conn.request(
        'POST',
        '/2.0/repositories/{0}/{1}'.format(username, reponame),
        headers=headers,
        body=body)
    response = conn.getresponse()
    assert response.status == 200, response.read()
