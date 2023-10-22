# russian-text-tools
Scripts for working with Russian (Cyrillic) text

## Current Tools
* replace words with their dictionary form (говорю --> говори́ть)
* add stress marks (говорю --> говорю́, еще --> ещё)
* replace accent marks with apostraphes (говорю́ --> говорю')
* replace apostraphes with accent marks (говорю' --> говорю́)
* strip all accent marks and apostraphes (говорю́ --> говорю)

Please open an issue or PR for any suggested new tools/features



## Quickstart

### tools.py command line script
* Download tools.py, and the words and word_forms csv files from [OpenRussian.org's database](https://app.togetherdb.com/db/fwoedz5fvtwvq03v/russian3/words)
* Then run python3 tools.py --help for options using the script 

### index.html + script.js online script
* https://joshm21.github.io/russian-text-tools/
* Note: this page does not support replacing words with their dictionary forms or adding stress marks.
    * Doing so would require loading all the data on a static page (extremely long loading time)
    * or deploying server code that could be fetched from the static page (I don't want to deploy anything, and can't fetch from OpenRussian.org because of CORS)

