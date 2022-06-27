#
# ISC License
#
# Copyright (C) 2021-present DS-Homebrew
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

import json
from typing import Any, Dict


def loadSettings() -> Dict[str, Any]:
    # Load config
    with open("settings.json", "r") as f:
        settings = json.load(f)

    ret = {}
    # bot internals
    ret['TOKEN'] = settings['DEFAULT']['TOKEN']
    ret['PREFIX'] = [x for x in settings['DEFAULT']['PREFIX']]
    ret['STATUS'] = settings['DEFAULT']['STATUS']
    ret['GSPREADKEY'] = settings.get('GSPREADKEY')

    # server specifics
    ret['GUILD'] = settings.get('GUILD')
    ret['staff_roles'] = [x for x in settings['MODERATOR']]

    # channels
    ret['NINUPDATE'] = settings['CHANNEL']['NINUPDATES']
    ret['SUBREDDIT'] = settings['CHANNEL']['SUBREDDIT']
    ret['GITHUBUPDATES'] = settings['CHANNEL']['GITHUBUPDATES']

    # threads
    ret['TWLUPDATES'] = settings['THREAD']['TWLUPDATES']
    ret['NDSBUPDATES'] = settings['THREAD']['NDSBUPDATES']
    ret['WEBUPDATES'] = settings['THREAD']['WEBUPDATES']
    ret['MISCUPDATES'] = settings['THREAD']['MISCUPDATES']

    return ret
