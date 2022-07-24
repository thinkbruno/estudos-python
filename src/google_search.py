# PEP8 OK
# -*- coding: utf-8 -*-

# PEP8 OK
# -*- coding: utf-8 -*-

from googlesearch import search

query = 'pudim'

result = list(search(query, lang='pt-br', num_results=5))


print(result)
