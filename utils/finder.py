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
from utils.search import search_string, search_dict
import pandas as pd
import os
import sys


def quote_find(arg1, page_number):
    """Search and find the quote and return both the line containing the quote as well as
     the next line, chapter heading of the chapter where the quote was found
     and quote found counter
     """
    file1 = resource_path(
        "data/Harry Potter and the Prince of Slytherin_pt.txt")
    file2 = resource_path(
        "data/Harry Potter and the Prince of Slytherin_md.txt")
    # book_lines=list of all the lines of the book and line_number=line number where string is found
    book_lines, line_number1, quote_found_ctr = search_string(
        file1, file2, arg1)
    # Subtracting 1 from the line_number list because of mismatch of line number when all the lines were assigned to list book_lines
    line_number2 = [x - 1 for x in line_number1]
    result = []  # list contains the line where the quote was found and the next line
    chapter_heading = []  # line containg the chapter heading
    try:
        if quote_found_ctr == 0:  # if no string found in the file
            return 'err', 'err', quote_found_ctr, len(line_number2)
        for i in range(1):
            result.append(book_lines[line_number2[page_number]].rstrip())
            # line at which the quote was found
            if len(line_number2) > page_number:
                quote_found = line_number2[page_number]
            else:
                quote_found = line_number2[len(line_number2)]
            quote_found_ctr = 1

    except IndexError:
        quote_found_ctr = 2  # if the page number croses the len(line_number2)
        return 'err', 'err', quote_found_ctr, len(line_number2)
    if quote_found < 51316:  # after line number 51316, ". HB&" starts
        pos_book_tag = ". HP&"  # till chapter 138
    else:  # pos_book_tag is the identifier used to recognize the book name i.e. HP or HB
        pos_book_tag = ". HB&"  # from chapter 139
    for i in range(quote_found, 0, -1):
        if pos_book_tag in book_lines[i]:
            # append all the lines containing the chapter heading from the last chapter to the chapter containing the quote_found
            chapter_heading.append(book_lines[i])
    quote_found += 2  # line number of the next line after the line where the quote was found
    next_line = book_lines[quote_found]  # Next line of the quote
    str1 = ""  # final output string
    for i in range(1):
        # Assigning the 1st value of the result list i.e. the line containing the quote
        str1 += result[0]
        str1 += "\n\n"  # Two nextlines to make it more clean
        str1 += next_line  # Concatinating both the line containing the quote and the next line
    if len(chapter_heading) == 0:
        # dummy book+chap name
        chapter_heading.append("0. HP&POS 0: First Page")
    # To fix the embed.description: Must be 2048 or fewer in length error
    if len(list(str1)) > 2048:
        str1 = str1[:2020] + "..."
    # chapter_heading[0] contains the chapter heading of the chapter where the quote was found
    return str1, chapter_heading[0], quote_found_ctr, len(line_number2)


def get_dict_index():
    """ Read the Title column of the excel file and assign it
     to index and return the index
    """
    file1 = resource_path("data/POS Dictionary.xlsx")
    df = pd.read_excel(file1,
                       sheet_name=0)
    df.set_index('Title')
    df.dropna()
    index = df['Title'].values[:]
    index = index[~pd.isnull(index)]
    return index


def pos_dict(arg, page):
    """ Call search_dict() and return title,
    description & quote_found_ctr
    """
    file2 = resource_path("data/POS Dictionary.json")
    title, description, quote_found_ctr, page_limit = search_dict(
        file2, arg, page)
    description += '\n\n' + "Page: "+str(page+1)+'/'+str(page_limit)
    return title, description, quote_found_ctr, page_limit


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
