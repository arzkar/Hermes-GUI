# Copyright (C) 2021 Arbaaz Laskar
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
from utils.string_processing import chapter_processing
from utils.finder import get_dict_index, quote_find, pos_dict


def get_output(x, arg, page=0):
    if x == 1:
        return quote_page(arg, page)
    elif x == 2:
        return dict_page(arg, page)
    elif x == 3:
        return index_page(page)


def quote_page(arg, page):  # page=0 so that 1st page is sent first
    """ Call quote_find() and process the chapter_title & chapter_url
    and return the embed and page_limit
    """
    chapter_description, chapter_heading, quote_found_ctr, page_limit = quote_find(
        arg, page)
    if quote_found_ctr == 1:  # to fix the  UnboundLocalError: local variable 'loc_of_and' referenced before assignment error
        chapter_title, chapter_url = chapter_processing(
            chapter_heading)
    chapter_description += "\n" + \
        "Page: "+str(page+1)+'/'+str(page_limit)
    if quote_found_ctr == 1:
        title = ''.join(chapter_title)
    elif quote_found_ctr == 0:
        title = ""
        chapter_url = ""
        chapter_description = "Quote not found!"
    elif quote_found_ctr == 2:
        title = ""
        chapter_url = ""
        chapter_description = "No more quotes found!"
    return title, chapter_description, chapter_url, page_limit


def index_page(page):
    """ Call get_dict_index() & divide_chunks() and return
    the embed & limit
    """
    des = get_dict_index()
    # Divide the index list into chunks so that there are 10 in each page
    res = list(divide_chunks(des, 10))
    limit = len(res)
    url = ""
    if page < limit:
        title = 'POS Dictionary Index'
        description = '\n'.join(res[page])
        description += "\n\n" + \
            "Page: "+str(page+1)+'/'+str(limit)
    else:
        title = ''
        description = "No more index data!"
    return title, description, url, limit


def dict_page(arg, page):
    title, description, quote_found_ctr, page_limit = pos_dict(arg, page)
    if quote_found_ctr == 1:
        chapter_url = ""
    elif quote_found_ctr == 0:
        title = ""
        chapter_url = ""
        description = "Dictionary data not found!"
    elif quote_found_ctr == 2:
        title = ""
        chapter_url = ""
        description = "No more dictionary data found!"
    return title, description, chapter_url, page_limit


def divide_chunks(list1, n):
    """ Divide the index list into 'n' equal chunks
    """
    for i in range(0, len(list1), n):
        yield list1[i:i + n]
