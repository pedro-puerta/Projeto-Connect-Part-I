import tweepy as tw

bearer_token = 'AAAAAAAAAAAAAAAAAAAAACv%2BeAEAAAAA%2FCaj8X9MF3VIheMO5%2BPiVfr9Ago%3DsLhQpyb2kB023Ua2w6j0CqSYNqTxtB4IgCo0348ornUPquMPwz'
consumer_key = 'nQ1oVFgRAwrMeFuDAlDKgtNaL'
consumer_secret = 'WSAEzoGwRLQoyjEw8aJR9JlOy9zdnMzYlq3eqjHGKauOSwwy9I'
access_token = '191265085-PZcFVKvcp8wtgxLiW2cENaAYkhVb5NIjOEPypVBy'
access_token_secret = 'JHxGMtKeQRpB4zSs4cDieMRcRih7wOqgTyeML306Kflxw'

cliente = tw.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

def busca():

    busca = cliente.search_recent_tweets(query='internet', max_results=30)

    return busca
