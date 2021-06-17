# import libraries
import api_keys as ak
import tweepy

# authentication of credentials
auth = tweepy.OAuthHandler(ak.consumerKey, ak.consumerKeyPrivate)
	
#setting authorization
auth.set_access_token(ak.accessKey, ak.accessKeyPrivate)

#object for accessing tweets
api = tweepy.API(auth)

# retrieve posts

# API.search(q[, geocode][, lang][, locale][, result_type][, count][, until][, since_id][, max_id][, include_entities])

# Parameters:	
	# q – the search query string of 500 characters maximum

	# geocode – Returns tweets by users located within a given radius of the given latitude/longitude. The parameter value is specified by “latitide,longitude,radius”, where radius units must be specified as either “mi” (miles) or “km” (kilometers). 

	# lang – Restricts tweets to the given language

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

posts = api.search(q = word, lang = "en", count = 2, tweet_mode = "extended", result_type = "popular")

# store tweet part of tweets in a list

tweets = []
i = 0
for tweet in posts[0: 2]:
	tweets.insert(i, tweet.full_text)
	i = i + 1
	
# creating a dataframe
	
import pandas as pd
df = pd.DataFrame(tweets, columns = ['Tweets'])
	
# store data in csv
	# DataFrame.to_csv(path_or_buf=None, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)
	
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
		# Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc., if using a URL that will be parsed by fsspec

df.to_csv(path_or_buf = 'data.csv', columns = ['Tweets'], index = False, mode = 'w')


