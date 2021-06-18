def main():
    import sentimentAnalysis
    import api_keys
    import tweepy
    import pandas as pd
    import re

    # ------------------Input keyword to search for in tweets------------------------

    query = input("\n\nEnter a keyword to search for: ")

    flag = 0

    # ---------checking input--------

    while(flag == 0):
        if(len(query) > 500):
            print(
                "Query length too long\nQuery should not be greater than 500 characters!")
        elif(query.isspace()):
            print("\nQuery cannot contains only spaces!")
        elif(len(query) == 0):
            print("\nQuery cannot be empty!")
        else:
            flag = 1
        if(flag == 0):
            query = input("\n\nEnter a keyword to search for: ")

    type = input("What type of tweets to search for? (popular/top/mixed): ")
    type = type.lower()
    while(type != "popular" and type != "top" and type != "mixed"):
        print("Wrong type entered!")
        type = input(
            "What type of tweets to search for? (popular/top/mixed): ")
        type = type.lower()

    count = int(input("Entered the number of tweets to fetch: "))
    while(count <= 0):
        print("Error: count should be greater than 0")
        count = int(input("Entered the number of tweets to fetch: "))

    # ------------------------Retrieving Tweets--------------------

    auth = tweepy.OAuthHandler(
        api_keys.consumerKey, api_keys.consumerKeyPrivate)
    auth.set_access_token(api_keys.accessKey, api_keys.accessKeyPrivate)
    api = tweepy.API(auth)

    posts = api.search(q=query, count=count, lang="en",
                       result_type=type, tweet_mode="extended")

    # API.search(q[, geocode][, lang][, locale][, result_type][, count][, until][, since_id][, max_id]
    # [, include_entities])
    # Parameters:
    # q – the search query string of 500 characters maximum, including operators. Queries may additionally be limited by complexity.
    # geocode – Returns tweets by users located within a given radius of the given latitude/longitude. The location is preferentially taking from the Geotagging API, but will fall back to their Twitter profile. The parameter value is specified by “latitide,longitude,radius”, where radius units must be specified as either “mi” (miles) or “km” (kilometers). Note that you cannot use the near operator via the API to geocode arbitrary locations; however you can use this geocode parameter to search near geocodes directly. A maximum of 1,000 distinct “sub-regions” will be considered when using the radius modifier.
    # lang – Restricts tweets to the given language, given by an ISO 639-1 code. Language detection is best-effort.
    # locale – Specify the language of the query you are sending (only ja is currently effective). This is intended for language-specific consumers and the default should work in the majority of cases.
    # result_type –
    # Specifies what type of search results you would prefer to receive. The current default is “mixed.” Valid values include:
    # mixed : include both popular and real time results in the response
    # recent : return only the most recent results in the response
    # popular : return only the most popular results in the response
    # count – The number of results to try and retrieve per page.
    # until – Returns tweets created before the given date. Date should be formatted as YYYY-MM-DD. Keep in mind that the search index has a 7-day limit. In other words, no tweets will be found for a date older than one week.
    # since_id – Returns only statuses with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occurred since the since_id, the since_id will be forced to the oldest ID available.
    # max_id – Returns only statuses with an ID less than (that is, older than) or equal to the specified ID.
    # include_entities – The entities node will not be included when set to false. Defaults to true.
    # Return type: SearchResults object

    df = pd.DataFrame([tweet.full_text for tweet in posts], columns=["Tweets"])
    # class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
    # Parameters
    # datandarray (structured or homogeneous), Iterable, dict, or DataFrame
    # Dict can contain Series, arrays, constants, dataclass or list-like objects. If data is a dict, column order follows insertion-order.

    # Changed in version 0.25.0: If data is a list of dicts, column order follows insertion-order.

    # indexIndex or array-like
    # Index to use for resulting frame. Will default to RangeIndex if no indexing information part of input data and no index provided.

    # columnsIndex or array-like
    # Column labels to use for resulting frame. Will default to RangeIndex (0, 1, 2, …, n) if no column labels are provided.

    # dtypedtype, default None
    # Data type to force. Only a single dtype is allowed. If None, infer.

    # copybool, default False
    # Copy data from inputs. Only affects DataFrame / 2d ndarray input.

    # ---------------------Preprocessing the tweets-----------------------

    def cleanTweet(tweet):
        tweet = re.sub(r'RT[\s]', '', tweet)
        tweet = re.sub(r'https?:\/\/\S+', '', tweet)
        tweet = re.sub(r'@[a-zA-Z0-9:]+', '', tweet)
        tweet = re.sub(r'#', '', tweet)
        tweet = re.sub(r'[\n]', '', tweet)
        return tweet

    df['Tweets'] = df['Tweets'].apply(cleanTweet)

    # ----------------Storing tweets in CSV file------------

    df.to_csv(path_or_buf='data.csv', columns=[
              'Tweets'], index=False, mode='w')

    # DataFrame.to_csv(path_or_buf=None, sep=',', na_rep='', float_format=None, columns=None,
    # header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer',
    # quoting=None, quotechar='"', line_terminator=None, chunksize=None, date_format=None,
    # doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)

    # Parameters
    # path_or_bufstr or file handle, default None
    # File path or object, if None is provided the result is returned as a string. If a non-binary file object is passed, it should be opened with newline=’’, disabling universal newlines. If a binary file object is passed, mode might need to contain a ‘b’.

    # sepstr, default ‘,’
    # String of length 1. Field delimiter for the output file.

    # na_repstr, default ‘’
    # Missing data representation.

    # float_formatstr, default None
    # Format string for floating point numbers.

    # columnssequence, optional
    # Columns to write.

    # headerbool or list of str, default True
    # Write out the column names. If a list of strings is given it is assumed to be aliases for the column names.

    # indexbool, default True
    # Write row names (index).

    # index_labelstr or sequence, or False, default None
    # Column label for index column(s) if desired. If None is given, and header and index are True, then the index names are used. A sequence should be given if the object uses MultiIndex. If False do not print fields for index names. Use index_label=False for easier importing in R.

    # modestr
    # Python write mode, default ‘w’.

    # encodingstr, optional
    # A string representing the encoding to use in the output file, defaults to ‘utf-8’. encoding is not supported if path_or_buf is a non-binary file object.

    # compressionstr or dict, default ‘infer’
    # If str, represents compression mode. If dict, value at ‘method’ is the compression mode. Compression mode may be any of the following possible values: {‘infer’, ‘gzip’, ‘bz2’, ‘zip’, ‘xz’, None}. If compression mode is ‘infer’ and path_or_buf is path-like, then detect compression mode from the following extensions: ‘.gz’, ‘.bz2’, ‘.zip’ or ‘.xz’. (otherwise no compression). If dict given and mode is one of {‘zip’, ‘gzip’, ‘bz2’}, or inferred as one of the above, other entries passed as additional compression options.

    # quotingoptional constant from csv module
    # Defaults to csv.QUOTE_MINIMAL. If you have set a float_format then floats are converted to strings and thus csv.QUOTE_NONNUMERIC will treat them as non-numeric.

    # quotecharstr, default ‘"’
    # String of length 1. Character used to quote fields.

    # line_terminatorstr, optional
    # The newline character or character sequence to use in the output file. Defaults to os.linesep, which depends on the OS in which this method is called (‘n’ for linux, ‘rn’ for Windows, i.e.).

    # chunksizeint or None
    # Rows to write at a time.

    # date_formatstr, default None
    # Format string for datetime objects.

    # doublequotebool, default True
    # Control quoting of quotechar inside a field.

    # escapecharstr, default None
    # String of length 1. Character used to escape sep and quotechar when appropriate.

    # decimalstr, default ‘.’
    # Character recognized as decimal separator. E.g. use ‘,’ for European data.

    # errorsstr, default ‘strict’
    # Specifies how encoding and decoding errors are to be handled. See the errors argument for open() for a full list of options.

    # storage_optionsdict, optional
    # Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc., if using a URL that will be parsed by fsspec, e.g., starting “s3://”, “gcs://”. An error will be raised if providing this argument with a non-fsspec URL. See the fsspec and backend storage implementation docs for the set of allowed keys and values.

    # Returns
    # None or str
    # If path_or_buf is None, returns the resulting csv format as a string. Otherwise returns None.

    input("\nData stored in CSV file successfully!\n\nPress any key to continue")

    # -----------calling Sentiment Analysis program---------------
    sentimentAnalysis.main()
